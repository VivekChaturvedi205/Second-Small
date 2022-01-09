from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Upload
from .forms import UploadForm


def header(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = UploadForm()
    q = Upload.objects.all()
    return render(request, 'firstapp/header.html', {'form': form, 'q': q})
