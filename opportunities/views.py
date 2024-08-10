from django.shortcuts import render, redirect, get_object_or_404
from departments.models import DepartmentHeads
from django.contrib import messages
from .models import Opportunities


# Create your views here.
def index(request):
    if request.user.is_superuser:
        # Get all department heads
        heads = DepartmentHeads.objects.all()
        
        # Create a list of dictionaries containing department, the count of opportunities, and head ID
        department_opportunity_counts = []
        for head in heads:
            opportunity_count = Opportunities.objects.filter(head=head).count()
            department_opportunity_counts.append({
                'department': head.department,
                'count': opportunity_count,
                'head_id': head.id  # Include the head ID for URL linking
            })
        
        context = {
            'department_opportunity_counts': department_opportunity_counts
        }
        return render(request, 'opportunities/indexAdmin.html', context)
    else:
        return render(request, 'opportunities/index.html')



def addOpportunity(request):
    currentUser = request.user
    try:
        departmentHead = DepartmentHeads.objects.get(head=currentUser)
    except DepartmentHeads.DoesNotExist:
        messages.error(request, 'No department head found')
        return render(request, 'opportunities/department/addOpportunity.html')

    if request.method == 'POST':
        opportunityStatement = request.POST.get('opportunityStatement')
        plannedActions = request.POST.get('plannedActions')
        kpi = request.POST.get('kpi')
        keyPersons = request.POST.get('keyPersons')
        targetOutput = request.POST.get('targetOutput')
        budget = request.POST.get('budget')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        Opportunities.objects.create(
            head = departmentHead,
            statement = opportunityStatement,
            plannedActions = plannedActions,
            kpi = kpi,
            keyPersons = keyPersons,
            targetOutput = targetOutput,
            budget = budget,
            startDate = startDate,
            endDate = endDate,
        )
        return redirect('addOpportunity')
    
    opportunities = Opportunities.objects.filter(head=departmentHead)
    context= {
        'opportunities' : opportunities
    }

    return render(request, 'opportunities/department/addOpportunity.html', context)

def deleteOpportunity(request, opportunity_id):
    try:
        opportunity = get_object_or_404(Opportunities, pk=opportunity_id)
        opportunity.delete()
        messages.success(request, 'Opportunity deleted successfully!')
    except Exception as e:
        messages.error(request, f'An error occurred: {e}')

    return redirect('addOpportunity')  # Redirect to the list view

def getOpportunitiesbyHead(request, id):
    head = get_object_or_404(DepartmentHeads, pk=id)
    opportunities = Opportunities.objects.filter(head=head)

    context = {
        'head': head,
        'opportunities': opportunities
    }

    return render(request, 'opportunities/admin/allOpportunities.html', context)