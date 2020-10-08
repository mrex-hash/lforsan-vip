from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name





class Post(models.Model):
    
    auteur = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=50, null=True)
    subtitle = models.CharField(max_length=50, null=True)
    contenu = models.TextField(max_length=900, null=True)
    image = models.ImageField(null =True, blank =True, upload_to = "images", default ="placeholder.png")
    data_creates = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)


    def __str__(self):
        return self.title