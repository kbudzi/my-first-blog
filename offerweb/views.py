from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Kontrahent , Oferty, Indeksy, Operacje, Technologia
from .forms import KontrahentForm, OfertaForm, IndeksForm,OperacjeForm, TechnologiaForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from simple_search import search_filter

def glowna(request):
    
    return render(request, 'home.html')


@login_required
def wszystkie_oferty(request):
    oferty =Oferty.objects.all()
    return render(request, 'oferty.html',{'oferty': oferty})

def nowa_oferta(request):
    oferta_form =OfertaForm(request.POST or None)
    if oferta_form.is_valid():
        oferta_form.save()
        return redirect(wszystkie_oferty)
        
    return render(request, 'nowa_oferta.html',{'oferta_form': oferta_form})

@login_required
def edytuj_top_oferty(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    oferta_form =OfertaForm(request.POST or None, instance=oferty)
    indeksy = Indeksy.objects.filter(Oferta=oferty)
    
    if oferta_form.is_valid():
        oferta_form.save()
        return redirect(wszystkie_oferty)
    return render(request, 'edytuj_oferte.html',{'oferta_form': oferta_form, 'indeksy':indeksy})
@login_required
def edytuj_oferte(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    kontrahent = Kontrahent.objects.get(pk=oferty.kontrahenci.id)
    #kontrahent = get_object_or_404(Kontrahent, pk=id)
    oferta_form =OfertaForm(request.GET or None, instance=oferty)
    indeksy = Indeksy.objects.filter(oferta=oferty)
    #kontrahent = Kontrahent.objects.filter(oferta=kontrahent) # lista indeksów dla danej oferty
    indeksy_form = IndeksForm(request.POST or None)#instance=oferty
    if request.method == 'POST':
        if 'indeks' in request.POST:
            indeks = indeksy_form.save(commit=False)
            indeks.oferta = oferty
            indeks.kontrahent = kontrahent
            indeks.save()
            return HttpResponseRedirect(reverse("edytuj_oferte", args=[id]))
    #t=kontrahent.id
    t=oferty.id
    return render(request, 'edytuj_oferte.html',{'oferta_form': oferta_form, 'indeksy':indeksy, 'indeksy_form':indeksy_form, 't':t})

@login_required
def usun_oferte(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    if request.method == "POST":
        oferty.delete()
        return redirect (wszystkie_oferty)
    return render(request, 'usun_oferte.html',{'oferty': oferty})

def kontrahent(request):
    kontrahenci = Kontrahent.objects.all()
    return render(request, 'kontrahent.html',{"kontrahenci":kontrahenci})

def nowy_kontrahent(request):
    kontrahenci_form =KontrahentForm(request.POST or None)
    
    
    if kontrahenci_form.is_valid():
        kontrahenci_form.save()
        return redirect('/')
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})

def edytuj_kontrahent(request, id):
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    kontrahenci_form =KontrahentForm(request.POST or None, instance=kontrahenci)
    if kontrahenci_form.is_valid():
        kontrahenci_form.save()
        return redirect(kontrahent)
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})
@login_required

def indeksy_kontrahent(request, id):
    
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    indeksy = Indeksy.objects.filter(kontrahent=kontrahenci)
    
    return render(request, 'wybierz_indeks.html',{'indeksy': indeksy, 'kontrahenci':kontrahenci})

def indeksy_oferta(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    kontrahent = Kontrahent.objects.get(pk=oferty.kontrahenci.id)
    #ind = Indeksy.objects.all()
    indeksy = Indeksy.objects.filter(kontrahent=kontrahent)
    indeksy_form = IndeksForm (request.POST or None)

    if request.method == "POST":
        for i in indeksy:
        #i= Indeksy.objects.get(pk=ind.indeks)
            print(i.id)
        #ind.delete()
    
    return render(request, 'wybierz_indeks2.html',{'indeksy': indeksy, 'oferty':oferty, 'indeksy_form':indeksy_form})
#def dodaj_do_bazy():
@login_required
def add_indeks(request, id):
    indeksy = get_object_or_404(Indeksy, pk=id)
    if request.method == "POST":
        indeksy.delete()
        return redirect (wszystkie_oferty)        

@login_required
def usun_kontrahenta(request, id):
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    if request.method == "POST":
        kontrahenci.delete()
        return redirect (kontrahent)

    return render(request, 'usun_kontrahenta.html',{'kontrahenci': kontrahenci})
@login_required
def usun_indeks(request, id):
    indeks = get_object_or_404(Indeksy, pk=id)
    oferta_id = indeks.oferta.id
    if request.method == "POST":
        indeks.delete()
        #return redirect (wszystkie_oferty)
        return redirect("edytuj_oferte", id=oferta_id)
    return render(request, 'usun_indeks.html',{'indeks': indeks})

@login_required
def edytuj_indeks(request, id):
    indeks = get_object_or_404(Indeksy, pk=id)
    oferta_id = indeks.oferta.id
    indeksy_form = IndeksForm(request.POST or None, instance=indeks)
    technologia = Technologia.objects.filter(indeks=indeks)
    technologia_form = TechnologiaForm(request.POST or None, instance=indeks)
    if indeksy_form.is_valid():
        indeksy_form.save()
        return redirect("edytuj_oferte", id=oferta_id)
            
        

    return render(request, 'edytuj_indeks.html',{'indeksy_form':indeksy_form,'technologia_form':technologia_form,'technologia':technologia})


@login_required
def operacje(request):
    operacje =Operacje.objects.all()
    return render(request, 'operacje.html',{'operacje': operacje})

def dodaj_operacje(request):
    operacje_form =OperacjeForm(request.POST or None)
    
    
    if operacje_form.is_valid():
        operacje_form.save()
        return redirect('operacje')
    return render(request, 'dodaj_operacje.html',{'operacje_form': operacje_form})

def usun_operacje(request,id):
    operacja = get_object_or_404(Operacje, pk=id)
    if request.method == "POST":
        operacja.delete()
        return redirect ('operacje')

    return render(request, 'usun_operacje.html',{'operacja': operacja})
