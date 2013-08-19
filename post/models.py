from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class mCategories (models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=240)

    def __unicode__(self):
        return u'%s' % self.name


class mComment(models.Model):
    username = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    title = models.CharField(max_length=180)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    validation_key = models.CharField(max_length=24)
    validation = models.BooleanField(default=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = generic.GenericForeignKey('Content_type', 'Object_id')

    def __unicode__(self):
        return u'Comment: %s' % self.title

    def get_sub(self):
        return mComment.objects.filter(object_id=self.id,
                                       content_type=ContentType.objects.get_for_model(self))


class mPost(models.Model):
    user = models.ForeignKey(User)
    cat = models.ForeignKey(mCategories)
    title = models.CharField(max_length=240)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    comments = generic.GenericRelation(mComment)

    def __unicode__(self):
        return self.title