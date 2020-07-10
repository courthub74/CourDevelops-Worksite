from django.shortcuts import render, redirect
from .models import Projects, Deliverables
from .forms import ProjectsForm, DeliverablesForm
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

#DEPLOY TO HEROKU
def django_heroku(request):
	return render(request, "django_heroku.html", {})

######################################################

#FLASK
#Flask Basic Structure
def flaskbasic(request):
	return render(request, "flaskbasic.html", {})

#Flask to Heroku
def flask_heroku(request):
	return render(request, "flask_heroku.html", {})


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

#PROJECTS TODO LIST

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

#DELIVERABLES TODO LIST

#DELIVERABLESentry
def deliverables(request):
	if request.method == 'POST':
		dform = DeliverablesForm(request.POST or None)

		if dform.is_valid():
			dform.save()
			all_delivs = Deliverables.objects.all
			messages.success(request, ("Deliverable Has Been Added To 'Deliverables' List"))
			return render(request, "deliverables.html", {'all_delivs': all_delivs})

	else:
		all_delivs = Deliverables.objects.all
		return render(request, "deliverables.html", {'all_delivs': all_delivs})



#DELIVERABLEScrossoff
def delivs_cross_off(request, list_id):
	delivs = Deliverables.objects.get(pk=list_id)
	delivs.delivscomplete = True
	delivs.save()
	return redirect ('deliverables')

#DELIVERABLESuncross
def delivs_uncross(request, list_id):
	delivs = Deliverables.objects.get(pk=list_id)
	delivs.delivscomplete = False
	delivs.save()
	return redirect ('deliverables')

#DELIVERABLESdelete
def delivs_delete(request, list_id):
	delivs = Deliverables.objects.get(pk=list_id)
	delivs.delete()
	messages.success(request, ('Deliverable Has Been Deleted'))
	return redirect ('deliverables')











	 
	
