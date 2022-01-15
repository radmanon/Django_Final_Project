from django.db import models
from django.contrib.auth.models import User
# Create your models here.



MALE = "m"
FEMALE = "f"
OTHER = "سایر"
PROFILE_GENDER_CHOICES = [
    (MALE, "آقا"),
    (FEMALE, "خانم"),
    (OTHER, "سایر")
]



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="profile")
    membership_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveSmallIntegerField(verbose_name="سن")
    nc = models.CharField(verbose_name="کد ملی", max_length=10)
    phone_number = models.CharField(verbose_name="شماره موبایل", max_length=11)
    bio = models.TextField(verbose_name="معرفی",null=True, blank=True)
    gender = models.CharField(verbose_name="جنسیت",max_length=4, choices=PROFILE_GENDER_CHOICES)
    is_author = models.BooleanField(verbose_name="آیا نویسنده است", default=False)
    upload_resume = models.FileField(verbose_name="فایل رزومه")
    







