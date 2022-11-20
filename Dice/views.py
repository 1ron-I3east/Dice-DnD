from django.shortcuts import render
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HTMLtextSerializers
from .models import*
import pandas as pd
import json
# Create your views here.
# class download:
#    def download_file(request):
        # if filename != '':
        #     # Define Django project base directory
        #     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #     # Define the full file path
        #     filepath = BASE_DIR + '/cooldice/' + filename
        #     # Open the file for reading content
        #     path = open(filepath, 'rb')
        #     # Set the mime type
        #     mime_type, _ = mimetypes.guess_type(filepath)
        #     # Set the return value of the HttpResponse
        #     response = HttpResponse(path, content_type=mime_type)
        #     # Set the HTTP header for sending to browser
        #     response['Content-Disposition'] = "attachment; filename=%s" % filename
        #     # Return the response value
        #     return response
        # else:
        #     # Load the template
        # return render(request, 'index2.html')
class main:
    def home(request):
        item = Character.objects.all().values()
        df = pd.DataFrame(item)
    
        mydict = {
            "df": df.to_html()
        }
        df.to_excel("output.xlsx")
        return render(request, 'index.html', context=mydict)

class dice_view(APIView):   
    def get(self, request):
        item = Character.objects.all().values()
        df = pd.DataFrame(item)   
        a = df.to_dict()
        return Response(a)
       
    # Create your views here.
 # result = df.to_json(orient="split")
        # parsed = json.loads(result)
         # {column: values[0] for column, values in df.fillna(0).to_dict().items(orient='list')}
          # df.to_excel("output.xlsx")
        # return render(request, 'index.html', context=mydict), render(request,'index.html', parsed)
        # serializer_for_request = HTMLtextSerializers(instance=parsed)
        # return Response(serializer_for_request.data)
        #         mydict = {
        #     "df": df.to_html()
        # }
        # return render(request, 'index.html', parsed)