from django.contrib import admin
from .models import Projects, Deliverables, Practices

# Register your models here.
admin.site.register(Projects)
admin.site.register(Deliverables)
admin.site.register(Practices)
