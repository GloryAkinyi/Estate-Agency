from django.contrib import admin
from django.urls import path
from Estateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('single/', views.single,name='single'),
    path('grid/', views.grid,name='grid'),
    path('bloggrid/', views.bloggrid,name='bloggrid'),
    path('blogsingle/', views.blogsingle,name='blogsingle'),
    path('blogsingle/', views.blogsingle,name='blogsingle'),
    path('contact/', views.contact,name='contact'),
    path('propertygrid/', views.propertygrid,name='propertygrid'),
    path('propertysingle/', views.propertysingle,name='propertysingle'),
]
