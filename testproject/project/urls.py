from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin


urlpatterns = i18n_patterns(
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^',
        include('cms.urls')
    ),
)


# When running debug/devserver let django deliver static and media files
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
