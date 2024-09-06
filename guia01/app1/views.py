from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(resquest):
    return HttpResponse("<h1> Soy el index de la app1</h1>")

def presentacion(request):
    html="""
        <p>Soy el parrafo de la app1.</p>
        <h2> soy un subtitulo de la app1</h2>
    """
    return HttpResponse(html)

