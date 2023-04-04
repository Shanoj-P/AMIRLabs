from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.TextField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='image')

    def get_url(self):
        return reverse('feedsApp:showComment', args=[self.slug])
    def get_url1(self):
        return reverse('feedsApp:addCmt', args=[self.slug])

    def __int__(self):
        return '{}'.format(self.title)

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    cmt = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



    def __int__(self):
        return '{}'.format(self.cmt)
