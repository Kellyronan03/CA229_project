from django.db import models
import datetime

# Page model representing a webpage with title, content, and timestamps
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    create_date = models.DateField('First Published', default = datetime.date.today)
    bodytext = models.TextField('Page Content', blank=True)


    def __str__(self):
        return self.title # String representation of the Page object, returns its title
