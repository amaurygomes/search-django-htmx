from django.shortcuts import render, redirect
from .models import Question
from django.views.decorators.http import require_POST
import csv, io
from django.contrib import messages

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
    if not Question.objects.filter(question_text=question).exists():
       new_question = Question(question_text=question, answer_text=answer)
       new_question.save()
       return render(request, 'htmx_components/success_add.html')
    else:
        return render(request, 'htmx_components/error_add.html')


@require_POST
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
            if 'Question' not in row or 'Correct Answer' not in row:
                messages.error(request, 'O arquivo CSV não contém as colunas necessárias.')
                return redirect('upload_csv')
            question_text = row['Question']
            answer_text = row['Correct Answer']           
            if not Question.objects.filter(question_text=question_text).exists():            
                question = Question(
                    question_text=question_text,
                    answer_text=answer_text
                )
                question.save()
            else:                
                print(f"Question '{question_text}' already exists, skipping...")
        return render(request, 'htmx_components/success_import.html')
    else:
        return render(request, 'htmx_components/success_import.html')
    
