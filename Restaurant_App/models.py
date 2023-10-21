from django.db import models


# makemigraions - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations
 
# Create your models here.
class Contact(models.Model):
    f_name=models.CharField(max_length=10)
    l_name=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=10)
    desc=models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.f_name
    
class User_Data(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email =models.CharField(max_length=100)

    date = models.DateField()

# model for Product
class Categories(models.Model):
    item_id= models.AutoField
    item_name= models.CharField(max_length=30)
    category= models.CharField(max_length=10,default="")
    price=models.IntegerField(default=0)
    desc= models.CharField(max_length=100)
    image=models.ImageField(upload_to="static/images",default="")

    def __str__(self):
        return self.item_name