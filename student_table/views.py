from django.shortcuts import render, redirect
from . models import student
from . forms import studentForm

# Create your views here.
def home(request):
    students = student.objects.all()
    context = {'student_list' : students}
    return render(request, 'student_table/table.html', context)


def addStudent(request):
    form = studentForm()

    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'student_table/add_student.html', context)


def updateStudent(request, pk):
    current_student = student.objects.get(auto_increment_id=pk)
    form = studentForm(instance=current_student)

    if request.method == 'POST':
        form = studentForm(request.POST, instance=current_student)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'student_table/add_student.html', context)


def deleteStudent(request, pk):
    current_student = student.objects.get(auto_increment_id=pk)
    if request.method == 'POST':
        current_student.delete()
        return redirect('home')
    context = {'object' : current_student}
    return render(request, 'student_table/delete-student.html', context)