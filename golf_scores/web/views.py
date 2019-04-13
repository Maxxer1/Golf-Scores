from django.shortcuts import render, redirect
from .models import GolfCourse
from commons.error_messages import ErrorMessage

# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def golf_courses(request):
    golf_courses = GolfCourse.objects.all().values()
    if request.method == 'POST':
        form = request.POST
        if GolfCourse.objects.filter(name=form.__getitem__('name')).exists():
            return render(request, 'golf_courses.html', {'courses': golf_courses, 'error_message': ErrorMessage.COURSE_ALREADY_EXISTS.value})
        golf_course = GolfCourse.objects.create(name=form.__getitem__('name'), city=form.__getitem__(
            'city'), country=form.__getitem__('country'), par=form.__getitem__('par'))
        golf_course.save()
        return redirect('/golf_courses')
    return render(request, 'golf_courses.html', {'courses': golf_courses})


def delete_course(request):
    if request.method == 'POST':
        form = request.POST
        golf_course = GolfCourse.objects.get(name=form.__getitem__('name'))
        golf_course.delete()
        return redirect('/golf_courses')
