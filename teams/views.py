from django.shortcuts import render
from django.views import View
from .models import AWSTeams
# Create your views here.

class AWSTeamList(View):
    def get(self,request):
        teams=AWSTeams.objects.all()
        context={
            'teams':teams
        }
        return render(request,'teams/teams_list.html',context)