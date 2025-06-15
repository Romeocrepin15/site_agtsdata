from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import Projet, MembreEquipe, MessageContact
from .forms import MessageContactForm


# Accueil
def accueil(request):
    projets = Projet.objects.all().order_by('-date_lancement')
    membres = MembreEquipe.objects.all()
    return render(request, 'agtsdata_app/accueil.html', {
        'projets': projets,
        'membres': membres
    })


# Liste paginée des projets
def projets_list(request):
    projets = Projet.objects.all().order_by('-date_lancement')
    paginator = Paginator(projets, 6)  # 6 projets par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'agtsdata_app/projets_list.html', {'page_obj': page_obj})


# Détail d’un projet
def projet_detail(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    return render(request, 'agtsdata_app/projet_detail.html', {'projet': projet})


# Liste des membres de l'équipe
def equipe_view(request):
    membres = MembreEquipe.objects.all()
    return render(request, 'agtsdata_app/equipe.html', {'membres': membres})


# Vue de contact avec formulaire, enregistrement et envoi d'email
def contact_view(request):
    if request.method == 'POST':
        form = MessageContactForm(request.POST)
        if form.is_valid():
            message_obj = form.save()

            # Email à l'équipe AGTS
            sujet_admin = f"[Contact AGTS] {message_obj.sujet}"
            contenu_admin = (
                f"Nom: {message_obj.nom}\n"
                f"Email: {message_obj.email}\n\n"
                f"Message:\n{message_obj.message}"
            )
            send_mail(sujet_admin, contenu_admin, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

            # Accusé de réception à l'expéditeur
            sujet_accuse = "Accusé de réception - AGTS DATA"
            contenu_accuse = (
                f"Bonjour {message_obj.nom},\n\n"
                f"Merci pour votre message. Nous avons bien reçu :\n\n"
                f"\"{message_obj.message}\"\n\n"
                f"Notre équipe vous répondra bientôt.\n\n"
                f"--\nL’équipe AGTS DATA"
            )
            send_mail(sujet_accuse, contenu_accuse, settings.DEFAULT_FROM_EMAIL, [message_obj.email])

            messages.success(request, "Votre message a bien été envoyé.")
            return redirect('contact')
        else:
            messages.error(request, "Veuillez remplir correctement le formulaire.")
    else:
        form = MessageContactForm()

    messages_recus = MessageContact.objects.order_by('-date_envoi')[:5]

    return render(request, 'agtsdata_app/contact.html', {
        'form': form,
        'messages': messages_recus,
    })


# Like / Dislike d’un projet (bouton classique)
@login_required
def toggle_like(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.user in projet.likes.all():
        projet.likes.remove(request.user)
    else:
        projet.likes.add(request.user)
    return redirect('projet_detail', pk=projet.id)


# Like / Dislike AJAX
@login_required
def toggle_like_ajax(request):
    if request.method == "POST":
        projet_id = request.POST.get("projet_id")
        projet = get_object_or_404(Projet, id=projet_id)
        user = request.user

        liked = False
        if user in projet.likes.all():
            projet.likes.remove(user)
        else:
            projet.likes.add(user)
            liked = True

        return JsonResponse({
            'liked': liked,
            'total_likes': projet.likes.count()
        })

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import MessageContactForm
from .models import MessageContact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = MessageContactForm(request.POST)
        if form.is_valid():
            message_obj = form.save()

            # Envoi d’email à l’équipe AGTS
            sujet_admin = f"[Contact AGTS] {message_obj.sujet}"
            contenu_admin = (
                f"Nom: {message_obj.nom}\n"
                f"Email: {message_obj.email}\n\n"
                f"Message:\n{message_obj.message}"
            )
            send_mail(
                sujet_admin,
                contenu_admin,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )

            # Accusé de réception à l’expéditeur
            sujet_accuse = "Accusé de réception - AGTS DATA"
            contenu_accuse = (
                f"Bonjour {message_obj.nom},\n\n"
                f"Merci pour votre message. Nous avons bien reçu :\n\n"
                f"\"{message_obj.message}\"\n\n"
                f"Notre équipe vous répondra très bientôt.\n\n"
                f"-- L’équipe AGTS DATA"
            )
            send_mail(
                sujet_accuse,
                contenu_accuse,
                settings.DEFAULT_FROM_EMAIL,
                [message_obj.email],
            )

            messages.success(request, "Message envoyé avec succès.")
            return redirect('contact')
    else:
        form = MessageContactForm()

    derniers_messages = MessageContact.objects.order_by('-date_envoi')[:5]

    return render(request, 'agtsdata_app/contact.html', {
        'form': form,
        'messages': derniers_messages,
    })



from django.shortcuts import render
from .models import Service

def services_view(request):
    services = Service.objects.all()
    return render(request, 'agtsdata_app/services.html', {'services': services})


from django.shortcuts import render, get_object_or_404
from .models import Service

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'agtsdata_app/service_detail.html', {'service': service})
