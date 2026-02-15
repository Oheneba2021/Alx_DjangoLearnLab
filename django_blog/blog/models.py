from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE )
    
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