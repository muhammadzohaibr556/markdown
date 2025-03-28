"""
URL configuration for markdown project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from documents.views import DocumentListView, DocumentCreateView, DocumentDetailView, DocumentUpdateView, \
    DocumentDeleteView, LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/users/login/', LoginView.as_view(), name='user-login'),

    path('api/documents/', DocumentListView.as_view(), name='document-list'),
    path('api/documents/', DocumentCreateView.as_view(), name='document-create'),
    path('api/documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('api/documents/<int:pk>/', DocumentUpdateView.as_view(), name='document-update'),
    path('api/documents/<int:pk>/', DocumentDeleteView.as_view(), name='document-delete'),
]



