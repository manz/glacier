from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from leglacier import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'restaurant.views.home', name='home'),
    url(r'^contact/$', 'restaurant.views.contact', name='contact'),
    url(r'^actualites/$', 'restaurant.views.news', name='news'),
    url(r'^menus/$', 'restaurant.views.menus', name='menus'),
    url(r'^services/$', 'restaurant.views.services', name='services'),
    url(r'^events/(?P<event_id>\d+)?$', 'restaurant.views.edit_event', name="edit_event"),

    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns.append(static(settings.STATIC_URL, document_root='static/'))
