from django.http import HttpResponse
import PyPDF2
from . import env
from . import requests
from PyPDF2 import PdfFileReader 
from PyPDF2 import PdfFileMerger
from django.shortcuts import render
from django.conf import settings
import os
from api import reference

def consume_file(request):
    if request.method == 'POST':
        print(request.FILES['file'])
        reference.get_references(request.FILES['file'])
        return HttpResponse(request.FILES['file'].name)
    extension = request.FILES['file'].name.split(".")
    extension[1] != "pdf"
    extension = ["sample", "pdf"]
    if(extension[1] != "pdf"):
        return HttpResponse.status_code == 400