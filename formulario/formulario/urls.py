from django.contrib import admin
from django.urls import path, include
#PROJETO
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form.urls')),
]
