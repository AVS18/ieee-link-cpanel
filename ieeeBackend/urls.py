from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
admin.site.site_header = 'IEEE LINK Web Login Panel'                    # default: "Django Administration"
admin.site.index_title = 'Admin Arena'                 # default: "Site administration"
admin.site.site_title = 'IEEE Kerala Section - LINK Team' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('',include('posts.urls'))
]
urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]