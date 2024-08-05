from django.views import View
from project.forms import ProjectCreateForm
from django.shortcuts import render
class CreateProject(View):
    def get(self, request):
        return render(request, 'project/create_project.html', context={'form': ProjectCreateForm()})

    def post(self, request):
        pass

