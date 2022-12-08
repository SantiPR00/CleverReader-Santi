import json

from django.http import HttpResponse

import PyPDF2
from refextract import extract_references_from_url

from api import table_parser as tp
from api import image_parser as ip


def consume_file(request):
    if request.method == 'POST':
        file = request.FILES['file'].file
        pdfFileReader = PyPDF2.PdfFileReader(file)
        numOfPages = pdfFileReader.numPages
        tp.table_parser(file, numOfPages)
        ip.image_parser(file, numOfPages)
        references = extract_references_from_url("http://localhost:8080/api/v1/file/2")
        return HttpResponse(json.dumps(references))


