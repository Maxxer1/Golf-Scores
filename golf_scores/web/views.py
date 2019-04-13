from django.shortcuts import render, redirect
from .models import GolfCourse, Score
from commons.error_messages import ErrorMessage
from .helpers import calculate_score_to_par, format_date


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def golf_courses(request):
    golf_courses = GolfCourse.objects.all()
    if request.method == 'POST':
        form = request.POST
        if GolfCourse.objects.filter(name=form.__getitem__('name')).exists():
            return render(request, 'golf_courses.html', {'golf_courses': golf_courses, 'error_message': ErrorMessage.COURSE_ALREADY_EXISTS.value})
        golf_course = GolfCourse.objects.create(name=form.__getitem__('name'), city=form.__getitem__(
            'city'), country=form.__getitem__('country'), par=form.__getitem__('par')).save()
        return redirect('/golf_courses')
    return render(request, 'golf_courses.html', {'golf_courses': enumerate(golf_courses, start=1)})


def delete_course(request):
    if request.method == 'POST':
        form = request.POST
        GolfCourse.objects.get(pk=form.__getitem__('id')).delete()
        return redirect('/golf_courses')


def scores_view(request):
    scores = Score.objects.all().order_by('date').reverse()
    golf_courses = GolfCourse.objects.all()
    if request.method == 'POST':
        form = request.POST
        golf_course = GolfCourse.objects.filter(
            name=form.__getitem__('golf_course')).first()
        to_par = calculate_score_to_par(int(form.__getitem__('score')), golf_course.par)
        score = Score.objects.create(date=format_date(form.__getitem__(
            'datepicker')), golf_course=golf_course, score=form.__getitem__('score'), to_par=to_par).save()
    return render(request, 'scores.html', {'golf_courses': golf_courses, 'scores': enumerate(scores, start=1)})


def delete_score(request):
    if request.method == 'POST':
        form = request.POST
        Score.objects.get(pk=form.__getitem__('id')).delete()
        return redirect('/scores')