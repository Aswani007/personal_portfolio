from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)          #for the title of anything, how many words it should be of
    description = models.CharField(max_length=250)    #for the description of any title of how many words it should be of
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


    def __str__(self):                      #from thid function we will be able to see the project names and blogs names
        return self.title                   #  in the admin page
