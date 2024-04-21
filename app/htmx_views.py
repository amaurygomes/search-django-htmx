from django.shortcuts import render
from .models import Question
from django.views.decorators.http import require_POST

# Views para requisicões HTMX
def search_input(request):

    result = request.GET['search_input']

    if result == "":
       return render(request, 'htmx_components/search_empty.html')
   
    else:
        data = Question.objects.filter(question_text__icontains=result)
        return render(request, 'htmx_components/search_out.html',{'data': data})
    

def search_clear(request):
    pass
    return render(request, 'htmx_components/search_empty.html')
   
@require_POST
def submit_question(request):
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    new_question = Question(question_text=question, answer_text=answer)
    new_question.save()

    return render(request, 'htmx_components/success_add.html')