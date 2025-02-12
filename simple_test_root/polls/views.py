from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from pages.models import Page


from pages.models import Page

# View for listing the latest questions on the index page
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context


# View for displaying details of a specific question
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# View for displaying results of a specific question after voting
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# View for handling user votes on a question
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