from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
#from django.template import RequestContext, loader

from website.models import WebPage
 
 
def newhomepage(request, thisurl):
     
    page = WebPage.objects.filter(Url ='zz')[0]
    z = page.ContentSections.all()
    try:
        assert(page)
    except:
        raise Http404
 
    context = {'page': page, 'name':'shane', 'z':z}
 
    return render(request, 'website/page_homepage.html', context)



def oldhomepage(request):

#    page_set = WebPage.objects.filter(PageCategory__CategoryName='splash')
#
#    try:
#        assert(page_set)
#    except:
#        raise Http404
#
#    page = page_set.all()[0]
    page = 'dummy'
    context = {'webpage': page}
    return render(request, 'website/splash.html', context)

#    template = loader.get_template('website/splash.html')
#    context = RequestContext(request, {'webpage': this_page})
#    return HttpResponse(template.render(context))