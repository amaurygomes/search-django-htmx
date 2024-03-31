from django.shortcuts import render
from .models import Question

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
   
   