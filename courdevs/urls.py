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
	#Clone Django Project
	path('djangoclone/', views.clone_django_proj, name="djangoclone"),
	#Django Database Models
	path('django_database/', views.django_database_models, name="django_database"),
	#Django Context Dictionary
	path('context_dictionary/', views.django_context_dictionary, name="context_dictionary"),
	#Django Heroku
	path('django_heroku/', views.django_heroku, name="django_heroku"),

	#Projects Checklist
	path('projects/', views.projects, name="projects"),
	path('project_cross_off/<list_id>', views.project_cross_off, name="project_cross_off"),
	path('project_uncross/<list_id>', views.project_uncross, name="project_uncross"),
	path('project_delete/<list_id>', views.project_delete, name="project_delete"),

	#Deliverables Checklist
	path('deliverables/', views.deliverables, name="deliverables"),
	path('delivs_cross_off/<list_id>', views.delivs_cross_off, name="delivs_cross_off"),
	path('delivs_uncross/<list_id>', views.delivs_uncross, name="delivs_uncross"),
	path('delivs_delete/<list_id>', views.delivs_delete, name="delivs_delete"),

	#GIT
	#InitializeGit
	path('initializegit/', views.initializegit, name="initializegit"),
	#DeleteGitRepo
	path('deletegitrepo/', views.deletegitrepo, name="deletegitrepo"),
	#PushToHeroku
	path('pushtoheroku/', views.pushtoheroku, name="pushtoheroku"),

]