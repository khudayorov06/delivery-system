from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),  # Orders ilovasini asosiy sahifaga bog‘lash
]
