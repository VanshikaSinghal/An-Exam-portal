from django.db import models

# # Create your models here.
class Contact(models.Model):   
    sno= models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone= models.CharField(max_length=14)
    content = models.TextField() 
    timestamp =models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message From'+self.name

    
#to fetch  current events for the exam site for stet
class currentevents(models.Model):
    cno = models.AutoField(primary_key=True)
    file =models.FileField(upload_to ='portal/files' ,default='')
    filename = models.CharField(max_length=400)


# Create your models here.
class links(models.Model):   
    lno= models.AutoField(primary_key=True)
    lname=models.CharField(max_length=50)
    lcontent = models.CharField(max_length=250)
    

    def __str__(self):
        return self.lcontent

class news(models.Model):   
    nno= models.AutoField(primary_key=True)
    nname = models.CharField(max_length=50)
    news=models.CharField(max_length=250)

    def __str__(self):
        return self.nname
# to take registration of user
class Register(models.Model):
    applicantno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone = models.CharField(max_length=100 ,unique=True)
    pincode = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.phone
    
    class Imageupload(models.Model):
        imageno = models.AutoField(primary_key=True)
        phone = models.CharField(max_length=20)    
        tenmark =models.FileField(upload_to ='portal/docs/tenmark' ,default='')
        twmark =models.FileField(upload_to ='portal/docs/twmark' ,default='')
        gmark =models.FileField(upload_to ='portal/docs/gmark' ,default='')
        smark =models.FileField(upload_to ='portal/docs/smark' ,default='')
        bcertificate =models.FileField(upload_to ='portal/docs/birthcertificate' ,default='')
        ccertificate =models.FileField(upload_to ='portal/docs/ccertificate' ,default='')
        photo =models.FileField(upload_to ='portal/docs/photo' ,default='')
        sign =models.FileField(upload_to ='portal/docs/sign' ,default='')
        filename = models.CharField(max_length=400)

        def __str__(self):
            return self.phone

    
    
