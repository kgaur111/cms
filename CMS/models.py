import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
# from datetime import datetime
# from django.db import models

# # Create your models here.
class User(models.Model):
    Id= models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(unique=True)
    Password= models.CharField(max_length=100)
    Contact_Details = models.TextField(max_length=200)
    
class Blog(models.Model):
    Id= models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 250)
    Description = models.TextField()
    Content= models.TextField()
    Created_On = models.DateTimeField(auto_now_add=True)
    Updated_On = models.DateTimeField(default=None, null=True)
    is_public = models.BooleanField(default=True)  # Add the is_public field here
    Author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def save(self, *args, **kwargs):
        if self.pk:
           # This is a new object, set Created_On
           self.Updated_On = timezone.now()

        # Always update Updated_On to the current date and time when saving
        

        super(Blog, self).save(*args, **kwargs)


class Like(models.Model):
    Id = models.AutoField(primary_key=True)
    Post_Id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    User_Id = models.ForeignKey(User,on_delete=models.CASCADE)
    Liked_On = models.DateTimeField(default=datetime.datetime.now())


