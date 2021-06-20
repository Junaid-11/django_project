from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *


router=SimpleRouter()

router.register('profile',ProfileView)
router.register('product',ProductView)


urlpatterns=router.urls
