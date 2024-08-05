from django.urls import path
from project.controllers.project import ProjectView
from project.controllers.create_project import CreateProject

urlpatterns = [
    path('create/', CreateProject.as_view(), name='project_create'),
    path('', ProjectView.as_view(), name='project'),
]

