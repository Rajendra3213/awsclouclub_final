from django.shortcuts import render
from django.views import View
from event.models import GrandEventSystem,EventSystem
from blog.models import AWSBlog
from django.utils import timezone
from datetime import datetime
class HomeView(View):

    def get(self,request):
        latest_events = EventSystem.objects.order_by('-startDate')[:3]
        latest_blogs=AWSBlog.objects.order_by('-date_of_publish')[:3]
        current_time = timezone.now()
        current_time=current_time.replace(hour=0, minute=0, second=0)
        grand_event = GrandEventSystem.objects.filter(EventStatus='Ongoing',startDate__gt=current_time).order_by('startDate').first()
        context={
            'events':latest_events,
            'blogs':latest_blogs,
            'grand_event':grand_event
        }
        return render(request,'home/homepage.html',context)
    
def custom_404(request, exception):
    return render(request, "home/404.html")

class AboutUs(View):
    def get(self,request):
        return render(request,'home/aboutus.html')