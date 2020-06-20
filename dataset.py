import csv

# a) Obtención de datos
new_dataset = []
with open('./data/positivos_covid.csv', encoding='latin') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  first_line = True
  for row in csv_reader:
    if first_line:
      first_line = False
      continue
    # b) Limpieza de datos: purgando datos
    if row[1] == 'CUSCO':
      edad = int(row[5])
      rango_edad = ''
      if edad <= 10:
        rango_edad = '0-10'
      elif edad <= 20:
        rango_edad = '11-20'
      elif edad <= 30:
        rango_edad = '21-30'
      elif edad <= 40:
        rango_edad = '31-40'
      elif edad <= 50:
        rango_edad = '41-50'
      elif edad <= 60:
        rango_edad = '51-60'
      elif edad <= 70:
        rango_edad = '61-70'
      elif edad <= 80:
        rango_edad = '71-80'
      elif edad <= 90:
        rango_edad = '81-90'
      else:
        rango_edad = '91+'
      new_row = [row[2], row[3], rango_edad, row[6], row[7]]
      new_dataset.append(new_row)

# b) Limpieza de datos: creando dataset con datos purgados
with open('./data/dataset.csv', mode='w', encoding='latin') as csv_file:
  csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  fieldnames = ['PROVINCIA', 'DISTRITO', 'EDAD', 'SEXO', 'FECHA_RESULTADO']
  csv_writer.writerow(fieldnames)
  csv_writer.writerows(new_dataset)