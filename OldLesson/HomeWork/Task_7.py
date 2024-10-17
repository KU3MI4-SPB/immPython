import re
from collections import Counter

def top_ten_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    word_counts = {word: count for word, count in word_counts.items() if not word.isdigit()}
    # Сначала сортируем по количеству упоминаний
    sorted_by_count = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    # Затем проходим по списку и сортируем группы слов с одинаковым количеством упоминаний
    sorted_words = []
    last_count = None
    temp_group = []
    for word, count in sorted_by_count:
        if count != last_count:
            if temp_group:
                sorted_words.extend(sorted(temp_group, reverse=True))
                temp_group = []
            last_count = count
        temp_group.append(word)
    # Не забываем добавить последнюю группу, если она есть
    if temp_group:
        sorted_words.extend(sorted(temp_group, reverse=True))

    return [(word, word_counts[word]) for word in sorted_words][:10]

text = 'Hello world. Hello Python. Hello again.'
print(top_ten_words(text))
