from rest_framework import routers
from rental import views as rental_views

router = routers.DefaultRouter()
router.register(r'friends', rental_views.FriendViewSet)
router.register(r'belongins', rental_views.BelongingViewSet)
router.register(r'borrowings', rental_views.BorrowedViewSet)