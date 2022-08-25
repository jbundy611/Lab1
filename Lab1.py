name = input("what is your name?: ")
birthday = input('what month were you born in?: ')
print(f'Hello {name} There are {len(name)} letters in your name.')
if 'august' in birthday.lower():
    print('happy birthday month!')

classes = input ('Please enter your classes seperated by a comma: ')
class_list = classes.split(', ')
for s in class_list:
    print(s)

Sentence = "fOnt proCESSOR and ParsER"
Sentence_list = Sentence.split()
first = Sentence_list[0]
second = Sentence_list[1]
third = Sentence_list[2]
fourth =Sentence_list[3]
newSentence = first.lower() + second.capitalize() + third.capitalize() + fourth.capitalize()

print(newSentence)