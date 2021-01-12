"""myproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from pharmacy import views
urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('eadd', views.eadd),
    path('eshow', views.eshow),
    path('pedit/<int:id>', views.pedit),
    path('pupdate/<int:id>', views.pupdate),
    path('pdelete/<int:id>', views.pdestroy),
    path('padd', views.padd),
    path('pshow', views.pshow),
    path('madd', views.madd),
    path('mshow', views.mshow),
    path('medit/<int:id>', views.medit),
    path('mupdate/<int:id>', views.mupdate),
    path('mdelete/<int:id>', views.mdestroy),
    path('index',views.index),
    path('mshowy',views.mshowy),
    path('mshowm',views.mshowm),
    path('mshowd',views.mshowd)

]
