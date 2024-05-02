from django.contrib import admin
from .models import Vehicle,get_data
# Register your models here.
admin.site.register(Vehicle)

# get_data('https://verificacionvehicular.puebla.gob.mx/Citas/ExpedientePublico?clave=%2bPwWwL%2b28DQxECy2JvxnHg%3d%3d')
