from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Não há na tabela Question id com esse número! \nCrie mais Questions em Question.")
    context = {"question" : question}
    return render(request, "polls/detail.html", context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question": question, "error_message": "Você não selecionou uma escolha."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", kwargs={'question_id': question.id}))

def results(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request,"polls/results.html", {"question": question})