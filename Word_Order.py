from collections import Counter
n = int(input())
words = []

for _ in range(n):
    word = input()
    words.append(word)

word_counts = Counter(words)
unique_words = list(word_counts.keys())

print(len(unique_words))
for word in unique_words:
    print(word_counts[word], end=" ")
