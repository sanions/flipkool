from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime

from .upload import UploadForm, PresentForm
from .models import Upload


import shelve

# Create your views here.


def get_form(request):
    return render(request, 'upload/upload.html')


def save(pin, url, date):
    storage = shelve.open('storage2')
    save_dict = {url: date}
    storage[pin] = save_dict
    storage.close()


def submit(request):
    if request.method == 'POST':
        upload = UploadForm(request.POST)
        if upload.is_valid():
            storage = shelve.open('storage2')
            obj = Upload()
            obj.url = upload.cleaned_data['url']
            obj.pin = upload.cleaned_data['pin']
            if obj.pin not in storage:
                # obj.save()
                pub_date = datetime.datetime.now()
                save(obj.pin, obj.url, pub_date)
                thanks = 'Thanks!'
                return render(request, 'upload/present.html', {'thanks': thanks})
            else:
                current_date = datetime.datetime.now()
                for url in storage[obj.pin]:
                    url = url
                date = storage[obj.pin][url]
                days_passed = abs((current_date - date).days)
                if days_passed > 7:
                    save(obj.pin, obj.url, current_date)
                    thanks = 'Thanks'
                    return render(request, 'upload/present.html', {'thanks': thanks})
                else:
                    return HttpResponse('This pin is already used.')
    else:
        upload = UploadForm()

    return render(request, 'upload/upload.html', {'upload': upload})


def present(request):
    if request.method == 'POST':
        presentpin = PresentForm(request.POST)
        if presentpin.is_valid():
            pin = presentpin.cleaned_data['pin']
            storage = shelve.open('storage2')
            try:
                for url in storage[pin]:
                    edit = '/edit'
                    if edit in url:
                        url = url.replace('/edit', '/present')
                    elif edit not in url:
                        url = url
                    return render(request, 'upload/redirect.html', {'url': url})
            except KeyError:
                wrong = "Incorrect kode. Please try again."
                return render(request, 'upload/present.html', {'wrong': wrong})
            # return render(request, 'upload/redirect.html', {'url': url})
        else:
            return HttpResponse('Not a valid pin.')

    return render(request, 'upload/present.html')
