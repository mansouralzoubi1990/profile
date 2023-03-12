from django.urls import path
from .views import index,blog,blogList

urlpatterns = [
    path('',index,name='home'),
    path('blog/<int:blog_id>',blog,name='blog'),
    path('blogs/',blogList,name='blogs'),

]