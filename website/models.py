from django.db import models

# Create your models here.


class Executive(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    post = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    image = models.ImageField(upload_to="images/executives", blank=False)
    about = models.TextField()
    linkedin_url = models.CharField(max_length=100)
    twitter_url = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + " " + self.lastname + " | " + self.post

class Gallery (models.Model):
    image = models.ImageField(upload_to="images/gallery", blank=False)
    caption = models.TextField()

    def __str__ (self):
        return self.caption

class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/events", blank=False)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    details = models.TextField()

    def __str__ (self):
        return self.title + " | " + self.venue