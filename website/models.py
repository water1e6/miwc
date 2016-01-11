from django.db import models
from django.utils import timezone
import datetime




class PageType(models.Model):
    Type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.Type

class PageCopyType(models.Model):
    Type = models.CharField(max_length=200)
 
    def __unicode__(self):
        return self.Type
 
 
class PageCopy(models.Model):
    Text = models.TextField()
    Label = models.CharField(max_length=200)
    Type = models.ForeignKey(PageCopyType)
 
    def __unicode__(self):
        return self.Text
 
class WebContent(models.Model): 
    Label = models.CharField(max_length=200)
    Value = models.ForeignKey(PageCopy, related_name='+')
    Location = models.CharField(max_length=200)
    Order = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.Label     

class WebContentSection(models.Model):
    Label = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Content = models.ManyToManyField(WebContent)
    Order = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.Label
    
class WebPage(models.Model):
    Key = models.CharField(max_length=200)
    Url = models.CharField(max_length=200)
    Title = models.ForeignKey(PageCopy, related_name='+')
    Type = models.ForeignKey(PageType, related_name='+')
    Headline = models.ForeignKey(PageCopy, related_name='+')
    TopImage = models.ForeignKey(PageCopy, related_name='+', null=True)
    BottomImage = models.ForeignKey(PageCopy, related_name='+', null=True)
    NullField = models.CharField(max_length=200, null=True)
    ContentSections = models.ManyToManyField(WebContentSection)

    def __unicode__(self):
        return self.Key