# . Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('angltext.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w') as f2:
    f2.writelines(new_file)








# rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
# with open('russian.txt', 'w', encoding='utf-8') as nf:
#     with open('angltext.txt', 'r', encoding='utf-8') as mf:
#         nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in mf]))


# from googletrans import Translator
# with open('4n.txt', 'w', encoding='utf-8') as nf:
#     with open('4m.txt', 'r', encoding='utf-8') as mf:
#         text = mf.read()
#     t = Translator()
#     a = t.translate(text)
#     print(a)