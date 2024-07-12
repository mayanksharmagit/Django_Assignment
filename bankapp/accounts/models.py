from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    aadhar_no = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=10)
    account_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.account_number}"
