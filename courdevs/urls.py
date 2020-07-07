from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='main'),

	#PYTHON
	#Try Except
	path('try_except/', views.try_except, name="try_except"),

	#DJANGO
	#Django Notes
	path('setupdjango/', views.setupdjango, name="setupdjango"),
	#MVC Notes
	path('mvcbasics/', views.mvcbasics, name="mvcbasics"),

	#Projects Checklist
	path('projects/', views.projects, name="projects"),
	path('project_cross_off/<list_id>', views.project_cross_off, name="project_cross_off"),
	path('project_uncross/<list_id>', views.project_uncross, name="project_uncross"),
	path('project_delete/<list_id>', views.project_delete, name="project_delete"),


	#GIT
	#InitializeGit
	path('initializegit/', views.initializegit, name="initializegit"),

]