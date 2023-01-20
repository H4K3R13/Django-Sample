from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView
# from django.urls import reverse

from.models import Course


def index(request):
    return HttpResponse("Hello, world. You're at the student index.")


def courses(request):

    #number_of_years = request.GET.get('number_of_years', 5)

    courses_list = Course.objects.all().order_by('-number_of_years')

    # courses_list = Course.objects.filter(number_of_years__lte=number_of_years)

    context = {'courses_list': courses_list}

    return render(request, 'student/courses.html', context)


def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        context = {
            'course': course
        }
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request, 'student/detail.html', context)

from django.urls import reverse

class CourseCreateView(CreateView):
    model = Course
    fields = "__all__"

    def get_success_url(self):
        return reverse('detail', kwargs={'course_id': self.object.pk})