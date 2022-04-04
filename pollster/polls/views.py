from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice

# GET QUESTIONS AND DISPLAY THEM

# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list':latest_question_list}
#     return render(request, 'polls/index.html', context)

## Generic View Format
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name='latest_question_list'

    def get_queryset(self):
        #Return the last five published questions (not including those set to be published in the future).
       return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



# SHOW SPECIFIC QUESTION AND CHOICES

# def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")    
    # return render(request, 'polls/detail.html', {'question': question})    

## Generic View Format
class DetailView(generic.DetailView):
    model = Question
    template_name='polls/detail.html'
   

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# GET QUESTION AND DISPLAY RESULTS 

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html',{'question': question})

## Generic View Format
class ResultView(generic.DetailView):
    model = Question
    template_name='polls/results.html'


# VOTE FOR A QUESTION CHOICE

def vote(request, question_id):
    # print(request.POST['choice'])
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






# "question_id" comes from 'url.py' file. Unlike Express.js, where we have to get parameters in routes, using "req.params", Django handles that for us. 
# For example, if we use Postman to test route "http://localhost:8000/polls/1/vote", on getting to 'url.py', it hits path '<int:question_id>/vote/', Django automatically
  # structures out '1' as 'question_id', and sends it to 'views.py'.
# 'request' is automatically sent from 'url.py' just like 'req and res' in Node.
# Guessing 'raise Http404("Question does not exist")' is similar to Node's 'res.status(404)'

# FOR vote view, NOTE the following:
  # 1. The 'else' isn't necessary, take it off and align the items under it properly, and we get same result.
  # 2. We could as well place the items under 'else', under 'try', we get same result.

## CHANGING VIEWS (index,detail and results) TO DJANGO'S GENERIC VIEWS [https://docs.djangoproject.com/en/3.2/intro/tutorial04/]  
#  1.Convert the URLconf.
#  2.Delete some of the old, unneeded views.
#  3.Introduce new views based on Django’s generic views.

"""So, how exactly does Django's Generic Views work???
 [https://docs.djangoproject.com/en/3.2/intro/tutorial04/] 
        " The detail() and results() views are very short – and, as mentioned above, redundant. The index() view, which displays a list of polls, is similar.
            These views represent a common case of basic Web development: getting data from the database according to a parameter passed in the URL, loading a template and returning the rendered template. 
            Because this is so common, Django provides a shortcut, called the “generic views” system.
            Generic views abstract common patterns to the point where you don’t even need to write Python code to write an app. " - From the docs

Firstly, we have to make changes to the URLconfig file (polls.urls.py)
  e.g   |path('', views.index, name='index')|    becomes    |path('', views.IndexView.as_view(), name='index')|
        |path('<int:question_id>/', views.detail, name='detail')|  becomes  |path('<int:pk>/', views.DetailView.as_view(), name='detail')|
 
Secondly, We amend the views in (polls.views.py), converting the old format to Django's Generic Views format, as done above.
  - We’re using two generic views here: ListView and DetailView. Respectively, those two views abstract the concepts of “display a list of objects” and “display a detail page for a particular 
  type of object.
  - The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views (polls.urls.py).


How it works (In summary)
 - When a path in (polls.urls.py) is matched, say, |path('<int:pk>/', views.DetailView.as_view(), name='detail')|, class Detailview  (which is a view in [polls.views.py] and which extends class
   generic.DetailView ) is called/fired. Django then uses the matched primary key(pk) to find the particular question in scope (using model = Question) and sends the question object down to the specified template.
 - For ListView, the 'get_queryset' function specifies the model to be used. "context_object_name" is used to rename the context variable to match what we have in our template (it's used to override the default provided by Django).
"""