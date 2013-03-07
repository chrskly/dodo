from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dodo.views.home', name='home'),
    # url(r'^dodo/', include('dodo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.view_tasks'),
    url(r'^add-task/', 'web.views.add_task'),
    url(r'^complete-task/', 'web.views.complete_task'),
)
