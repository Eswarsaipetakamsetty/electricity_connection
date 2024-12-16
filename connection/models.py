from django.db import models

class ElectricityConnectionRequest(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    aadhar_number = models.BigIntegerField(unique=True)
    aadhar_card = models.FileField(upload_to="aadhar_cards/")
    subject = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"