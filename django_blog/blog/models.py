from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE )
    tags= models.ManyToManyField(Tag, blank=True, related_name= "posts")
    
    class Meta:
        ordering= ["-pusblished_date"]
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # After create/update, Django can redirect here
        return reverse("post-detail", kwargs={"pk": self.pk})
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True)
    
    
    def __str__(self):
        return f"{self.username}'s Profile"
    
class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title[:30]}"

    def get_absolute_url(self):
        # After editing, go back to the post detail page
        return reverse("post-detail", kwargs={"pk": self.post.pk})