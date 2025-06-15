from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),

    # Une seule URL "contact/"
    path('contact/', views.contact, name='contact'),
    
    # Une deuxième version optionnelle à une autre URL
    path('contact2/', views.contact_view, name='contact2'),

    path('equipe/', views.equipe_view, name='equipe'),
    path('projets/<int:pk>/', views.projet_detail, name='projet_detail'),
    path('projets/', views.projets_list, name='projets'),
    path('projets/<int:projet_id>/like/', views.toggle_like, name='toggle_like'),
    path('like-ajax/', views.toggle_like_ajax, name='toggle_like_ajax'),
    path('services/', views.services_view, name='services'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),

]
