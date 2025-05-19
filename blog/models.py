from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name="posts")
    excerpt = models.TextField()
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
