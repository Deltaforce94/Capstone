# Project for Meta Back End Developer Course
user: admin1
password: m3cv%U%mf^S>uM+

paths: 
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('restaurant.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/menu/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
