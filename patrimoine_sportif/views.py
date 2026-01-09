from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Site, SiteOlympique, Typologie, Denomination, DateReference

def site_list(request):
    # Base queryset
    queryset = Site.objects.all().order_by('appellation')
    
    # Filtering
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(appellation__icontains=query) | 
            Q(commune__icontains=query) | 
            Q(description__icontains=query)
        )
    
    site_olympique_id = request.GET.get('site_olympique')
    if site_olympique_id:
        queryset = queryset.filter(site_olympique_id=site_olympique_id)
        
    typologie_ids = request.GET.getlist('typologie')
    if typologie_ids:
        queryset = queryset.filter(typologies__id__in=typologie_ids).distinct()

    denomination_ids = request.GET.getlist('denomination')
    if denomination_ids:
        queryset = queryset.filter(denominations__id__in=denomination_ids).distinct()
        
    departement = request.GET.get('departement')
    if departement:
        queryset = queryset.filter(departement=departement)

    # Context Data for Filters
    context = {
        'sites_olympiques': SiteOlympique.objects.all().order_by('nom'),
        'typologies': Typologie.objects.all().order_by('nom'),
        'denominations': Denomination.objects.all().order_by('nom'),
        'departements': Site.objects.values_list('departement', flat=True).distinct().order_by('departement'),
        'selected_typologies': [int(x) for x in typologie_ids if x.isdigit()],
        'selected_denominations': [int(x) for x in denomination_ids if x.isdigit()],
    }

    # Pagination
    paginator = Paginator(queryset, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context['page_obj'] = page_obj
    return render(request, 'patrimoine_sportif/site_list.html', context)

def site_detail(request, pk):
    site = get_object_or_404(Site, pk=pk)
    return render(request, 'patrimoine_sportif/site_detail.html', {'site': site})
