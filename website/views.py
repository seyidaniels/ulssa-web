from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Executive, Gallery, Event

# Create your views here.
class IndexView(View):
    template_name = "website/index.html"
    def get(self, request):
        gallery = Gallery.objects.order_by('?')[:5]
        gallery_captions = gallery.only('caption')
        latest_event = Event.objects.latest('id')
        
        return render(request, self.template_name, {
            'executives': Executive.objects.all(),
            'gallery': gallery,
            'captions': gallery_captions,
            'event': latest_event
        })

class ContactView(View):
    template_name = "website/contact.html"
    def get(self, request):
        return render(request, self.template_name)