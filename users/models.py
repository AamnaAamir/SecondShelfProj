from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import os

# helper function to extract file name and extension from a given file path
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# defines where and how profile pictures will be stored
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    # profile picture will be saved as: users/<user_id>-<username>.<ext>
    final_name = f"{instance.id}-{instance.user.username}{ext}"
    return f"users/{final_name}"

# creates database table users_user_profile
class user_profile(models.Model):
   # connects profile to Django’s built-in User model (One-to-One relationship)
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

  city = models.CharField(max_length=100, blank=True, null=True)
  address = models.CharField(max_length=500, blank=True, null=True)
  gender = models.CharField(max_length=10,default='Female')
  phone_num = models.CharField(max_length=15, blank=True, null=True)
  whatsapp_num = models.CharField(max_length=15, blank=True, null=True)

  # profile picture upload field (saved using upload_image_path)
  #profile_pic = models.ImageField(default='default.jpg', upload_to=upload_image_path)
  profile_pic = models.ImageField(default='default.jpg',upload_to=upload_image_path,blank=True,null=True
)
  # return username as readable name in admin or print()
  def __str__(self):
    return str(self.user.username)

