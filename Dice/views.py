from django.shortcuts import render
from .models import*
import pandas as pd
# Create your views here.
def home(request):
    item = Character.objects.all().values()
    df = pd.DataFrame(item)
   
    mydict = {
        "df": df.to_html()
    }
    df.to_excel("output.xlsx")
    return render(request, 'index.html', context=mydict)
# Create your views here.
