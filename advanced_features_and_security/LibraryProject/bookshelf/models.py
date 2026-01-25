
from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    '''Custom user manager that supports extra fields'''
    
    def create_user(self, username, email = None, password = None,**extra_fields):
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email = None, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")      
        
        return self.create_user(username, email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    '''Custom user model extending AbstractUser'''
    
    date_of_birth = models.DateField(
        _("date of birth"),
        null=True,
        blank=True
    )
    
    profile_photo = models.ImageField(
        upload_to= "profile_photos/",
        null=True,
        blank=True
    )

    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    

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
    

# class Article(models.Model):
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )
    
    # title = models.CharField(max_length=255)
  