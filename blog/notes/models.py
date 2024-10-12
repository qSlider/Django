from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    content = models.TextField()
    number_of_likes = models.IntegerField(default=0)
    author = models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    class Meta:
        pass
    def __str__(self):
        return self.title

class Author(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    number_of_posts = models.IntegerField(default=0)
    class Meta:
        pass
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title