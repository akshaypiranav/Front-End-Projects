import os
import zipfile
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import zlib


def home(request):
    return render(request,"index.html")


import os
import zipfile
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_path = handle_uploaded_file(file)
        compressed_file_path = compress_file(file_path)
        response = serve_compressed_file(compressed_file_path)
        return response

    return render(request, 'index.html')

def handle_uploaded_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path



def compress_file(file_path):
    compressed_file_path = f"{file_path}.zip"
    with zipfile.ZipFile(compressed_file_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        zipf.write(file_path, os.path.basename(file_path))
    return compressed_file_path

def serve_compressed_file(file_path):
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response