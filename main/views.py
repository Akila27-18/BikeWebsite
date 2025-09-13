from django.shortcuts import render, redirect, get_object_or_404
from .models import Bike  # ✅ import the model

def home(request):
    bikes = Bike.objects.all()[:3]   # fetch all bikes
    return render(request, 'home.html', {'bikes': bikes})
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')


from django.shortcuts import render
import datetime

def sell_bike(request):
    current_year = datetime.datetime.now().year
    years = list(range(2000, current_year + 1))  # 2000 → current year
    years.reverse()  # So latest years come first (2025, 2024, 2023, ...)

    return render(request, "sell_bike.html", {"years": years})

# -------------forms-------------
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to same page or a thank-you page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
# -------------------------bike---------------

from django.shortcuts import render
from .models import Bike

def bikes_list(request):
    bikes = Bike.objects.all()

    # Params
    brand = request.GET.get('brand')
    year = request.GET.get('year')
    price_range = request.GET.get('price_range')
    kilometers = request.GET.get('kilometers')
    engine_cc = request.GET.get('engine_cc')
    fuel_type = request.GET.get('fuel_type')
    color = request.GET.get('color')
    sort_by = request.GET.get('sort_by')

    # Brand
    if brand:
        bikes = bikes.filter(brand__icontains=brand)

    # Year
    if year:
        bikes = bikes.filter(year=year)

    # Price
    if price_range:
        try:
            min_price, max_price = map(int, price_range.split('-'))
            bikes = bikes.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            pass

    # Kilometers
    if kilometers:
        try:
            min_km, max_km = map(int, kilometers.split('-'))
            bikes = bikes.filter(kilometers__gte=min_km, kilometers__lte=max_km)
        except ValueError:
            pass

    # Engine CC
    if engine_cc:
        try:
            min_cc, max_cc = map(int, engine_cc.split('-'))
            bikes = bikes.filter(engine_cc__gte=min_cc, engine_cc__lte=max_cc)
        except ValueError:
            pass

    # Fuel Type
    if fuel_type:
        bikes = bikes.filter(fuel_type__iexact=fuel_type)

    # Color
    if color:
        bikes = bikes.filter(color__iexact=color)

    # Sorting
    if sort_by == 'price_asc':
        bikes = bikes.order_by('price')
    elif sort_by == 'price_desc':
        bikes = bikes.order_by('-price')
    else:
        bikes = bikes.order_by('-id')  # newest first

    return render(request, 'buybike.html', {'bikes': bikes})

def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    return render(request, 'bike_detail.html', {'bike': bike})

def payment_page(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    context = {
        'bike': bike,
        'show_popup': False # Initial state, no popup
    }
    return render(request, 'payment_page.html', context)

def confirm_payment(request):
    if request.method == 'POST':
        # Here you would handle the payment logic (e.g., call a payment gateway API)
        # For this example, we'll just assume it's successful.
        
        # After successful payment, you can redirect back to the bike detail page
        # with a query parameter to trigger the popup.
        bike_id = request.POST.get('bike_id')
        return redirect('bike_detail', bike_id=bike_id)
        
    return redirect('bike_detail', bike_id=request.POST.get('bike_id'))


# your_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home_page') # Redirect to your desired home page
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

from .forms import RegisterForm  # or your custom form

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('login')  # Redirect to login after successful registration
    return render(request, 'register.html', {'form': form})

