from django.db import models

# Create your models here.


    
class project(models.Model):
    name = models.CharField(max_length = 200)
    

class project1(models.Model):
    name1 = models.ForeignKey(project,on_delete = models.CASCADE)
    type = models.CharField(max_length = 100)

class project2(models.Model):
    name2 = models.ForeignKey(project,on_delete = models.CASCADE)
    type = models.CharField(max_length = 100)
    num = models.IntegerField()
    #img = models.ImageField(upload_to = 'upload')

class project3(models.Model):
    name3 = models.ForeignKey(project,on_delete = models.CASCADE)
    type = models.CharField(max_length = 100)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    #img = models.ImageField(upload_to = 'upload')

class project4(models.Model):
    name1 = models.ForeignKey(project,on_delete = models.CASCADE)
    type = models.CharField(max_length = 100)
    ad1 = models.CharField(max_length = 40)
    ad2 = models.CharField(max_length = 40)
    ad3 = models.CharField(max_length = 40)
    ad4 = models.CharField(max_length = 40)
    ad5 = models.CharField(max_length = 40)

class IMG(models.Model):
    img = models.ImageField(upload_to = 'img')
    
    
    
