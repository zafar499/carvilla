from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def details1_view(request):
    return render(request, 'details_1.html')

def details2_view(request):
    return render(request, 'details_2.html')

def details3_view(request):
    return render(request, 'details_3.html')