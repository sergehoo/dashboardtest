# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.http import JsonResponse
from dashboard import views
def healthz(_):
    # ⚡ rapide : sans requête DB
    return JsonResponse({"status": "ok"})
urlpatterns = [
                  path("healthz", healthz),
                  path('', views.Home.as_view(), name='home'),
                  path('sante-population/', views.SantePopulationView.as_view(), name='sante_population'),
                  path('acces-services/', views.AccesServicesView.as_view(), name='acces_services'),
                  path('qualite-soins/', views.QualiteSoinsView.as_view(), name='qualite_soins'),
                  path('ressources-humaines/', views.RessourcesHumainesView.as_view(), name='ressources_humaines'),
                  path('infrastructures/', views.InfrastructuresView.as_view(), name='infrastructures'),
                  path('medicaments/', views.MedicamentsView.as_view(), name='medicaments'),
                  path('financement/', views.FinancementView.as_view(), name='financement'),
                  path('cmu/', views.CMUView.as_view(), name='cmu'),
                  path('sante-publique/', views.SantePubliqueView.as_view(), name='sante_publique'),
                  path('sante-maternelle/', views.SanteMaternelleView.as_view(), name='sante_maternelle'),
                  path('sante-communautaire/', views.SanteCommunautaireView.as_view(), name='sante_communautaire'),
                  path('gouvernance/', views.GouvernanceView.as_view(), name='gouvernance'),
                  path('urgences/', views.UrgencesView.as_view(), name='urgences'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
