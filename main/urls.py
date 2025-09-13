from django.urls import path
from . import views
from .views import contact_view
from .views import bikes_list

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sell-bike/', views.sell_bike, name='sell-bike'),
     path('contact/', contact_view, name='contact'),
    path('buy-bike/', bikes_list, name='buy_bike'),
    path('bike/<int:pk>/', views.bike_detail, name='bike_detail'),
     path('bike/payment/<int:bike_id>/', views.payment_page, name='payment_page'),
    path('bike/confirm-payment/', views.confirm_payment, name='confirm_payment'),
      path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
