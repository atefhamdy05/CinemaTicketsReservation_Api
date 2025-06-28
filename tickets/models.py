from django.db import models
class Movie(models.Model):
    name = models.CharField(max_length=50)
    hall = models.CharField(max_length=50) 
    
class Guest(models.Model):
    name = models.CharField(max_length=50)
    mobile= models.CharField( max_length=15)
    
class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name="reservation", on_delete=models.CASCADE)    
    movie = models.ForeignKey(Movie, related_name="reservation", on_delete=models.CASCADE)    

    