from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('refine', 'rs_demo.onepage.refine'),
    url(r'show', 'rs_demo.onepage.show'),
    url(r'^mail$', 'rs_demo.mail_deliver.deliver'),
    url(r'^title$', 'rs_demo.mail_deliver2.deliver'),
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
