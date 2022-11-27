from django.http import HttpResponse
import PyPDF2
from . import env
from . import requests
from PyPDF2 import PdfFileReader 
from PyPDF2 import PdfFileMerger
from django.shortcuts import render
from django.conf import settings
import os


def get_references(file):
    print("Hello there\n", file.name)