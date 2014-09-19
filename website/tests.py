from django.test import TestCase

from website.models import WebPage

class WebsiteMethodTests(TestCase):

    def test_splash_page_exists(self):
        """
        There should be an active splash page defined
        """
#        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
#        self.assertEqual(future_poll.was_published_recently(), False)
        page_set = WebPage.objects.filter(PageCategory__CategoryName='splash')
#        z = page_set.all()[0]
#        self.assertTrue(page_set.exists(),msg="wtf %s"%z)
        self.assertTrue(page_set)


#####        
#            page_set = WebPage.objects.filter(PageCategory__CategoryName='splash')
#
#    try:
#        assert(page_set)
#    except:
#        raise Http404
#
#    page = page_set.all()[0]
#    context = {'webpage': page}
#    return render(request, 'website/splash.html', context)
#