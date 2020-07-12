from django.shortcuts import render, redirect
from .models import Projects, Deliverables, Practices
from .forms import ProjectsForm, DeliverablesForm, PracticesForm
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

#JAVASCRIPT

#DISABLE FIELDS BY CHECKBOX
def disable_fields(request):
	return render(request, "disable_fields.html", {})


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

#GITIGNORE
def gitignore(request):
	return render(request, "gitignore.html", {})

######################################################

#GITHUB

#INITIALPUSH
def initialgithub(request):
	return render(request, "initialgithub.html", {})

#GITHUB ACTIONS
def github_actions(request):
	return render(request, "github_actions.html", {})

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

#PROJECTSedit
def project_edit(request, list_id):
	if request.method == 'POST':
		pitem = Projects.objects.get(pk=list_id)

		pform = ProjectsForm(request.POST or None, instance=pitem)

		if pform.is_valid():
			pform.save()
			messages.success(request, ('Project Has Been Edited'))
			return redirect ('projects')

	else:
		pitem = Projects.objects.get(pk=list_id)
		return render(request, 'projedit.html', {'pitem': pitem})

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

#DELIVERABLESedit
def delivs_edit(request, list_id):
	if request.method == 'POST':
		ditem = Deliverables.objects.get(pk=list_id)

		dform = DeliverablesForm(request.POST or None, instance=ditem)

		if dform.is_valid():
			dform.save()
			messages.success(request, ('Deliverable Has Been Edited'))
			return redirect ('deliverables')

	else:
		ditem = Deliverables.objects.get(pk=list_id)
		return render(request, 'delivs_edit.html', {'ditem': ditem})
		

########################################################

#PRACTICES

#PRACTICESentry
def practices(request):
	if request.method == 'POST':
		pracform = PracticesForm(request.POST or None)

		if pracform.is_valid():
			pracform.save()
			all_practices = Practices.objects.all
			messages.success(request, ("Practice Has Been Added To 'Practices' List"))
			return render(request, "practices.html", {'all_practices': all_practices})

	else:
		all_practices = Practices.objects.all
		return render(request, "practices.html", {'all_practices': all_practices}) 
	

#PRACTICEScrossoff
def practices_cross_off(request, list_id):
	practices = Practices.objects.get(pk=list_id)
	practices.practicescomplete = True
	practices.save()
	return redirect ('practices')

#PRACTICESuncross
def practices_uncross(request, list_id):
	practices = Practices.objects.get(pk=list_id)
	practices.practicescomplete = False
	practices.save()
	return redirect ('practices')

#PRACTICESdelete
def practices_delete(request, list_id):
	practices = Practices.objects.get(pk=list_id)
	practices.delete()
	messages.success(request, ('Practice Has Been Deleted'))
	return redirect ('practices')

#PRACTICESedit
def practices_edit(request, list_id):
	if request.method == 'POST':
		pracitem = Practices.objects.get(pk=list_id)

		pracform = PracticesForm(request.POST or None)

		if pracform.is_valid():
			pracform.save()
			messages.success(request, ('Practice Has Been Edited'))
			return redirect ('practices')

	else:
		pracitem = Practices.objects.get(pk=list_id)
		return render(request, 'practices_edit.html', {'pracitem': pracitem})











	 
	
