from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(User):
    image = models.ImageField(upload_to = 'photo/', default = 'photo/None/no-img.jpg')
    phone = models.CharField(max_length=10,blank=True, verbose_name='Phone Number:')
    job = models.CharField(max_length=40,blank=True,verbose_name='Job :')
    def __unicode__(self):
        return '%s , %s %s - %s' %(self.username, self.first_name, self.last_name, self.email)

