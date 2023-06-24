from django.shortcuts import render

def home(request):
    template = 'catalog/home.html'
    return render(request, template, {})

def about(request):
    template = 'catalog/about.html'
    return render(request, template, {})

def contacts(request):
    template = 'catalog/contacts.html'
    context = {}
    if request.method == 'POST':
        context.update(request.POST.dict())
    return render(request, template, context)