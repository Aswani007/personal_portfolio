from django.urls import path
from . import views   # '.' because views is in this blog only

app_name = 'blog'

urlpatterns = [

    path('', views.all_blogs, name='all_blogs'),  #in here the url already has blog in it
    path('<int:blog_id>/', views.detail, name='detail'),

]
