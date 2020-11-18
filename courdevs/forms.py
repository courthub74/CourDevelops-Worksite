from django import forms
from .models import Projects, Deliverables, Practices, Classes

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Projects
		fields = ["projects", "projectscomplete"]

class DeliverablesForm(forms.ModelForm):
	class Meta:
		model = Deliverables
		fields = ["delivs", "delivscomplete"]

class PracticesForm(forms.ModelForm):
	class Meta:
		model = Practices
		fields = ["practices", "practicescomplete"]

class ClassesForm(forms.ModelForm):
	class Meta:
		model = Classes 
		fields = ["classes", "classescomplete"]