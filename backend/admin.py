# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from  .models import *
# Register your models here.


class SonInLine(admin.TabularInline):
    model = Son
    extra = 1


class ProjetInLine(admin.TabularInline):
    model = Projet
    extra = 1



class ArtisteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['pseudo']}),
        ('Autres infos', {'fields': ['label', 'photo', 'email', 'num_tel', 'pays', 'nom', 'prenom', 'id_moderateur'], 'classes': ['collapse']}),

    ]
    inlines = [ProjetInLine]
    search_fields = ['id_artist','pseudo','pays','nom','prenom','label']
    list_display = ['id_artist','pseudo','photo','pays','email','num_tel','label','nom','prenom']
    list_filter = ['id_artist','pseudo','nom','prenom']


class ProjetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nom']}),
        ('Autres infos', {'fields': ['prix', 'date_upload', 'date_sortie', 'precommandable', 'etat'], 'classes': ['collapse']}),
    ]
    inlines = [SonInLine]
    search_fields = ['id_projet','nom','date_sortie','precommandable','etat']
    list_display = ['id_projet','nom','prix','date_sortie','precommandable','etat','id_artist','id_type','date_upload']


class TypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['libelle']}),
    ]
    search_fields = ['libelle','id_type']
    list_display = ['id_type','libelle']


class GenreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['libelle']}),
    ]
    search_fields = ['libelle','id_genre']
    list_display = ['id_genre','libelle']


class SonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['titre']}),
        (None, {'fields': ['id_projet']}),
        (None, {'fields': ['id_genre']}),
        (None, {'fields': ['featurings']}),
        (None, {'fields': ['prix']}),
        (None, {'fields': ['chemin_audio']}),
    ]
    search_fields = ['titre','prix']
    list_display = ['id_son','titre','id_projet','id_genre','featurings','prix','chemin_audio']


class ReglementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id_artiste']}),
        (None, {'fields': ['id_moderateur']}),
        (None, {'fields': ['montant']}),
        (None, {'fields': ['periode']}),
        (None, {'fields': ['date']}),
    ]
    search_fields = ['periode', 'date']
    list_display = ['id_reglement','id_artiste','id_moderateur','montant','periode','date']


class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nom_playlist']}),
        (None, {'fields': ['categorie']}),
        (None, {'fields': ['photo']}),
        (None, {'fields': ['id_moderateur']}),
    ]
    search_fields = ['nom_playlist']
    list_display = ['id_playlist','nom_playlist','categorie','photo']


class PistePlaylistAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id_playlist','id_son']

admin.site.register(Artiste,ArtisteAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Son, SonAdmin)
admin.site.register(Reglement, ReglementAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(PistePlaylist, PistePlaylistAdmin)