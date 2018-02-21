from django.contrib import admin
from .models import Plant, Familia, Genus, Metabolite, Distribution,TherapeuticEffects

admin.site.register(Plant)
admin.site.register(Familia)
admin.site.register(Genus)
admin.site.register(Metabolite)
admin.site.register(Distribution)
admin.site.register(TherapeuticEffects)
