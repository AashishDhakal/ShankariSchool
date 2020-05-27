from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from school.forms import ParentInformationForm

from school.models import *
import random

def Homepage(request):
    notices = Notices.objects.all().order_by("-published_date")
    messageofceo = CEOMessage.objects.first()
    testimonials = Testimonials.objects.all()
    aboutsections = AboutSection.objects.all()
    importantnotice = ImportantNotice.objects.first()
    downloads = Downloads.objects.all()
    images = Gallery.objects.all()
    random_number = random.random()
    homepageimage = HomePage.objects.first()
    teammembers=TeamMember.objects.all()
    return render(request,"index.html",{'notices':notices,'homepageimage':homepageimage,'message':messageofceo,'testimonials':testimonials,'aboutsections':aboutsections,'importantnotice':importantnotice,'downloads':downloads,'random_number':random_number,'images':images,'teammembers':teammembers})

def GalleryView(request):
    images = Gallery.objects.all()
    return render(request,"gallery.html",{'images':images})


class NoticeDetailView(DetailView):
    template_name = 'notice.html'
    model = Notices

class AboutDetailView(DetailView):
    template_name = 'aboutdetail.html'
    model = AboutSection

def page_not_found_view(request):
    return render(request,'404.html',status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def ParentInformationView(request):
    form = ParentInformationForm()
    if request.POST:
        form = ParentInformationForm(request.POST)
        form.save()
        return render(request,'parentinformation.html',{'form':form})
    return render(request,'parentinformation.html',{'form':form})