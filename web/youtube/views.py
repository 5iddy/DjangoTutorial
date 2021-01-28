from django.shortcuts import render
from . import models
# Create your views here.
def home_view(request):
    context = {}
    if request.method == 'POST':
        url = request.POST.get('url')
        info = models.YtVid.fetch_info(url)
        context['formats'] = info['formats']

    return render(request, 'home/index.html', context)