
from django.db import models


# #Create a new user 
# user = User.objects.create_user('john', 'john@example.com', 'password123')

# # Retrieve a user based on username
# user = User.objects.get(username='john')

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
    