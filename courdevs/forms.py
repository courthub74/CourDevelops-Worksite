from django import forms
from .models import Projects, Deliverables

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Projects
		fields = ["projects", "projectscomplete"]


class DeliverablesForm(forms.ModelForm):
	class Meta:
		model = Deliverables
		fields = ["delivs", "delivscomplete"]