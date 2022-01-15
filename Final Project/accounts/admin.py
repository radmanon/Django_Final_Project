from django.contrib import admin
from accounts.models import Profile
from blog.admin import CommentInLine, PostInLine

# Register your models here.





@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("first_name", "last_name", "user", "nc","phone_number","gender","date_employment")
    list_filter = ("gender","date_employment")
    search_fields = ("user", "first_name", "last_name", "phone_number", "nc")
    ordering = ("age",)
    sortable_by = ("first_name", "last_name", "date_employment")
    list_editable = ("phone_number", "nc", "gender")
    inlines = [PostInLine, CommentInLine]