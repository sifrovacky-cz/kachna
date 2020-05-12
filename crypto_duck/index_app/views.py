from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'static/index.html')

def info(request):
    return render(request,'static/info.html')
    
def results(request):
    return render(request,'static/results.html')
        
def rules(request):
    return render(request,'static/rules.html')