from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from school.models import Notices

def Homepage(request):
    notices = Notices.objects.all()
    return render(request,"index.html",{'notices':notices,})

class NoticeDetailView(DetailView):
    template_name = 'notice.html'
    model = Notices