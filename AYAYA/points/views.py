from django.shortcuts import render
from django.db.models import Q
from .models import Point

def map_view(request):
    query = request.GET.get('q', '').strip()
    year = request.GET.get('year', '').strip()

    points = Point.objects.all()
    if query:
        points = points.filter(name__icontains=query)
    if year:
        # validate year as integer, ignore invalid
        try:
            year_int = int(year)
            points = points.filter(year=year_int)
        except ValueError:
            pass
    # Prepare points with radius converted to meters and image URL
    points_data = [
        {
            'name': point.name,
            'latitude': point.latitude,
            'longitude': point.longitude,
            'description': point.description,
            'radius': point.buffer_radius * 111000,  # Convert degrees to meters
            'image': point.image.url if point.image else None,  # Include image URL or None
            'year': point.year,
        }
        for point in points
    ]
    # Distinct available years for dropdown
    available_years = (
        Point.objects.order_by('year')
        .values_list('year', flat=True)
        .distinct()
        .exclude(year__isnull=True)
    )
    context = {'points_data': points_data, 'available_years': available_years}
    return render(request, 'points/map.html', context)