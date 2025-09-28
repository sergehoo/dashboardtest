from django.shortcuts import render

# Create your views here.
# views.py
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'dashbord_sample.html'


class SantePopulationView(TemplateView):
    template_name = 'sante_population.html'


class AccesServicesView(TemplateView):
    template_name = 'acces_services.html'


class QualiteSoinsView(TemplateView):
    template_name = 'qualite_soins.html'


class RessourcesHumainesView(TemplateView):
    template_name = 'ressources_humaines.html'


class InfrastructuresView(TemplateView):
    template_name = 'infrastructures.html'


class MedicamentsView(TemplateView):
    template_name = 'medicaments.html'


class FinancementView(TemplateView):
    template_name = 'financement.html'


class CMUView(TemplateView):
    template_name = 'cmu.html'


class SantePubliqueView(TemplateView):
    template_name = 'sante_publique.html'


class SanteMaternelleView(TemplateView):
    template_name = 'sante_maternelle.html'


class SanteCommunautaireView(TemplateView):
    template_name = 'sante_communautaire.html'


class GouvernanceView(TemplateView):
    template_name = 'gouvernance.html'


class UrgencesView(TemplateView):
    template_name = 'urgences.html'
