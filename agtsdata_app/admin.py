


from django.contrib import admin
from .models import Service, Projet, MembreEquipe, MessageContact

admin.site.register(Projet)
admin.site.register(MembreEquipe)
admin.site.register(MessageContact)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ordre_affichage', 'icone')
    list_editable = ('ordre_affichage',)
    search_fields = ('nom',)
