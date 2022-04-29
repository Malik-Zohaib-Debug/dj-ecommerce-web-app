from shutil import RegistryError
from django.contrib import admin
from djangoecommerce.models import RegisteredUser

# Register your models here.
admin.site.register(RegisteredUser)