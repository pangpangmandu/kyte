from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'match/index.html',)

def gameselect(request):
    return render(request, 'match/gameselect.html', )

def gamesearch(request):
    name = request.POST['gamename']
    num = request.POST['player']
    return render(request, 'match/gamesearch.html',{'name':name, 'num': num})

def result(request):
    return render(request, "match/result.html",)

def mypage(request):
    return render(request,"match/mypage.html" ,)