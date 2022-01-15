
from django.db import models

from accounts.models import Profile
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls.base import reverse
# Create your models here.


DRAFT = "1"
PUBLISHING = "2"
DISAPPROVAL = "0"
POST_STATUS_CHOICES = [
    (DRAFT, "پیش نویس"),
    (PUBLISHING, "در حال انتشار"),
    (DISAPPROVAL, "عدم تایید")
]


SCIENCE = "1"
EDUCATIONAL = "2"
NEWS = "0"
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
    slug = models.SlugField(verbose_name="پیوند یکتا", null=True, blank=True, allow_unicode=True)
    author = models.ForeignKey(Profile, on_delete= models.SET_NULL, related_name="post", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(verbose_name="عنوان", max_length=50)
    image = models.ImageField(verbose_name="عکس", upload_to="media/posts-image/")
    short_description = models.TextField(verbose_name="توضیحات خلاصه", max_length=300)
    long_description = RichTextField(verbose_name="توضیحات", max_length=5000, null=True)
    status = models.CharField(verbose_name="وضعیت", choices=POST_STATUS_CHOICES, max_length=1, default=1)
    category = models.CharField(verbose_name="دسته بندی", choices=POST_CATEGORY_CHOICES, max_length=1, default=1)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


    class Meta():
        verbose_name = "پست"
        verbose_name_plural = "پست ها"


    def get_accepted_comments_count(self):
        return self.comment.filter(status="a").count()


    def get_absolute_url(self):
        return reverse('blog:details', kwargs={"slug":self.slug})


    def __str__(self):
        return self.title
    
    def copy():
        return Post(created_at = models.DateTimeField(auto_now=True))

    def get_date(self):
        return self.created_at.strftime('in time: %H:%m:%S - in date: %y/%m/%d')

    get_date.short_description = "date"

    def get_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" alt="{self.title}" width="100" height="100">')
        else:
            return mark_safe(f'<img src="/media/posts-image/No-Image-Placeholder.svg.png" alt="NO IMAGE" width="100" height="100">')
    
    get_image.short_description = "image"




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="پست", related_name="comment")
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="کاربر", related_name="comment", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="متن دیدگاه")
    status = models.CharField(max_length=1, verbose_name="وضعیت", choices=COMMENT_STATUS_CHOICES)
    
    def __str__(self):
        return self.text + " (-) " + self.post.title


    class Meta():
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"
