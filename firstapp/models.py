from django.db import models

class Upload(models.Model):
    Customer_Name=models.CharField(max_length=50)
    Image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.Customer_Name
