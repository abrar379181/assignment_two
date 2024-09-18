import collections
import csv


def get_top_words(text_file, top_n=30):
    with open(text_file, 'r') as file:
        text = file.read().lower().split()
        word_count = collections.Counter(text)
        return word_count.most_common(top_n)


top_words = get_top_words('combined_text.txt')


print(top_words)

# Save to CSV
with open('top_30_words.csv', 'w', newline='') as csvfile:
    csv.writer(csvfile).writerows([['Word', 'Count']] + top_words)
