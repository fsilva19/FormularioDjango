from django.urls import path
from . import views
#APLICATIVO
urlpatterns = [
    path('',views.formBase, name='formulario_principal'),
]