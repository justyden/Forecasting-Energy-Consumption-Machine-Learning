from django.shortcuts import render

def home(request):
    """View function for the home page."""
    return render(request, 'consumption_forecast/home.html')

def help(request):
    """View function for the help page."""
    return render(request, 'consumption_forecast/help.html')

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        # Process the uploaded CSV file here
        # Example: Save the file to a specific location
        with open('uploaded_files/' + csv_file.name, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')