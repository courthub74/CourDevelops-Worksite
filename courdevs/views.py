from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectsForm
from django.contrib import messages

# Create your views here.

#MAIN
def main(request):
	return render(request, "main.html", {})

#####################################################

#PYTHON

#TRYEXCEPT
def try_except(request):
	return render(request, "try_except.html", {})


######################################################

#DJANGO

#DJANGOSETUP 
def setupdjango(request):
	return render(request, "setupdjango.html", {})

#MVC BASICS
def mvcbasics(request):
	return render(request, "mvcbasics.html", {})

#CLONE PROJECT
def clone_django_proj(request):
	return render(request, "djangoclone.html", {})

#DJANGO DATABASE
def django_database_models(request):
	return render(request, "django_database.html", {})

#DJANGO CONTEXT DICTIONARY
def django_context_dictionary(request):
	return render(request, "django_dictionary.html", {})

######################################################

#GIT

#INITIALIZEGIT
def initializegit(request):
	return render(request, "initializegit.html", {})

#DELETEGITREPO
def deletegitrepo(request):
	return render(request, "deletegitrepo.html", {})

#PUSHTOHEROKU
def pushtoheroku(request):
	return render(request, "pushtoheroku.html", {})

######################################################

#PROJECTSentry
def projects(request):
	if request.method == 'POST':
		pform = ProjectsForm(request.POST or None)

		if pform.is_valid():
			pform.save()
			all_projects = Projects.objects.all
			messages.success(request, ("Project Has Been Added To 'Projects' List"))
			return render(request, "projects.html", {'all_projects': all_projects})

	else:
		all_projects = Projects.objects.all
		return render(request, "projects.html", {'all_projects': all_projects})

#PROJECTScrossoff
def project_cross_off(request, list_id):
	projects = Projects.objects.get(pk=list_id)
	projects.projectscomplete = True
	projects.save()
	return redirect ('projects')

#PROJECTSuncross
def project_uncross(request, list_id):
	projects = Projects.objects.get(pk=list_id)
	projects.projectscomplete = False
	projects.save()
	return redirect ('projects')

#PROJECTSdelete
def project_delete(request, list_id):
	projects = Projects.objects.get(pk=list_id)
	projects.delete()
	messages.success(request, ('Project Has Been Deleted'))
	return redirect ('projects')

######################################################









	 
	
