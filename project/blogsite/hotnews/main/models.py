from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=15)


    def __str__(self):
        return self.title



class Form(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='phtos/%Y/%m/%d/')
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title