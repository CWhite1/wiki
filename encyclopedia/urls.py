from django.urls import path, re_path

from . import views

urlpatterns = [
   
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path('randoms', views.randoms, name="randoms"),
    path('edit/<str:name>/', views.edit, name="edit"),
    path('wiki/<str:name>/', views.title, name='entry')
]

# path('<str:page_title>', views.title, name="page_title")
# declare apps with 
# app_name = "encyclopedia"
# urlpatterns = [
#    path("", views.index, name="index")
# ]
#  path('<str:name>', views.title, name="name")