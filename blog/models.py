from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)          #for the title of anything, how many words it should be of
    description = models.TextField()    #for the description of any title of how many words it should be of
    date = models.DateField()

    def __str__(self):
        return self.title
