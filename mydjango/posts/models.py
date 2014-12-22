from django.db import models
from djangotoolbox.fields import ListField


class blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    #tags = ListField()
    pub_date = models.DateTimeField('date published')
    comments = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(blog)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Meta:
    ordering = ['-pub_date']


def __unicode__(self):
    return u'%s' % self.title


# Create your models here.
