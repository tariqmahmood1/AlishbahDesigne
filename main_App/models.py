from django.db import models

# Create your models here.

class Design(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='designs/')
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    is_banner = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class About_page(models.Model):
    title = models.CharField(max_length=100)
    vision = models.TextField()
    Experience = models.TextField()
    descriptions = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Bootstrap icon name e.g. bi-star")

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Replied', 'Replied'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

    