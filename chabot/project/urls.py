
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate_text/', views.generate_text, name='generate_text')
]



