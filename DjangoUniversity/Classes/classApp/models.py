from django.db import models

# Create your models here.


# django class creation
class djangoClasses(models.Model):
    title = models.CharField(max_length=90)
    courseNumber = models.IntegerField(default=0)
    instructorName = models.CharField(max_length=90)
    duration = models.FloatField(default=0.00)


    objects = models.Manager()

    def __str__(self):
        return self.title



# object attribute values
classOne = djangoClasses(title="Health", courseNumber=101, instructorName="Hannah Boyle", duration=1.0)
classTwo = djangoClasses(title="Calculus", courseNumber=141, instructorName="Robert Mass", duration=1.5)
classThree = djangoClasses(title="Biology", courseNumber=222, instructorName="Russell Peterson", duration=2.0)