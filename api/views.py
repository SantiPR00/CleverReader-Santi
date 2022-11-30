from django.http import HttpResponse
from api import reference

def consume_file(request):
    if request.method == 'POST':
        print(request.FILES['file'])
        file = request.FILES['file']
        extension = request.FILES['file'].name.split(".")
        extension[1] != "pdf"
        extension = ["sample", "pdf"]
        if(extension[1] != "pdf"):
            return HttpResponse.status_code == 400
        else:
            return reference.get_references(file)
    