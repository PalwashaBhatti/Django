from asyncio.windows_events import NULL
from random import choices
import string
from tokenize import Name

from django.db import models
from traitlets import default
from django.utils.timezone import now
        
class ModelName(models.Model):
        field_name = models.Field(**options)


class Employees(models.Model):
    Name = models.CharField(max_length=30)
    Website = models.CharField(max_length=30)
    Point_of_contact = models.EmailField(max_length=20)
    profile_picture = models.ImageField()
    Goal= models.Choices()
    due_date = models.DateField()
    Date_joined = models.DateField(auto_now_add=True)

# specifying choices
  
GOAL_CHOICES = (
    ("CPA", "CPA"),
    ("IMPRESSIONS", "IMPRESSIONS"),
    ("DOWNLOADS", "DOWNLOADS"),
    ("INSTALLS", "INSTALLS"),
    ("PURCHASE", "PURCHASE"),
)
   CREATE TABLE "myapp_SmallClient"
   (
   "name" string(30) NOT NULL PRIMARY KEY AUTOINCREMENT, 
   "website" string(30), 
   "Point_of_contact" string(30) NOT NULL, 
   "profile_picture" NOT NULL, 
   "goal"(30) choices = GOAL_CHOICES, default='CPA',
    "due_date" date NOT NULL, 
    "date_joined" DateTime,
 
);
   due_date.objects.filter(
    due_date_time__date=now().date()
)
COMMIT;