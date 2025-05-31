"""
URL configuration for DeliveryDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from DeliveryDjango import views
from DeliveryDjango.views import orders_chart_data, restaurants_rating_data, review_ratings_chart_data, \
    restaurant_list_view, restaurant_review_stats

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from DeliveryDjango import views
#from DeliveryDjango.views import orders_chart_data, restaurants_rating_data, review_ratings_chart_data, restaurant_list_view, all_restaurants_review_stats, export_reviews_view

from DeliveryDjango.views import (
    orders_chart_data, restaurants_rating_data, review_ratings_chart_data,
    restaurant_list_view, restaurant_review_stats, all_restaurants_review_stats,
    export_reviews_view, export_reviews_to_excel, restaurants_with_reviews_stats, orders_by_restaurant_stats, review_counts_by_restaurant, top_restaurants_by_reviews  # Добавьте этот импорт
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.menu_restaurant, name='restaurant_menu'),
    path('dish_detail/<int:pk>/', views.DishDetail.as_view(), name='dish_detail_page'),
    path('add_to_cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('order/', views.order, name='order'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('logout', auth_views.LogoutView.as_view(next_page='restaurant_list'), name='logout'),
    path('user_orders/', views.user_orders, name='user_orders'),
    path('rate_order/<int:order_id>/', views.rate_order, name='rate_order'),
    path('api/orders-chart-data/', orders_chart_data, name='orders_chart_data'),
    path('api/restaurants-rating-data/', restaurants_rating_data, name='restaurants_rating_data'),
    path('restaurant_list/', restaurant_list_view, name='restaurant_list_view'),
    path('api/review-ratings-chart-data/<int:restaurant_id>/', review_ratings_chart_data, name='review_ratings_chart_data'),
    path('api/review-chart-data/<int:restaurant_id>/', restaurant_review_stats, name='review_chart_data'),
    path('admin/export_reviews/', export_reviews_view, name='export_reviews_view'),
    path('export/reviews/', export_reviews_to_excel, name='export_reviews_to_excel'),  # Убедитесь, что этот путь правильный
    path('api/all-restaurants-review-stats/', all_restaurants_review_stats, name='review_chart_data'),
    path('api/restaurants-with-reviews-stats/', restaurants_with_reviews_stats, name='restaurants_with_reviews_stats'),
    path('api/orders-by-restaurant-stats/', orders_by_restaurant_stats, name='orders_by_restaurant_stats'),
    path('api/review-counts-by-restaurant/<int:restaurant_id>/', review_counts_by_restaurant, name='review_counts_by_restaurant'),
    path('api/top-restaurants-by-reviews/', top_restaurants_by_reviews, name='top_restaurants_by_reviews'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
