from django.contrib import admin

# Register your models here.

from escuela.models  import *


admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(Post)