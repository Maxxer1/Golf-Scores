from django.shortcuts import render, redirect
from .models import GolfCourse, Score
from commons.error_messages import ErrorMessage
from .helpers import calculate_score_to_par, format_date
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def golf_courses(request):
    golf_courses = GolfCourse.objects.all().order_by('country')
    if request.method == 'POST':
        if GolfCourse.objects.filter(name=request.POST['name']).exists():
            return render(request, 'golf_courses.html', {'golf_courses': golf_courses, 'error_message': ErrorMessage.COURSE_ALREADY_EXISTS.value})
        golf_course = GolfCourse.objects.create(name=request.POST['name'], city=request.POST[
            'city'], country=request.POST['country'], par=request.POST['par']).save()
        return redirect('/golf_courses')
    return render(request, 'golf_courses.html', {'golf_courses': enumerate(golf_courses, start=1)})

@login_required
def delete_course(request):
    if request.method == 'POST':
        GolfCourse.objects.get(pk=request.POST['id']).delete()
        return redirect('/golf_courses')

@login_required
def scores(request):
    scores = Score.objects.filter(user_score_id=request.user.id).order_by('date').reverse()
    golf_courses = GolfCourse.objects.all()
    if request.method == 'POST':
        golf_course = GolfCourse.objects.filter(
            name=request.POST['golf_course']).first()
        to_par = calculate_score_to_par(int(request.POST['score']), golf_course.par)
        score = Score.objects.create(date=format_date(request.POST[
            'datepicker']), golf_course=golf_course, score=request.POST['score'], to_par=to_par, user_score_id=request.user.id).save()
    return render(request, 'scores.html', {'golf_courses': golf_courses, 'scores': enumerate(scores, start=1)})

@login_required
def delete_score(request):
    if request.method == 'POST':
        Score.objects.get(pk=request.POST['id']).delete()
        return redirect('/scores')