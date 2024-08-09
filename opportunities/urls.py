from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="opportunities"),
    path('add-opportunity',views.addOpportunity, name="addOpportunity"),
    path('deleteOpportunity/<int:opportunity_id>/', views.deleteOpportunity, name='deleteOpportunity'),
]