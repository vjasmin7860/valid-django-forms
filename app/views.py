from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}
    if request.method=='POST':
        EFTO=TopicForm(request.POST)
        if EFTO.is_valid():
            topic_name=EFTO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            return HttpResponse('data submitted')
        else:
            return HttpResponse('data is invalid ')
        
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    EFWO=WebpageForm()
    d={'EFWO':EFWO}
    if request.method=='POST':
        EFWO=WebpageForm(request.POST)
        if EFWO.is_valid():
            topic_name=EFWO.cleaned_data['topic_name']
            name=EFWO.cleaned_data['name']
            url=EFWO.cleaned_data['url']
            email=EFWO.cleaned_data['email']

            
            #WO=Webpage.objects.get_or_create(topic_name=topic_name,name=name,url=url,email=email)[0]
            #WO.save()
            return HttpResponse(str(EFWO.cleaned_data))
        else:
            return HttpResponse('data is invalid')
    return render(request,'insert_webpage.html',d)



def insert_access(request):
    EFAO=AccessForm()
    d={'EFAO':EFAO}
    if request.method=='POST':
        EFAO=AccessForm(request.POST)
        if EFAO.is_valid():
            name=EFAO.cleaned_data['name']
            date=EFAO.cleaned_data['date']
            author=EFAO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=name,date=date,author=author)[0]
            AO.save()
            return HttpResponse('accessform is created successfully')
        else:
            return HttpResponse('invalid data')
    
    return render(request,'insert_access.html',d)

