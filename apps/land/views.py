from django.http import HttpResponse, Http404
from django.shortcuts import render
def index(request):
	user_info = {
		'name' : "Orion Supergan",
		'sport' : "video games",
		'language' : "Python",
	}
	return render(request, 'land/index.html', user_info)


def land(request):
	user_info = {
		'name' : "Orion Supergan",
		'sport' : "video games",
		'language' : "Python",
	}
	return render(request, 'land/index.html', user_info)