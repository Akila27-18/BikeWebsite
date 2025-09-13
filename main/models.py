from django.db import models

class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    engine_cc = models.IntegerField()
    kilometers = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    owner_type = models.CharField(max_length=50)
    price = models.FloatField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/default.png')


    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
   

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reason = models.CharField(max_length=100)
    how_found = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    

