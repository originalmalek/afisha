from django.http import HttpResponse



def first_page(request):
    return HttpResponse("<h2>Здесь будет карта</h2>")