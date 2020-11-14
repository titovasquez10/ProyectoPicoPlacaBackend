from django.conf.urls import url
from PicoplacaApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^ciudades/$',views.ciudadApi),
    url(r'^ciudades/([0-9]+)$',views.ciudadApi),

    url(r'^picoplaca/$',views.picoplacaApi),
    url(r'^picoplaca/([0-9]+)$',views.picoplacaApi),

    url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)