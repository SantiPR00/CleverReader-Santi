from django.http import HttpResponse
from . import env
from . import requests
from PyPDF2 import PdfFileReader 
from PyPDF2 import PdfFileMerger
from django.shortcuts import render
from django.conf import settings
import os

def consume_file(request):
    if request.method == 'POST':
        print(request.FILES['file'])
        return HttpResponse(request.FILES['file'].name)
    
#error handling

def uploadFile(fileFullPath):
    result=False
    
    print ("Attempting to upload file: ") + fileFullPath
    
    headers = {"X-Parse-Application-Id": env.X_Parse_Application_Id,
               "X-Parse-REST-API-Key": env.X_Parse_REST_API_Key,
               "Content-Type": "application/json"}
    try:
        f=open(fileFullPath, 'r')
        files = {'file': f}
        r = requests.post(env.PARSE_HOSTNAME + env.PARSE_FILES_ENDPOINT + "/" + env.PARSE_UPLOADED_FILE_NAME, files=files, headers=headers)
        jsonResult = r.json()
        
        if 'error' in jsonResult:
            print ("An error ocurred while trying to upload the file. Details: " + (jsonResult["error"]))
        else:
            print(jsonResult["name"])
            print(jsonResult["url"])
            
        print ("Completed uploading the file")
        result = True
        
    #Unable to open the file
    except IOError as ex:
        print ('IOError thrown. Details: ' + ' %s') % ex
        
if __name__ == "__main__":
    myFilePath = r'D:/myfile.pdf'
    print (uploadFile(myFilePath))
        
        
#extracting_text.py

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf=PdfFileReader(f)
        
#merging_text.py

def text_merger(path):
    pdf_file1=PdfFileReader("file1.pdf")
    pdf_file2=PdfFileReader("file2.pdf")
    output=PdfFileMerger()
    output.append(pdf_file1)
    output.append(pdf_file2)
    with open("merged.pdf", "wb") as output_stream:
            output.write(output_stream)
            

    