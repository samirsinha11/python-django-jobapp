from django.db import models
from django.utils.text import slugify
# Create your models here.

class Skill(models.Model):
    name =models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)

class Location (models.Model):
    street = models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)

class JobPost(models.Model):
    JOB_TYPE = [('Full Time', 'Full Time'), ('Part Time', 'Part Time'),]
    title = models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    salary=models.IntegerField()
    expiry=models.DateField(null=True)
    slug=models.SlugField(null=True, unique=True, max_length=45)
    location=models.OneToOneField(Location,on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE, null=True)
    skill = models.ManyToManyField(Skill)
    type = models.CharField(max_length=100, null=False, choices=JOB_TYPE)

    def save (self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
