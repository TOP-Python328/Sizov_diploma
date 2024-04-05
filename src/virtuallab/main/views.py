from django.shortcuts import render

from laboratories.forms import AddLaboratoryForm
from laboratories.models import Laboratory, Task
from users.forms import AddGroupForm
from users.models import Group, Teacher

def main(request):
    return render(
        request,
        'main.html',
    )


def administration(request):
    if request.method == 'GET':
        form1 = AddLaboratoryForm()
        form2 = AddGroupForm()
    
    elif request.method == 'POST':
        if request.POST['form'] == 'add_group':
            form = AddGroupForm(request.POST)
            if form.is_valid():
                form.save()
                form2 = AddGroupForm()
        
    return render(
        request,
        'administration.html',
        {
            'form1': form1,
            'form2': form2,
            'laboratories': Laboratory.objects.all(),
            'groups': Group.objects.order_by('teacher'),
            'tasks': Task.objects.order_by('laboratory'),
            'teachers': Teacher.objects.all(),
        }
    )