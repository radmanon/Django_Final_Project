
from django.db import models

from accounts.models import Profile

# Create your models here.


DRAFT = "d"
PUBLISHING = "p"
DISAPPROVAL = "da"
POST_STATUS_CHOICES = [
    (DRAFT, "پیش نویس"),
    (PUBLISHING, "در حال انتشار"),
    (DISAPPROVAL, "عدم تایید")
]


SCIENCE = "s"
EDUCATIONAL = "e"
NEWS = "n"
POST_CATEGORY_CHOICES = [
    (SCIENCE, "علمی"),
    (EDUCATIONAL, "آموزشی"),
    (NEWS, "خبری")
]


PENDDING = "p"
ACCEPTED = "a"
REJECTED = "r"
COMMENT_STATUS_CHOICES = [
    (PENDDING, "در حال بررسی"),
    (ACCEPTED, "مورد قبول"),
    (REJECTED, "عدم تایید")
]


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete= models.SET_NULL, related_name="post", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(verbose_name="عنوان", max_length=50)
    image = models.ImageField(verbose_name="عکس", upload_to="posts-image/")
    description = models.TextField(verbose_name="توضیحات خلاصه", max_length=300)
    status = models.PositiveSmallIntegerField(verbose_name="وضعیت", choices=POST_STATUS_CHOICES)
    category = models.SmallIntegerField(verbose_name="دسته بندی", choices=POST_CATEGORY_CHOICES)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="پست", related_name="comment")
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="کاربر", related_name="comment", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="متن دیدگاه")
    status = models.CharField(max_length=1, verbose_name="وضعیت", choices=COMMENT_STATUS_CHOICES)

