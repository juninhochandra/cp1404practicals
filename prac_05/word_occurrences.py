"""
Word Occurrences
Estimate: 20 minutes
Actual:   16 minutes
"""

string = input("Text: ")
words = string.split()

words_and_counts = {}
for word in words:
    if word in words_and_counts:
        words_and_counts[word] += 1
    else:
        words_and_counts[word] = 1

# We could just use the words array, but the topic is on dictionary, so...
max_word_align = max([len(word) for word in words_and_counts.keys()])

for word in sorted(words_and_counts.keys()):
    print(f"{word:{max_word_align}} : {words_and_counts[word]}")