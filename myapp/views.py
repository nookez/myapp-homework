from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def detail1(request):
    return render(request, 'detail1.html')

def detail2(request):
    return render(request, 'detail2.html')

def detail3(request):
    return render(request, 'detail3.html')

def detail4(request):
    return render(request, 'detail4.html')

from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')  # หรือชื่อไฟล์เทมเพลตที่ต้องการ
