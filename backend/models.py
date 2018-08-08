# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ctypes import py_object

from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.

@python_2_unicode_compatible
class Moderateur(AbstractUser):
    id_moderateur = models.AutoField(primary_key=True, verbose_name='ID')
    num_tel = models.CharField(max_length=25, blank=True)
    pays = models.CharField(max_length=50, blank=True)
    nom = models.CharField(max_length=50, blank=True)
    prenom = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class Type(models.Model):
    id_type = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=25)

    def __str__(self):
        return self.libelle


@python_2_unicode_compatible
class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=25)

    def __str__(self):
        return self.libelle


@python_2_unicode_compatible
class Artiste(models.Model):
    id_artist = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=100, blank=True)
    label = models.CharField(max_length=50, blank=True)
    photo = models.FileField()
    email = models.EmailField()
    num_tel = models.CharField(max_length=25, blank=True)
    pays = models.CharField(max_length=50, blank=True)
    nom = models.CharField(max_length=50, blank=True)
    prenom = models.CharField(max_length=50, blank=True)
    id_moderateur = models.ForeignKey(Moderateur, default=0)

    def __str__(self):
        return self.pseudo


@python_2_unicode_compatible
class Projet(models.Model):
    id_projet = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50,)
    prix = models.FloatField()
    date_upload = models.DateTimeField()
    date_sortie = models.DateTimeField()
    precommandable = models.BooleanField(default=False)
    etat = models.BooleanField(default=False)
    id_artist = models.ForeignKey(Artiste)
    id_type = models.ForeignKey(Type)
    cover = models.FileField()

    def __str__(self):
        return self.nom


@python_2_unicode_compatible
class Son(models.Model):
    id_son = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=25)
    id_projet = models.ForeignKey(Projet)
    id_genre = models.ForeignKey(Genre)
    featurings = models.CharField(max_length=255, blank=True)
    prix = models.FloatField(default=0)
    chemin_audio = models.FileField()

    def __str__(self):
        return self.titre


class Reglement(models.Model):
    id_reglement = models.AutoField(primary_key=True)
    id_artiste = models.ForeignKey(Artiste)
    id_moderateur = models.ForeignKey(Moderateur)
    montant = models.FloatField()
    periode = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField()


@python_2_unicode_compatible
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    photo = models.FileField()
    num_tel = models.CharField(max_length=25, blank=True)
    pays = models.CharField(max_length=50, blank=True)
    nom = models.CharField(max_length=50, blank=True)
    prenom = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username

@python_2_unicode_compatible
class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    nom_playlist = models.CharField(max_length=25)
    categorie = models.BooleanField()
    photo = models.FileField(blank=True)
    id_client = models.ForeignKey(Client, null=True)
    id_moderateur = models.ForeignKey(Moderateur, null=True)

    def __str__(self):
        return self.nom_playlist


class PistePlaylist(models.Model):
    id_son = models.ForeignKey(Son)
    id_playlist = models.ForeignKey(Playlist)


class Ecoutes(models.Model):
    id_client = models.ForeignKey(Client)
    id_son = models.ForeignKey(Son)
    nb_ecoutes = models.IntegerField()


class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client)
    date = models.DateTimeField()
    montant = models.FloatField()


class Achat(models.Model):
    id_achat = models.AutoField(primary_key=True)
    id_son = models.ForeignKey(Son)
    id_projet = models.ForeignKey(Projet)
    id_commande = models.ForeignKey(Commande)


class Abonnement(models.Model):
    id_abonnement = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client)
    date_deb = models.DateTimeField()
    date_fin = models.DateTimeField()
    prix = models.FloatField()


class Precommande(models.Model):
    id_abonnement = models.ForeignKey(Abonnement)
    id_projet = models.ForeignKey(Projet)