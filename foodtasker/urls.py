from django.conf.urls import url, include
from django.contrib import admin
from foodtaskerapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    # Restaurnat
    url(r'^restaurant/sign-in/$', LoginView.as_view(),
        {'template_name': 'restaurant/sign_in.html'},
        name= 'restaurant-sign-in'),
    url(r'^restaurant/sign-out', LogoutView.as_view(),
        {'next_page': '/' },
        name= 'restaurant-sign-out'),
    url(r'^restaurant/sign-up', views.restaurant_sign_up,
            name= 'restaurant-sign-up'),
    url(r'^restaurant/$', views.restaurant_home, name= 'restaurant-home'),

    # Sing In/ Sign Up/ Sign Out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert token (sign in/ sign up)
    # /revoke token (sign out)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
