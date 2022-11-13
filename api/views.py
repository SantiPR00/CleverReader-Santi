def consume_file(request):
    if request.method == 'POST':
        print(request.FILES['file'])
