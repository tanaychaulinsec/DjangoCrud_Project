from django.contrib import admin
from .models import Employee
from .forms import EmployeeForm

# Register your models here.
admin.site.register(Employee)
