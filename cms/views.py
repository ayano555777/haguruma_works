from django.shortcuts import render

# Create your views here.


def hagurumasite(request):
    return render(request, 'cms/lpage.html', {})
