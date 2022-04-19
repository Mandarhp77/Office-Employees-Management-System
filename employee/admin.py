from django.contrib import admin

# Register your models here.
from .models import role, education, employee

admin.site.register(role)
admin.site.register(education)
admin.site.register(employee)