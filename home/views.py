from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-oscar', 'url': 'http://pypi.python.org/pypi/django-oscar/1.5.1'},
    ]
    context = {
        'title': 'valeria-crowdbotics-83',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
