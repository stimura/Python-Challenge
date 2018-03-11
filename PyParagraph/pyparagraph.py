import statistics as stats
import re

print("Please type the name of the file you would like me to analyze.")
filename = input(" ")

with open(filename) as file_object:
    lines = file_object.readlines()     

# To calculate sentences
text_file = []
for word in lines:
    text_file += word.strip()

period_count = text_file.count('.')
explanation_count = text_file.count('!')
question_count = text_file.count('?')
sentence_count = period_count + explanation_count + question_count

# To calculate words
word_count = []
with open(filename,'r') as fileobject:
    for line in fileobject:
        for word in line.split():
            word_count.append(word)

# To calculate average letters
avg_letter = []
for x in word_count:
    letter_count = len(x)
    avg_letter.append(letter_count)

# Average sentence length
joined_file = "".join(word_count)
split_sentences = re.split(r'[.?!]\s*', joined_file)

avg_sentence = []
for v in split_sentences:
    sentence_count = len(v)
    avg_sentence.append(sentence_count)

# Creating variables
average_letters = stats.mean(avg_letter)
average_sentence = (stats.mean(avg_sentence)) / average_letters

# Printing results
print("\n")
print("Paragraph Analysis")
print("-----------------------")
print("Approximate Word Count: " + str(len(word_count)))
print("Approximate Sentence Count: " + str(len(split_sentences)))
print("Average Letter Count: " + str(average_letters))
print("Average Sentence Length: " + str(average_sentence))
print("-----------------------")
print("\n")


