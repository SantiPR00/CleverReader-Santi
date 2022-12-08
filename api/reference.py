import PyPDF2
import re
import json
from django.http import HttpResponse

def get_references(file):
    doc = PyPDF2.PdfFileReader(file)
    pages = doc.getNumPages()

    extracted_text = ""

    # Get each page and extract text
    for i in range(pages):
        curr_page = doc.getPage(i)
        curr_text = curr_page.extractText()
        extracted_text += curr_text

    # Search for references part
    tmp = extracted_text.split("References")[1].strip()
    
    references = ""

    # Remove all newline(\n) characters between lowercase letters
    for i in range(0, len(tmp)):
        if tmp[i] == '\n':
            if ((tmp[i-1].islower() & tmp[i+1].islower()) or not tmp[i-1].isalnum() or (tmp[i-1].islower() & tmp[i+1].isupper()) or (tmp[i-1].isalnum() & tmp[i+1].isnumeric()) ):
                tmp = tmp[:i] + " " + tmp[i+1:]
        references += tmp[i]
    
    ref_list = references.split("\n")

    # Convert references array to json
    ref_json = json.dumps(ref_list)

    return HttpResponse(ref_json)