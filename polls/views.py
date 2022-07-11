from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, User, Choice

def index(request):
    
    latest_question_list = Question.objects.all()
    answear_list = Choice.objects.all()
    context = {'latest_question_list': latest_question_list, 'answear_list': answear_list}

    points = 0
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in answear_list:
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.votes += 1
                    if item.correct == True:
                        points += 1
                item.save()
            print("Points" + str(points))
        return HttpResponse("Your score: " + str(points))

    return render(request, 'polls/index.html', context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def users(request):
    user_list = User.objects.all
    return render(request, 'polls/users.html', {'user_list': user_list})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
