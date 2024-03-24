from django.shortcuts import render

# Create your views here.
def home(request):
    #This command will render the request and fetch the given template file
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def more(request):
    return render(request, 'more.html')
