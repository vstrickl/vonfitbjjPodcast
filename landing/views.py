from django.shortcuts import render

from .models import Hero, SocialMenu

# Create your views here.
def landing_page(request):

    hero = Hero.objects.all()
    social = SocialMenu.objects.all()

    context = {            
        'hero':hero,
        'social':social,
    }
    
    return render(request, 'landing_page.html', context)