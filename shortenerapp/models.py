from django.db import models
import random


# Create your models here.
class Urls(models.Model):
    short_id = models.SlugField(max_length=6,primary_key=True)
    httpurl = models.URLField(max_length=200, null = True)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
 
    def __str__(self):
        return self.httpurl

    def save_url(self):
        '''
        Method that saves Urls objects
        '''
        self.save()

    @classmethod
    def count_unique(cls,httpurl):
        all = cls.objects.filter(httpurl = httpurl).count()
        return all

    def code_generator(size = 6 , char = '1234567890afuhufxrkerwcklbvds' ):
        new_code = ''
        for i in range(size):
            new_code += random.choice(char)
        return new_code
    
