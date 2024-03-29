"""
URL configuration for SustainableSipsApis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title="sustainable sips API")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/products/", include("Product.urls") ),
    path("api/user/", include("Users.urls") ),
    path("api/sales/", include("Sale.urls") ),
    path("api/common/", include("Common.urls")),
    # path('api/schema/docs', schema_view),

]+ static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
