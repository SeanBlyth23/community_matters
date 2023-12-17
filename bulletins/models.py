from django.db import models
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(("Bulletin Category"), max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    
class Bulletin(TimeStampMixin):
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='bulletin_user')
    category = models.ForeignKey(Category, on_delete= models.CASCADE,related_name='bulletin_category')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]

