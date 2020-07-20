from django.urls import path
from .views import SubscriberViewSet

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("article", SubscriberViewSet)

urlpatterns = router.urls

