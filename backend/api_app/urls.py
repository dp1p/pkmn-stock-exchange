from django.urls import path, include
from .views import Noun_Project
#http:localhost:8000/api/v1/noun
urlpatterns = [
    path('<str:name>/', Noun_Project.as_view(), name="noun_project")
]