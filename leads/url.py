from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')  #this is main url root we're going to request api throght
                                                    #we're calling the function we're going to use
                                                    #we will name it leads

urlpatterns = router.urls   #this one is Abbreviation for include(''), so we're going do this
                            #it will give us urls we register for above url 'api/leads' endpoint
                            #beacuse we have CRUD function, instead of making them all, we;re calling the 
                            #router.urls to create it by it's own