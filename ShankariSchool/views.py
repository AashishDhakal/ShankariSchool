from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from school.models import Notices,CEOMessage,Testimonials,AboutSection,ImportantNotice,Downloads,Gallery

def Homepage(request):
    notices = Notices.objects.all()
    messageofceo = CEOMessage.objects.first()
    testimonials = Testimonials.objects.all()
    aboutsections = AboutSection.objects.all()
    importantnotice = ImportantNotice.objects.first()
    downloads = Downloads.objects.all()
    images = Gallery.objects.all()
    return render(request,"index.html",{'notices':notices,'message':messageofceo,'testimonials':testimonials,'aboutsections':aboutsections,'importantnotice':importantnotice,'downloads':downloads,'images':images})

class NoticeDetailView(DetailView):
    template_name = 'notice.html'
    model = Notices

class AboutDetailView(DetailView):
    template_name = 'aboutdetail.html'
    model = AboutSection
