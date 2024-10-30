"""paper_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from paper_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paper_types/', views.get_paper_types),     # 前端接口，查看前端数据
    path('get_chart_types/', views.get_chart_types, name='get_chart_types'),
    path('chart_types/<str:paper_type>/', views.get_chart_types_by_paper_type, name='get_chart_types_by_paper_type'),
    path('entries/', views.get_entries, name='get-entries'),
    path('entries_types/<str:paper_type>/', views.get_entries_by_paper_type, name='get_entries_by_paper_type'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
