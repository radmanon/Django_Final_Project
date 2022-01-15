



from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.core import validators
from django.db import models
from django.db.models.aggregates import Avg

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.urls.base import reverse

# Create your models here.


def limit_file_size(value):
    if value.size > 10485760:
        raise ValidationError("عکس عکس باید کمتر از 10 مگابایت باشد.")


MALE ='m'
FEMALE = 'f'
PROFILE_GENDER_CHOICES = [
    (MALE, "آقا"),
    (FEMALE, "خانم")
]



YES ='m'
NO = 'f'
PROFILE_AUTHOR_CHOICES = [
    (YES, "بله"),
    (NO, "خیر")
]





class Profile(models.Model):
    slug = models.SlugField(verbose_name="پیوند یکتا", null=True, blank=True, allow_unicode=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="profile")
    bio = models.TextField(verbose_name="درباره ی من", null=True, blank=True, help_text="توضیحات فردی")
    first_name = models.CharField(max_length=50, verbose_name="نام", null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی", null=True, blank=True)
    phone_number = models.CharField(max_length=11 ,verbose_name="شماره همراه", null=True, blank=True, help_text="11 رقم وارد کنید")
    age = models.CharField(max_length=2, verbose_name="سن", help_text="2رقم وارد کنید", null=True, blank=True)
    job = models.CharField(max_length=50, verbose_name="سمت شغلی", blank=True)
    date_employment = models.DateTimeField(auto_now_add=True)
    date_user_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(verbose_name="عکس رزومه", upload_to="media/resume/", null=True, blank=True)
    gender = models.CharField(verbose_name="جنسیت", max_length=1, choices=PROFILE_GENDER_CHOICES, null=True, blank=True)
    nc = models.CharField(verbose_name="کدملی", max_length=11, null=True, blank=True) #nationalcode
    email = models.CharField(verbose_name="ایمیل", max_length=100, null=True, blank=True)
    is_author = models.CharField(verbose_name="آیا نویسنده هستید", max_length=1, choices=PROFILE_AUTHOR_CHOICES, default="خیر")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user, allow_unicode=True)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


    class Meta():
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"



    def get_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" alt="{self.first_name}" width="100" height="100">')
        else:
            return mark_safe(f'<img src="/media/posts-image/No-Image-Placeholder.svg.png" alt="NO IMAGE" width="100" height="100">')
    
    get_image.short_description = "image"


class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField()

