from django.db import models
from django.utils import timezone
import datetime

class PageCategory(models.Model):
    CategoryName = models.CharField(max_length=200)

    def __unicode__(self):
        return self.CategoryName


class WebPage(models.Model):
    PageTitle = models.CharField(max_length=500)
    PageCategory = models.ForeignKey(PageCategory)

    def __unicode__(self):
        return self.PageTitle

#class Poll(models.Model):
#    question = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    def was_published_recently(self):
#        return (self.pub_date >= timezone.now() - datetime.timedelta(days=1)) and (self.pub_date <= timezone.now()) 
#    was_published_recently.short_description = 'Published in the _recent_ past?'
#    def __unicode__(self):
#        return self.question
#
#class Choice(models.Model):
#    poll = models.ForeignKey(Poll)
#    choice = models.CharField(max_length=200)
#    votes = models.IntegerField()
#    def __unicode__(self):
#        return self.choice