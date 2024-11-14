from django.db import models

from django.utils import timezone

# Create your models here.
# Events Model
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    location = models.CharField(max_length=200)

    class Meta:
        ordering = ['date', 'time']  # Order events by date and time by default

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time}"


# Partnerships Model
class Opportunity(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.TextField()
    job_description = models.TextField()
    qualifications = models.TextField()
    contact_details = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['job_title', 'date_posted']  # Order opportunities by job title and date posted by default

    def __str__(self):
        return self.job_title



# News
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    class Meta:
        ordering = ['title', 'date_posted']

    def __str__(self):
        return self.title

# Commercial Shop
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name