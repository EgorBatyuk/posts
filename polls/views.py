from django.http import HttpResponse
import json
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    output = ', '.join([q.question_text for q in latest_question_list])
    q = json.dumps(output)
    return HttpResponse([q])


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request):
    w = 1
    t = 778
    q = json.dumps(w)
    print(q)










