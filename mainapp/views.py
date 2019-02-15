from django.shortcuts import render

def main(request):
	return render(request, 'mainapp/main.html')

def a(request):
	return render(request, 'mainapp/a.html')
	