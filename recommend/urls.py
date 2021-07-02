from django.urls import path
from .views import *
urlpatterns = [
    path('recommend/',recommend, name="recommend"),
    path('recommend1/',recommend1, name="recommend1"),
    path('recommend2/',recommend2, name="recommend2"),
    path('recommend3/',recommend3, name="recommend3"),
    path('recommend4/',recommend4, name="recommend4"),
    path('recommend5/',recommend5, name="recommend5"),
    path('recommend6/',recommend6, name="recommend6"),
    path('recommend7/',recommend7, name="recommend7"),
    path('recommend8/',recommend8, name="recommend8"),
    path('recommend9/',recommend9, name="recommend9"),
    path('recommend10/',recommend10, name="recommend10"),
    path('recommend11/',recommend11, name="recommend11"),
    path('like/',like, name="like"),

]