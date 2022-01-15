


from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/<str:slug>/', views.blog_details, name="details"),
]


# Development
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)