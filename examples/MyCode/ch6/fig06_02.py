from collections import Counter

#fig06_02.py
"""Tokenizing a string and counting unique words."""

text = ('this is sample text with several words '
        'this is more sample text with some different words')

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(counter))