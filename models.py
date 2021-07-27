from django.db import models
from django.urls import  reverse
from django.template.defaultfilters import slugify




# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('story:story_by_category', args=[self.slug])

class Story(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)
    answer3 = models.CharField(max_length=200)
    answer4 = models.CharField(max_length=200)
    correct = models.CharField(max_length=200)
    publish=models.DateTimeField(auto_now_add=True)
    
    def slug(self):
        return slugify(self.title)
    class Meta:
        ordering=('-title',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('story:story_detail', kwargs={'slug': self.title})

