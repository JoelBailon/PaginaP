from django.contrib import admin
from TransPorto.models import Usuarios
from TransPorto.models import Informes
from TransPorto.models import CooperativaTransporte
from TransPorto.models import Conductores
from TransPorto.models import RegistroAcceso
from TransPorto.models import Rutas
from TransPorto.models import PersonalAdministrativo
from TransPorto.models import UnidadTransporte
from TransPorto.models import HistorialTransacciones
from TransPorto.models import Tarjeta

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Informes)
admin.site.register(CooperativaTransporte)
admin.site.register(Conductores)
admin.site.register(RegistroAcceso)
admin.site.register(Rutas)
admin.site.register(PersonalAdministrativo)
admin.site.register(UnidadTransporte)
admin.site.register(HistorialTransacciones)
admin.site.register(Tarjeta)