from django.shortcuts import  render, redirect
from .models import Question
from django.core.paginator import Paginator
import csv, io
from django.contrib import messages
from django.db import IntegrityError


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



def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
            return redirect('upload_csv')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string)

        for row in reader:
             

            try:
                question = Question(
                    question_text=row['Question'],
                    answer_text=row['Correct Answer']
                )
                question.save()
            except IntegrityError:
                # Se uma entrada duplicada causar uma IntegrityError, ignore-a e continue
                print(f"Duplicated entry skipped for question: {row['Question']}")
                continue


        
        messages.success(request, 'CSV file has been successfully processed.')
        return redirect('upload_csv')
    else:
        return render(request, 'upload_csv.html')