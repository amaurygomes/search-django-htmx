import csv


csv_file_path = 'Programação_Aplicada_Redes.csv'


modified_csv_file_path = 'redes_out.csv'

def remove_correct_prefix(csv_input_path, csv_output_path):
    with open(csv_input_path, mode='r', encoding='utf-8') as csvfile, \
         open(csv_output_path, mode='w', encoding='utf-8', newline='') as modified_csvfile:
        
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(modified_csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in reader:
            # Remove o prefixo 'Correta:' se estiver presente na coluna 'Correct Answer'
            if row['Correct Answer'].startswith('Correta:'):
                row['Correct Answer'] = row['Correct Answer'][9:]  # Remove os primeiros 9 caracteres 'Correta:'
            writer.writerow(row)

remove_correct_prefix(csv_file_path, modified_csv_file_path)

print("As respostas com o prefixo 'Correta:' foram modificadas no arquivo CSV.")
