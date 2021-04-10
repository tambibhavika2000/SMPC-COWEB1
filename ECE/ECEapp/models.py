from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
choices_year={(1,'First Year'),(2,'Second Year'),(3,'Third Year'),(4,'Final Year'),(5,'M.TECH'),(6,'PHD')}
choice_type={(1,'Thsesis'),(2,'Article'),(3,'Publication'),(4,'Conference Paper'),(5,'Chapter'),(6,'Patent'),
(7,'Poster'),(8,'Pre Print'),(9,'Research Internship  Report')}
choice_role={('FULL-TIME','Full Time'),('INTERNSHIP','Intern')}
choice_field={('IT','IT'),('ECE-CORE','ECE-CORE'),('MANAGERIAL','ANALYST')}


class Notice(models.Model):
     title=models.CharField(max_length=100,blank=False)
     url=models.FileField()

     def __str__(self):
         return self.title


class Project(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    abstract=models.CharField(max_length=10000)
    projecttype=models.IntegerField(choices=choice_type,default=1)
    url=models.URLField()
    def __str__(self):
        return self.title


class Faculty(models.Model):
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=10)
    research=models.CharField(max_length=500)
    pic=models.ImageField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField()
    role=models.CharField(max_length=10, choices=choice_role)
    doamin=models.CharField(max_length=10,choices=choice_field)
    elegibilty=models.CharField(max_length=10,blank=True,null=True)
    url=models.URLField(blank=True,null=True)
    pic=models.ImageField()

    def __str__(self):
        return self.name

class People(models.Model):
    year=models.IntegerField(choices=choices_year)
    rollno=models.CharField(max_length=8)
    phoneno=models.CharField(max_length=10)

    def __str__(self):
        return self.rollno

class Event(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField()
    url=models.URLField()
    desc=models.TextField(max_length=500)
    pic=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
