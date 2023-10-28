from django.shortcuts import render

from .models import Hero, SocialMenu

# Create your views here.
def landing_page(request):

    hero = Hero.objects.get(pk=1)
    font = Hero.objects.prefetch_related('header_font', 'general_font').get(pk=1)
    social = SocialMenu.objects.all()

    context = {            
        'h':hero,
        'font':font,
        'social':social,
    }
    
    return render(request, 'landing_page.html', context)