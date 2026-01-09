from django.db import models

class SiteOlympique(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nom

class Typologie(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom

class Denomination(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom

class DateReference(models.Model):
    annee = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.annee

class Site(models.Model):
    remarquable = models.CharField(max_length=255, null=True, blank=True, verbose_name="Type de reconnaissance patrimoniale")
    departement = models.IntegerField(null=True, blank=True)
    commune = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    code_postal = models.CharField(max_length=10, null=True, blank=True)
    
    # Coordinates
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    informations_transport = models.TextField(null=True, blank=True, verbose_name="Informations d'accès en transport en commun")
    appellation = models.CharField(max_length=255, verbose_name="Nom du site")
    
    # Relations
    site_olympique = models.ForeignKey(SiteOlympique, on_delete=models.SET_NULL, null=True, blank=True, related_name='sites')
    typologies = models.ManyToManyField(Typologie, blank=True, related_name='sites')
    denominations = models.ManyToManyField(Denomination, blank=True, related_name='sites')
    dates_reference = models.ManyToManyField(DateReference, blank=True, related_name='sites')
    
    datation = models.CharField(max_length=255, null=True, blank=True)
    periode_construction = models.CharField(max_length=255, null=True, blank=True, verbose_name="Période de construction")
    description = models.TextField(null=True, blank=True, verbose_name="Historique et description")
    credits = models.CharField(max_length=255, null=True, blank=True)
    url_image = models.URLField(max_length=500, null=True, blank=True)
    
    # Geo Point (Optional, storing as simple lat/lon fields above is often easier for basic usage, 
    # but if using PostGIS we could use PointField. Keeping it simple as requested)

    def __str__(self):
        return self.appellation
