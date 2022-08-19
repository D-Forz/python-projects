from django.db import models

# Create your models here.

class Delivery(models.Model):
    street = models.CharField(max_length=100)
    n_street = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"Delivery {self.id}: {self.street} {self.n_street} {self.city} {self.state}"
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"User {self.id}:  {self.first_name}, {self.last_name}, {self.email}"