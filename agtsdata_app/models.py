from django.db import models



# models.py
from django.contrib.auth.models import User  # ou ton CustomUser


class Projet(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_lancement = models.DateField()
    image = models.ImageField(upload_to='projets/', null=True, blank=True)
    
    likes = models.ManyToManyField(User, related_name='projets_aimes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.nom


class MembreEquipe(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='equipe/', blank=True, null=True)
    biographie = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"


from django.db import models

class Service(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    icone = models.CharField(max_length=100, help_text="Classe FontAwesome (ex: 'fas fa-chart-pie')", blank=True)
    ordre_affichage = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    details = models.TextField(blank=True, help_text="Détails complémentaires sur ce service")
    prix_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Prix minimum pour ce service")
    prix_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Prix maximum pour ce service")


    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['ordre_affichage']
