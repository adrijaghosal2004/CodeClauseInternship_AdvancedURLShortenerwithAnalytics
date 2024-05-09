from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Short
from .data import newShortUrl
from datetime import datetime
import pyshorteners

def index(request):
    return render(request, 'index.html')

def shortenedUrl(request):
    if request.method == 'POST':
        form = newShortUrl(request.POST)
        if form.is_valid():
            original = form.cleaned_data['originalUrl']
            sh = pyshorteners.Shortener()
            surl = sh.tinyurl.short(original)
            date = datetime.now()
            s = Short(originalUrl=original, shortUrl=surl, date_and_time=date)
            s.save()
            generated_url = reverse('forward', kwargs={'url': surl})
            return redirect(generated_url)
        else:
            return render(request, 'build.html', {'form': form})
    else:
        form = newShortUrl()
        return render(request, 'build.html', {'form': form})


def forward(request, url):
    try:
        short_object = Short.objects.get(shortUrl=url)
        return render(request, 'forward.html', {'obj': short_object})
    except Short.DoesNotExist:
        return render(request, 'unavailable.html')
    except Short.MultipleObjectsReturned:
        short_objects = Short.objects.filter(shortUrl=url)
        first_object = short_objects.first()  # Get the first object
        return render(request, 'forward.html', {'obj': first_object})

