from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Job Listing API</h1>")

def api_root(request):
    return JsonResponse({"message": "Welcome to the API. Use /jobs/ to access job data."})

urlpatterns = [
    path('', home, name='home'),            # Root URL
    path('api/', api_root, name='api-root'), # API Root URL
    path('api/jobs/', include('jobs.urls')), # Include jobs app URLs
    path('admin/', admin.site.urls),         # Admin panel
]
