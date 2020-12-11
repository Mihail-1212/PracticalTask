from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('webdiary.urls'), name='webdiary'),
    path('authorization/', include('authorization.urls')),
    path('admin/', admin.site.urls),
]
