from django.shortcuts import render
from . models import Cliente

def index(request):
	return render(request, 'index.html')