from django.urls import path
from . import views

urlpatterns = [
	
	#DEVELOPMENT STACK PAGE
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

	#FLASK
	#Flask Basic Structure
	path('flaskbasic/', views.flaskbasic, name="flaskbasic"),
	#Flask Heroku
	path('flask_heroku/', views.flask_heroku, name="flask_heroku"),

	#Projects Checklist
	path('projects/', views.projects, name="projects"),
	path('project_cross_off/<list_id>', views.project_cross_off, name="project_cross_off"),
	path('project_uncross/<list_id>', views.project_uncross, name="project_uncross"),
	path('project_delete/<list_id>', views.project_delete, name="project_delete"),
	path('project_edit/<list_id>', views.project_edit, name="project_edit"),


	#Deliverables Checklist
	path('deliverables/', views.deliverables, name="deliverables"),
	path('delivs_cross_off/<list_id>', views.delivs_cross_off, name="delivs_cross_off"),
	path('delivs_uncross/<list_id>', views.delivs_uncross, name="delivs_uncross"),
	path('delivs_delete/<list_id>', views.delivs_delete, name="delivs_delete"),

	#Practices Checklist
	path('practices/', views.practices, name="practices"),
	path('practices_cross_off/<list_id>', views.practices_cross_off, name="practices_cross_off"),
	path('practices_uncross/<list_id>', views.practices_uncross, name="practices_uncross"),
	path('practices_delete/<list_id>', views.practices_delete, name="practices_delete"),

	#GIT
	#InitializeGit
	path('initializegit/', views.initializegit, name="initializegit"),
	#DeleteGitRepo
	path('deletegitrepo/', views.deletegitrepo, name="deletegitrepo"),
	#PushToHeroku
	path('pushtoheroku/', views.pushtoheroku, name="pushtoheroku"),

]