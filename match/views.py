from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .models import MatchedUser
from .models import GameSeed
from django.shortcuts import redirect
import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        p = Profile.objects.get(user_id = request.user.id)
        return render(request, 'match/index.html',{'gameseeds' : GameSeed.objects.all, 'ugame':p.seeds.all, 'name':request.user.id})
    return render(request, 'match/index.html')
def gameselect(request):
    p = Profile.objects.get(user_id = request.user.id)
    return render(request, 'match/gameselect.html',{'gameseeds' : GameSeed.objects.all, 'ugame':p.seeds.all } )



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

@csrf_exempt
def gamesearch(request):
    if request.method=='POST':
        gamename = request.POST.get('name', None)
        u = User.objects.get(username=request.user.username)
        pf = Profile.objects.get(user_id=u.id)
        pf.running = True
        pf.save()
    try:
        matched = MatchedUser.objects.get(user_id=u.id)
        context = {'chatroom':  matched.chatroom}
        return HttpResponse(json.dumps(context), content_type="application/json")
    except MatchedUser.DoesNotExist:
        return HttpResponse(json.dumps(''), content_type="application/json")

        