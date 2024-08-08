from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="plans"),
    path('add-plans', views.addPlan, name="add-plans"),
    path('add-strat-goals',views.addStratGoal, name="addStratGoals"),
    path('key-areas',views.getKeyArea,name="keyAreas"),
    path('strategicGoal/<int:id>/', views.getStratGoal, name='strategicGoal'),
    path('deleteStratGoal/<int:id>/', views.deleteStratGoal, name='deleteStratGoal'),
    path('createObjectives/<int:goal_id>/', views.createStratObjectives, name='createObjectives'),
    path('deleteObjective/<int:id>/', views.deleteStratObjective, name="deleteStratObjective"),
    path('actionPlans/<int:goal_id>/', views.createActionPlans, name='actionPlans'),
    path('addActionPlans/<int:goal_id>/<int:objective_id>/', views.addActionPlans, name='addActionPlans'),
    path('deleteActionPlan/<int:plan_id>/<int:goal_id>/<int:objective_id>/', views.deleteActionPlan, name='deleteActionPlan'),
    path('allActionPlans/<int:goal_id>/<int:objective_id>/', views.getAllActionPlans, name='allActionPlans')
]