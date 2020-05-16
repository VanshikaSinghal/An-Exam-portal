from django.db import models

# Create your models here.
class Post(models.Model):   
    sno= models.AutoField(primary_key=True)
    topic=models.CharField(max_length=250)
    question=models.CharField(max_length=750)
    author = models.CharField(max_length=100)
    content = models.TextField() 
    slug =models.CharField(max_length=100)
    timestamp =models.DateTimeField(blank=True)
    

    def __str__(self):
        return self.topic +' by '+self.author
    
