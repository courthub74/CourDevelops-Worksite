from django.shortcuts import render, redirect
from .models import Projects, Deliverables, Practices, Classes 
from .forms import ProjectsForm, DeliverablesForm, PracticesForm, ClassesForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#LOGIN
def login_user(request):
	# return render(request, "main.html", {})
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You are Logged in as'))
			return redirect('main')
		else:
			messages.success(request, ('Error Logging In - Please Try Again...'))
			return redirect('login_user')
	else:
		return render(request, "login/login.html", {})

#MAIN (STACK)
def main(request):
	return render(request, "main.html", {})

#LOGOUT
def logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out'))
	return redirect('login_user')

#ACCOUNT INFO
def acct_info(request):
	return render(request, "account_info/acct.html", {})

#####################################################

#PYTHON

#TRYEXCEPT
def try_except(request):
	return render(request, "try_except.html", {})

#SELF PARAMETER
def self_param(request):
	return render(request, "python/selfparameter.html", {})

#WEB SCRAPING
def web_scraping_html(request):
	return render(request, "python/webscrapinghtml.html", {})

#FOR LOOP
def for_loop(request):
	return render(request, "python/forloop.html", {})

#WHILE LOOP
def while_loop(request):
	return render(request, "python/whileloop.html", {})

#COUNTER
def counter(request):
	return render(request, "python/counter.html", {})

#CLASSES
def python_classes(request):
	return render(request, "python/classes.html", {})

#CONTROL FLOW
def ctrl_flow(request):
	return render(request, "python/ctrl_flow.html", {})

#FUNCTION WITH PARAMETERS
def functionparams(request):
	return render(request, "python/functionparams.html", {})

# REGEX
def regex(request):
	return render(request, "python/regex.html", {})

# SEND EMAIL
def email(request):
	return render(request, "python/email.html", {})

######################################################

#JAVASCRIPT

#JAVASCRIPT BASICS
def basicsjs(request):
	return render(request, "javascript/basicsjs.html", {})

#DISABLE FIELDS BY CHECKBOX
def disable_fields(request):
	return render(request, "disable_fields.html", {})

#COLOR CODE SELECTION BY RADIODIAL
def color_code(request):
	return render(request, "color_code.html", {})

#SCOPES JS
def scopes_js(request):
	return render(request, "javascript/scopesjs.html", {})

#ARRAYS ACCESSING ELEMENTS
def arrays_elements(request):
	return render(request, "javascript/arrayselements.html", {})

#FUNCTIONS
def functions_js(request):
	return render(request, "javascript/functionsjs.html", {})

#DISSAPEAR ELEMENTS
def dissapear_elements(request):
	return render(request, "javascript/dissapear_elements.html", {})

#SHOW HIDE COLORS
def showhidecolors(request):
	return render(request, "javascript/showhidecolors.html", {})

#FIZZBUZZ
def fizzbuzz(request):
	return render(request, "javascript/fizzbuzz.html", {})

#ALLEN IVERSON
def allen(request):
	return render(request, "javascript/jsalleniverson.html", {})


######################################################

#HTML

#HTMLforms
def html_forms(request):
	return render(request, "html_forms.html", {})

#HTMLtables
def html_tables(request):
	return render(request, "html_tables.html", {})

#HTMLsubmit button
def submit_button(request):
	return render(request, "submit_button.html", {})

#HTMLdropdown
def dropdown(request):
	return render(request, "dropdown.html", {})

#HTMLuser authentication
def user_auth(request):
	return render(request, "user_auth.html", {})

#HTMLnumber box
def numberbox(request):
	return render(request, "numberbox.html", {})

#HTMLslider
def slider(request):
	return render(request, "slider.html", {})

#HTMLradiodial
def radio(request):
	return render(request, "radio.html", {})

#HTMLtextarea
def textarea(request):
	return render(request, "textarea.html", {})

#HTML DEMO
def bobs_burger(request):
	return render(request, "bobs_burger.html", {})

######################################################

#CSS

#CSS Notes
def css_notes(request):
	return render(request, "css_notes.html", {})

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

#API

#API BASICS
def api_basics(request):
	return render(request, "api_basics.html", {})

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


######################################################

#CLASSES TODO LIST

#CLASSESentry
def classes(request):
	if request.method == 'POST':
		classesform = ClassesForm(request.POST or None) #The Entry

		if classesform.is_valid():
			classesform.save()
			all_classes = Classes.objects.all #Iterating through all objects of the Classes model
			messages.success(request, ("Class Has Been Added To 'Classes to Take' List"))
			return render(request, "todolists/classes.html", {'all_classes': all_classes})

	else:
		all_classes = Classes.objects.all
		return render(request, "todolists/classes.html", {'all_classes': all_classes})


#CLASSEScrossoff
def classes_cross_off(request, list_id):
	classes = Classes.objects.get(pk=list_id) #pk if for Primary Key
	classes.classescomplete = True #If the class is complete
	classes.save() #Then save the class
	return redirect ('classes') #Redirect to 'classes' page


#CLASSESuncross
def classes_uncross(request, list_id):
	classes = Classes.objects.get(pk=list_id) #In the classes model you will get the object that is the id of what you clicked on  #pk if for Primary Key
	classes.classescomplete = False # Opposite of cross off # Deems the classescomplete feature off
	classes.save() #Then save that object (in this case the class)
	return redirect ('classes') #Redirect to 'classes' page


#CLASSESdelete
def classes_delete(request, list_id):
	classes = Classes.objects.get(pk=list_id)
	classes.delete()
	messages.success(request, ('Class Has Been Deleted'))
	return redirect ('classes')


#CLASSESedit
def classes_edit(request, list_id):
	if request.method == 'POST':
		classitem = Classes.objects.get(pk=list_id) #The Retrieval 

		classesform = ClassesForm(request.POST or None, instance=classitem) #Create a variable called 'classesform' call it ClassesForm and populate it with whats posted or if nothing then none
		
		if classesform.is_valid():
			classesform.save()
			messages.success(request, ('Classes Has Been Edited'))
			return redirect ('classes')


	else:
		classitem = Classes.objects.get(pk=list_id)
		return render(request, 'todolists/classes_edit.html', {'classitem': classitem})
















	 
	
