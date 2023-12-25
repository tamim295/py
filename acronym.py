user_input = str(input("Enter a Phrase:"))
text = user_input.split()
a = " "
for i in text: a = a+str(i[0]).upper()
print(a)

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
Phrase=input("please enter the phrase you need its acronym: ")
acro=""
for i in range(len(stopwords)):
    Phrase=Phrase.replace(stopwords[i]+' ',"")
    Phrase=Phrase.replace(',',' ')
Phrase=Phrase.upper()
Words=Phrase.split()
for word in Words:
    acro = acro + word[0]
print(acro)
