from django.db import models
from django.urls import  reverse
from django.template.defaultfilters import slugify




# Create your models here.

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


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
    
    

    class Meta:
        ordering=('-title',)
   
    
    slug = models.SlugField(max_length=255, unique=True)
    class Meta:
        ordering=('-title',)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Story, self).save(*args, **kwargs)
