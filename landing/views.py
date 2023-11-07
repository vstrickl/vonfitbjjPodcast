from django.shortcuts import render
from django.conf import settings

from .models import Hero, SocialMenu

# Create your views here.
def landing_page(request):

    hero = Hero.objects.get(pk=1)
    font = Hero.objects.prefetch_related('header_font', 'general_font').get(pk=1)
    social = SocialMenu.objects.all()

    google_tag_url = settings.MEASUREMENT_ID
    measurement_id = settings.GOOGLE_TAG_URL

    context = {            
        'h':hero,
        'font':font,
        'social':social,
        'google_tag_url':google_tag_url,
        'measurement_id':measurement_id,
    }
    
    return render(request, 'landing_page.html', context)