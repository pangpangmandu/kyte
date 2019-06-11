from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .models import MatchedUser
from .models import GameSeed
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        p = Profile.objects.get(user_id = request.user.id)
        return render(request, 'match/index.html',{'gameseeds' : GameSeed.objects.all, 'ugame':p.seeds.all })
    return render(request, 'match/index.html')
def gameselect(request):
    p = Profile.objects.get(user_id = request.user.id)
    return render(request, 'match/gameselect.html',{'gameseeds' : GameSeed.objects.all, 'ugame':p.seeds.all } )

def gamesearch(request):
    name = request.POST['gamename']
    num = request.POST['player']
    u = User.objects.get(username=request.user.username)
    pf = Profile.objects.get(user_id=u.id)
    pf.running = True
    pf.save()
    try:
        matched = MatchedUser.objects.get(user_id=u.id)
        return render(request, 'match/gamesearch.html',{'name':name, 'num': num, 'chatroom': matched.chatroom})
    except MatchedUser.DoesNotExist:
        print('Not in matched user')
        return render(request, 'match/gamesearch.html',{'name':name, 'num': num, 'chatroom': 'null'})

    #print(request.user.username)
    return render(request, 'match/gamesearch.html',{'name':name, 'num': num})

def result(request):
    return render(request, "match/result.html",)

def mypage(request):
    return render(request,"match/mypage.html" ,)

def assessment(request):
    return render(request, 'match/assessment.html', )
def gameadd(request):
    user = Profile.objects.get(user_id=request.user.id)
    g  = GameSeed.objects.get(gamename=request.POST['game'])
    g.users.add(user)
    return redirect('/match')
