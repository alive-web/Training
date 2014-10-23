from django.http import HttpResponse

from polls.models import Question



def ind(request):
    return HttpResponse("Hello, world. You're at the root index.")

from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)