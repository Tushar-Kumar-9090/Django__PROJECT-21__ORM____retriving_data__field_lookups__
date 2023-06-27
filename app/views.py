from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *
from django.db.models.functions import *
from django.db.models import Q


## Retrieving the data of Topic
def display_topics(request):

    topic=Topic.objects.all()
    topic=Topic.objects.filter(topic_name='wwe')
    ## topic=Topic.objects.get(topic_name='wwe')        it will showing error in HTML page//FE page
    topic=Topic.objects.all()

    d={'topics':topic}
    return render(request,'display_topics.html',d)




## Retrieving the data of Webpage
def display_webpages(request):
    webpage=Webpage.objects.all()

    webpage=Webpage.objects.filter(url__startswith='https')
    webpage=Webpage.objects.filter(url__endswith='in')
    webpage=Webpage.objects.filter(name__contains='t')

    webpage=Webpage.objects.filter(name__in=['tushar','undertaker'])
    webpage=Webpage.objects.filter(name__regex='u\w+')
    webpage=Webpage.objects.all()

    webpage=Webpage.objects.filter(Q(name='virat') | Q(url__startswith='https'))
    webpage=Webpage.objects.filter(Q(name='tushar') | Q(url__endswith='in'))
    webpage=Webpage.objects.filter(Q(name='virat') & Q(url__startswith='http'))

    webpage=Webpage.objects.all()

    d={'webpages':webpage}
    return render(request,'display_webpages.html',d)





## Retrieving the data of Access_records
def display_accessrecords(request):

    accessrecord = AccessRecord.objects.all()

    accessrecord = AccessRecord.objects.filter(date='2013-06-17')
    accessrecord = AccessRecord.objects.filter(date__gt='2013-06-17')
    accessrecord = AccessRecord.objects.filter(date__lte='2016-06-17')
    accessrecord = AccessRecord.objects.filter(date__year='2010')
    accessrecord = AccessRecord.objects.filter(date__month='06')
    accessrecord = AccessRecord.objects.filter(date__day='10')
    accessrecord = AccessRecord.objects.filter(date__year__gte='2020')
    accessrecord = AccessRecord.objects.filter(date__year__lte='2020')
    accessrecord = AccessRecord.objects.filter(date__day__gt='17')
    

    d={'accessrecords':accessrecord}
    return render(request,'display_access_records.html',d)





def display_all(request):

    topic=Topic.objects.all()
    webpage=Webpage.objects.all()
    accessrecord=AccessRecord.objects.all()

    d={'topics':topic, 'webpages':webpage, 'accessrecords':accessrecord}

    return render(request,'display_all.html',d)









