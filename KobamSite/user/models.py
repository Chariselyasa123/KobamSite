from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import gettext_lazy as _
# Create your models here.

GENDER_CHOICES=(
    ("M", "MALE"),
    ("FM", "FEMALE"),
)


class User(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender=models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=1,
    )



    def __str__(self):
        return f'{self.user.username} Profile'


    