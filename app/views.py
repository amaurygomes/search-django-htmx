from django.shortcuts import  render, redirect
from .models import Question
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def about(request):
    return render(request, 'about.html')


def questions_add(request):    
    return render(request, 'questions_add.html')

def list_questions(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 10) 
    page_number = request.GET.get('page')
    questions = paginator.get_page(page_number)

    return render(request, 'list_questions.html', {'questions': questions})


def delete_question(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return redirect('list_questions')  