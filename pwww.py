# NLP - Natural language processing

# NLP is a branch of computer scicence
# NLP gives computers the ability to understand
# human languages ex) Siri, chatbot

# We need to train the computer with the text data
# so that computer can learn about the human language

# Text preprocessing

# Raw text data may contain unwanted or unimportant text 
# due to which our results might not 
# give efficeint accuracy.

# Twitter, for example
# 1. "I am wayyyy too lazyyyy!!!"

# 2. "I am way too lazy"

# 1 and 2 have same smantic meaning
# but thesese two have have different vibe.
# Depending on how we process data, the reults also different.
import re # Regular Expression
from nltk.corpus import stopwords

text = "The 5 biggest countries by population are China, India, United States, Indonesia, and Brazil."

# Lets you want to count the number words. 
# Computer is case-sensitive, this means computer thinks
# We, we
# We:1 , we:1
# we: 2

# We need change the string in to all lowercases
print(text)
text = text.lower()
print(text)

text = re.sub(r'\d+','',text)
print(text)

text2 = "Box A contains 3 blue balls, 5 red balls, 2 green ballss"
text2 = re.sub(r'\d','',text2) #\d stands for a digit
print(text2)

text3 = "I am ? @ wayyyy, ,too lazyyyy!!!"
# Removing Punctuation
text3 = re.sub(r'[!,?@%^&*]',"",text3)
print(text3)


# We can Stopwords: stopwords is any meanless words 
# ex) a, the, is, be, are, will, ...,..

stopwords = stopwords.words('english')
print(stopwords)
#I am   wayyyy too lazyyyy
word_list = text3.split()

print(word_list)