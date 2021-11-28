from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class User(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = "user"


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.name}"

    class Meta:
        db_table = "category"


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    editor_text = models.TextField()
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)

    def __str__(self):
        return f"{self.id}-{self.title} by {self.user}"

    class Meta:
        db_table = "post"


class Tag(models.Model):
    # posts = models.ManyToManyField(Post, related_name="tags", blank=True)
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = "tag"