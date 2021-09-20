from django.http import HttpResponse
import json
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request):
    w = ['fwfw']
    q = json.dumps(w)
    print(q)
    return HttpResponse(q)









