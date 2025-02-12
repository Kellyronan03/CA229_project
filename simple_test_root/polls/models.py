from django.db import models
import datetime
from django.utils import timezone


# Question model representing a poll question with text and publication date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice model representing an option for a poll question with text and vote count
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Page model representing a webpage with title, content, and timestamps
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField("Last Updated")
    create_date = models.DateField("First Published", default=datetime.date.today)
    bodytext = models.TextField("Page Content", blank=True)

    def __str__(self):
        return self.title # String representation of the Page object, returns its title