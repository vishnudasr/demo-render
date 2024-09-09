from django.contrib import admin
from django.urls import path, include
from myapp.views import home  # Import the home view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('myapp.urls')),  # Include myapp URLs
    path('', home, name='home'),  # Map the root URL to the home view
]

urlpatterns +=staticfiles_urlpatterns()