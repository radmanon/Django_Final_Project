from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile"),
    path('profile view just/', profile_view_just, name="profile_view_just"),
    path('signup/', signup_view, name="signup")
]



urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)