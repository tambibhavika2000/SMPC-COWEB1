from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
choices_year={(1,'First Year'),(2,'Second Year'),(3,'Third Year'),(4,'Final Year')}
choice_type={(1,'Thsesis'),(2,'Article'),(3,'Publication'),(4,'Conference Paper'),(5,'Chapter'),(6,'Patent'),
(7,'Poster'),(8,'Pre Print'),(9,'Research Internship  Report')}
# choices_division={(1,'A'),(2,'B')}
# choice_subjects={1,(('ASM101','ENGINEERING MATHEMATICS-I'),
#     ('ASP102ABC','ENGINEERING PHYSICS'),
#     ('ASC103ABC','ENGINEERING CHEMISTRY'),
#     ('AMD104ABC','ENGINEERING MECHANICS'),
#     ('CIME105ABC','ENGINEERING DRAWING'),
#     ('ASM201','ENGINEERING MATHEMATICS-II'),
#     ('ELE207ABC','ELECTROTECHNIQUES'),
#     ('COM208ABC','FUNDAMENTALS OF COMPUTER PROGRAMMING'),
#     ('ECE209ABC','BASIC OF ELECTRONICS ENGINEERING'),
#     ('MED210ABC','BASIC MECHANICAL SYSTEMS'),
#     ('CICH106ABC','BASIC OF CIVIL AND ENVIRONMENTAL ENGINEERING'),
#     ('ASE211ABC','ENGLISH AND COMMUNICATIO SKILLS'),
#     ('MED212ABC','WORKSHOP PRACTICE'),
#     ('MA217','ENGINEERING MATHEMATHICS III')),
#     2,(('EC201','ELECTRONICS CIRCUIT'),
#     ('EC203','DIGITAL LOGIC DESIGN'),
#     ('EC205','SIGNAL AND SYSTEM'),
#     ('EE207','NETWORK ANALYSIS AND SYSTEMS'),
#     ('EC202','STATICAL SIGNAL ANALYSIS'),
#     ('EC204','PRINCIPLE OF COMMUNICATION SYSTEM'),
#     ('EC206','MICROPROCESSORS AND MICROCONTROLLERS'),
#     ('EC208','LINEAR IC APPLICATIONS'),
#     ('EE214','CONTROL SYSTEMS')),
#     3,(('EC301','DIGITAL COMMUNICATIONS'),
#     ('EC303','DIGITAL SIGNAL PROCESSING'),
#     ('EC305','ANALOG INTEGRATED CIRCUITS'),
#     ('EC307','ELECTROMAGNETIC WAVES AND RADIATING SYSTEMS'),
#     ('EC302','DATA COMMUNICATIONS AND NETWORKS'),
#     ('EC304','DIGITAL INTEGRATED CIRCUITS'),
#     ('EC306','EMBEDDED SYSTEMS'),
#     ('EC308','FIBER OPTIC COMMUNICATION')),
#     4,(('EC401','VLSI DESIGN'),
#     ('EC403','MOBILE COMMUNICATION'),
#     ('EC405','ELECTRONICS INSTRUMENTS'),
#     ('EC402','RF & MICROWAVE ENGINEERING'),
#     ('EC404','ELECTRONICS SYSTEM DESIGN'),
#     ('MH404','INDUSTRIAL MANAGEMENT'))
#    }


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

    

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno=models.CharField(max_length=8)
    year=models.IntegerField(choices=choices_year)
    projects=models.ManyToManyField('Project',blank=True,null=True)

    def __str__(self):
        return self.user.username
