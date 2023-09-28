# Замена разделителя в csv файле

## Запуск

changedelimiter.py -i inputfile.csv -o outputfile.csv -d 'delimiter' -n 'new delimiter'

## Опции

-h, --Help
-i, --Input=    исходный csv файл
-o, --Output=   результирующий csv файл, при пропуск опции будет создан файл с именем входного файла и суффиксом _out
-d, --Delimiter= искомый разделитель
-n, --NewDelimiter= новый разделитель
