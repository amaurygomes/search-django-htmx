import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import Question  

def import_csv_to_model(csv_file_path):
  
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            
            question = Question(
                question_text=row['Question'],
                answer_text=row['Correct Answer']
            )
            
            question.save()


csv_file_path = 'redes_out.csv'
import_csv_to_model(csv_file_path)

print("Dados importados com sucesso do arquivo CSV para o modelo Question.")
