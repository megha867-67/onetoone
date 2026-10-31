from django.db import models
class Countries(models.Model):
    countryname=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.countryname

class Capital(models.Model):
    country = models.OneToOneField(
        Countries,on_delete=models.CASCADE,related_name='capital'
    )
    capitalname= models.CharField(max_length=100)
    def __str__(self):
        return self.capitalname

# Create your models here.
