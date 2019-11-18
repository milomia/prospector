from django.shortcuts import render
from django.http import HttpResponse
import pdb as pdb_module
from django.template import Library, Node

from prospects.models import Interview   

def home(request):
    interviews = Interview.objects.all()
    return render(request,'home.html',{'interviews': interviews })

def interview_detail(request, id):
    try:
        interview = Interview.objects.get(id=1)
    except Interview.DoesNotExist:
        raise Http404('Interview not found')
    return render(request, 'interview_detail.html', {'interview':interview})
