# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

book = open('Text.txt', 'r', encoding='utf-8').readlines()
words_n = 1
for _ in book:
    words_n += len(book)
print('Количество строк в тексте-', len(book))
print('Количество слов в тексте', words_n)
f.close()

# with open('Text.txt', 'r', encoding='utf-8') as f:
#     usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
#     print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')


# lines_n = 0
# words_n = 0
# f = open('Text.txt', 'r', encoding='utf-8')
# for line in f:
#     lines_n += 1
#     words = line.split()
#     words_n += len(words)
# f.close()
# print(lines_n)
# print(words_n)