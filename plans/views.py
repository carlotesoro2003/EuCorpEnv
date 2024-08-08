from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import KeyAreas
from leads.models import Lead
from departments.models import DepartmentHeads
from .models import StrategicGoals, KeyAreas, StrategicObjectives, ActionPlans
from .forms import StrategicGoalForm
from django.contrib import messages
from django.db import transaction


# Create your views here.

##Admin View

@login_required(login_url='authentication/login')
def index(request):  
    if request.user.is_superuser: 
        strategicGoals = StrategicGoals.objects.all()
        context = {
            'strategicGoals': strategicGoals
        }
        return render(request, 'plans/indexAdmin.html', context)
    else:
        user = request.user 
        try:
            departmentHead = DepartmentHeads.objects.get(head=user)
            strategicGoals = StrategicGoals.objects.filter(members=departmentHead)
        except DepartmentHeads.DoesNotExist:
            strategicGoals = []

        context = {
            'departmentHead': departmentHead,
            'strategicGoals': strategicGoals
        }

        return render(request, 'plans/index.html', context)



@login_required(login_url='authentication/login')
def addPlan(request):
    return render(request, 'plans/addPlans.html')

@login_required(login_url='authentication/login')
def addStratGoal(request):
    if request.method == 'POST':
        form = StrategicGoalForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    strategic_goal = form.save(commit=False)
    
                    strategic_goal.save()
                    form.save_m2m() 

                    messages.success(request, 'Strategic Goal added successfully!')
                    return redirect('plans')  
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StrategicGoalForm()

    context = {
        'form': form,
    }
    return render(request, 'plans/addStratGoals.html', context)

@login_required(login_url='authentication/login')
def getKeyArea(request):
    keyAreas = KeyAreas.objects.all()
    context = {
        'keyAreas' : keyAreas,
    }
    return render(request, 'plans/keyAreas.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import StrategicGoals

@login_required(login_url='authentication/login')
def getStratGoal(request, id):
    try:
        strategicGoal = get_object_or_404(StrategicGoals, pk=id)
        objectives = StrategicObjectives.objects.filter(goal_id=strategicGoal)
        
        context = {
            'strategicGoal': strategicGoal,
            'objectives' : objectives
        }
        
        return render(request, 'plans/strategicGoal.html', context)
    
    except StrategicGoals.DoesNotExist:
        messages.error(request, "Strategic Goal not found.")
        return redirect('plans') 

@login_required(login_url='authentication/login')
def deleteStratGoal(request, id):
    strategicGoal = StrategicGoals.objects.get(pk=id)
    strategicGoal.delete()
    messages.success(request, "Strategic Goal removed successfully")
    return redirect('plans')

@login_required(login_url='authentication/login')
def createStratObjectives(request, goal_id):
    strategicGoal = get_object_or_404(StrategicGoals, pk=goal_id)

    if request.method == 'POST':
        try:
            with transaction.atomic():
                strategic_objectives = request.POST.get('strategicObjectives', '').strip()
                kpi = request.POST.get('kpi', '').strip()
                target = request.POST.get('target', '').strip()
                eval_measures = request.POST.get('evalMeasures', '').strip()

                StrategicObjectives.objects.create(
                    goal_id=strategicGoal,  
                    strategicObjectives=strategic_objectives,
                    kpi=kpi,
                    target=target,
                    evalMeasures=eval_measures
                )

                messages.success(request, 'Strategic Objective created successfully!')
                return redirect('strategicGoal', id=goal_id) 

        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('strategicGoal', id=goal_id)

    return render(request, 'plans/strategicGoal.html', {'strategicGoal': strategicGoal})

@login_required(login_url='authentication/login')
def deleteStratObjective(request, id):
    try:
        objective = get_object_or_404(StrategicObjectives, pk=id)
        objective.delete()
        messages.success(request, 'Strategic Objective deleted successfully.')
    except Exception as e:
        messages.error(request, f'An error occurred: {e}')

    return redirect('strategicGoal', id=objective.goal_id.pk)



##Department View
@login_required(login_url='authentication/login')
def createActionPlans(request, goal_id):
    strategicGoal = get_object_or_404(StrategicGoals, pk=goal_id)

    strategicObjectives = StrategicObjectives.objects.filter(goal_id=strategicGoal)

    context = {
        'strategicGoal': strategicGoal,
        'strategicObjectives': strategicObjectives
    }
    return render(request, 'plans/actionPlans.html', context)


@login_required(login_url="authentication/login")
def addActionPlans(request, objective_id, goal_id):
    strategicGoal = get_object_or_404(StrategicGoals, pk=goal_id)
    strategicObjective = get_object_or_404(StrategicObjectives, pk=objective_id, goal_id=strategicGoal)

    if request.method == 'POST':
        action_plan = request.POST.get('actionPlan')
        kpi = request.POST.get('kpi')
        target_output = request.POST.get('targetOutput')
        person_responsible = request.POST.get('personResponsible')
        budget = request.POST.get('budget')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        ActionPlans.objects.create(
            objective_id=strategicObjective,
            actionPlan=action_plan,
            kpi=kpi,
            targetOutput=target_output,
            personResponsible=person_responsible,
            budget=budget,
            startDate=start_date,
            endDate=end_date
        )
        return redirect('addActionPlans', objective_id=objective_id, goal_id=goal_id)

    actionPlans = ActionPlans.objects.filter(objective_id=strategicObjective)
    context = {
        'strategicGoal': strategicGoal,
        'objective': strategicObjective,
        'actionPlans': actionPlans
    }
    return render(request, 'plans/addActionPlans.html', context)

@login_required(login_url='authentication/login')
def deleteActionPlan(request, plan_id, goal_id, objective_id):
    try:
        plan = get_object_or_404(ActionPlans, pk=plan_id)
        plan.delete()
        messages.success(request, 'plan deleted successfully')
    except Exception as e:
        messages.error(request, f'an error occured : {e}')
    
    return redirect('addActionPlans', goal_id=goal_id, objective_id=objective_id)

@login_required(login_url='authentication/login')
def getAllActionPlans(request,goal_id, objective_id ):
    strategicGoal = get_object_or_404(StrategicGoals, pk=goal_id)
    strategicObjective = get_object_or_404(StrategicObjectives, pk=objective_id, goal_id=strategicGoal)
    actionPlans = ActionPlans.objects.filter(objective_id=strategicObjective)

    context = {
        'strategicGoal' : strategicGoal,
        'objective' : strategicObjective,
        'actionPlans' : actionPlans
    }

    return render(request, 'plans/allActionPlans.html', context)
