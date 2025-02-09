from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("account.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("projects/", include("project.urls")),
    path("",TemplateView.as_view(template_name="home.html"), name="home"),

]
