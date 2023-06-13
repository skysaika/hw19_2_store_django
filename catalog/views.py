from django.shortcuts import render

# Create your views here.
def index(request):
    """Контроллер для отображения главной страницы """
    return render(request, 'catalog/index.html')


def contacts(request):
    """Контроллер для отображения страницы contacts"""
    if request.method == 'POST':
        # Обработка данных формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')
    return render(request, 'catalog/contacts.html')
