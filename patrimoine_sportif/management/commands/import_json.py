import json
import os
from django.core.management.base import BaseCommand
from patrimoine_sportif.models import Site, SiteOlympique, Typologie, Denomination, DateReference
from django.conf import settings

class Command(BaseCommand):
    help = 'Import sites from JSON file'

    def handle(self, *args, **kwargs):
        json_file_path = os.path.join(settings.BASE_DIR, 'sites-sportifs-emblematiques.json')
        
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
            return

        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            try:
                # Handle SiteOlympique (1-N)
                site_olympique_name = item.get('site_olympique')
                site_olympique = None
                if site_olympique_name:
                    site_olympique, _ = SiteOlympique.objects.get_or_create(nom=site_olympique_name)

                # Create Site
                site, created = Site.objects.update_or_create(
                    appellation=item.get('appellation', 'Sans nom'),
                    defaults={
                        'remarquable': item.get('type_de_reconnaissance_patrimoniale'),
                        'departement': item.get('departement'),
                        'commune': item.get('commune'),
                        'adresse': item.get('adresse'),
                        'code_postal': item.get('code_postal'),
                        'latitude': item.get('geo', {}).get('lat') if item.get('geo') else None,
                        'longitude': item.get('geo', {}).get('lon') if item.get('geo') else None,
                        'informations_transport': item.get('informations_d_acces_en_transport_en_commun'),
                        'site_olympique': site_olympique,
                        'datation': item.get('datation'),
                        'periode_construction': item.get('periode_de_construction'),
                        'description': item.get('historique_et_description'),
                        'credits': item.get('credits'),
                        'url_image': item.get('url_image'),
                    }
                )

                # Handle ManyToMany relationships
                
                # Typologie
                typologies_list = item.get('typologie')
                if typologies_list:
                    for nom in typologies_list:
                        obj, _ = Typologie.objects.get_or_create(nom=nom)
                        site.typologies.add(obj)

                # Denomination
                denominations_list = item.get('denomination')
                if denominations_list:
                    for nom in denominations_list:
                        obj, _ = Denomination.objects.get_or_create(nom=nom)
                        site.denominations.add(obj)

                # DateReference
                dates_list = item.get('date_s_de_reference')
                if dates_list:
                    for annee in dates_list:
                        obj, _ = DateReference.objects.get_or_create(annee=annee)
                        site.dates_reference.add(obj)
                
                action = "Created" if created else "Updated"
                self.stdout.write(self.style.SUCCESS(f'{action} site: {site.appellation}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error importing item: {e}'))

        self.stdout.write(self.style.SUCCESS('Import completed successfully'))
