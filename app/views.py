from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def navya(request):
    return HttpResponse('navya is good')

def likitha(request):
    return HttpResponse('liki is sister of navya')




def swathi(request):
    return HttpResponse('swathi is bigsister of navya')



