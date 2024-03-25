# from django.urls import path, include
# from rest_framework import routers
#
# from blog import views
# from blog.views import get_likes, get_comment
#
# router = routers.DefaultRouter()
# router.register(r'users', views.CustomerUserViewSet)
# router.register(r'blog', views.BlogViewSet)
# router.register(r'comment', views.CommentViewSet)
# router.register(r'like', views.LikeViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('like-count/<int:blog_id>/', get_likes, name='like-count'),
#     path('get-comment/', get_comment, name='get_comment'),
# ]

from rest_framework import routers
from django.urls import path, include

from restaurant_app import views

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'restaurant', views.RestaurantViewSet)
router.register(r'food', views.FoodViewSet)
router.register(r'food_comment', views.Food_commentViewSet)
router.register(r'restaurant_comment', views.Restaurant_commentViewSet)
router.register(r'restaurant_location', views.Restaurant_locationViewSet)


urlpatterns = [
    path('', include(router.urls))
]