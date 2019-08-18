from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField(max_length=200)
    def __str__(self):
        return f"{self.name}-{self.bio}"

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    timeRequired = models.CharField(max_length=20)
    instructions = models.TextField(max_length=500)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}-{self.description}-{self.timeRequired}-{self.instructions}"

