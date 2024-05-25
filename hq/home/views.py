from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views her

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    beleske = Beleska.objects.all()
    context = {'beleske': beleske}

    return render(request, 'home/home.html', context)


@login_required(login_url=settings.LOGIN_URL)
def dodaj_belesku(request):

    if request.method == "POST":
        naslov = request.POST.get('naslov')
        text = request.POST.get('text')

        nova_beleska = Beleska(naslov=naslov, text=text)
        nova_beleska.save()


    
    return redirect('home')

@login_required(login_url=settings.LOGIN_URL)
def pregledaj_belesku(request, beleska_id):

    beleska = Beleska.objects.get(id=beleska_id)

    context = {'beleska': beleska}
    return render(request, 'home/pregledaj_belesku.html', context)

@login_required(login_url=settings.LOGIN_URL)
def obrisi_belesku(request, beleska_id):
    beleska = Beleska.objects.get(id=beleska_id)

    beleska.delete()

 
    return redirect('home')

@login_required(login_url=settings.LOGIN_URL)
def izmeni_belesku(request, beleska_id):
   
    beleska = Beleska.objects.get(id=beleska_id)

    if request.method == "POST":
        text = request.POST.get('text')
        print(text)
        beleska.text = text

        beleska.save()
        
        return redirect('pregledaj_belesku', beleska_id=beleska.id)
    
    return redirect('home')

@login_required(login_url=settings.LOGIN_URL)
def profil(request):



    return render(request, 'home/profil.html')

@login_required(login_url=settings.LOGIN_URL)
def projekti(request):
    projekti = Projekat.objects.all()
    clanovi = Clan.objects.all()

    if request.method == "POST":
        ime = request.POST.get('ime')
        deskripcija = request.POST.get('deskripcija')
        clanovii = request.POST.getlist('clanovi')
        slika = request.POST.get('slika')

        novi_projekat = Projekat(ime=ime, deskripcija=deskripcija, slika=slika)
        novi_projekat.save()

        if clanovii:
            novi_projekat.clanovi.set(clanovii)


        return redirect('projekti')

    context = {'projekti': projekti, 'clanovi': clanovi}
    
    return render(request, 'home/projekti.html', context)

@login_required(login_url=settings.LOGIN_URL)
def clanovi(request):

    clanovi = Clan.objects.all()
    context = {'clanovi': clanovi}
    
    return render(request, 'home/clanovi.html', context)

@login_required(login_url=settings.LOGIN_URL)
def webftp(request):



    return render(request, 'home/webftp.html')

@login_required(login_url=settings.LOGIN_URL)
def masine(request):

    masine = Masina.objects.all()
    context = {'masine': masine}
    
    return render(request, 'home/masine.html', context)

@login_required(login_url=settings.LOGIN_URL)
def copilot(request):



    return render(request, 'home/copilot.html')

@login_required(login_url=settings.LOGIN_URL)
def planovi(request):



    return render(request, 'home/planovi.html')

@login_required(login_url=settings.LOGIN_URL)
def obuka(request):



    return render(request, 'home/obuka.html')

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Preusmeri na željenu stranicu nakon prijave
        else:
            context['error'] = 'Pogrešno korisničko ime ili lozinka.'

    if not context:
        context = None

    return render(request, 'home/login.html', context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')

def projekat(request, projekat_id):

    projekat = Projekat.objects.get(id=projekat_id)

    context = {'projekat':projekat}

    return render(request, 'home/projekat.html', context)



