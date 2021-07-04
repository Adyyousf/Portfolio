from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'name':"Ady", 'course':"Django"}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is my About page (/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is my Projects page (/projects)")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("This is my Contact page (/contact)")
    return render(request, 'contact.html')

