# thefile = input("What is your file name: ")
# abbreviations = {'dr.': 'doctor', 'Mr.': 'mister', 'bro.': 'brother', 'bro': 'brother', 'mrs.': 'mistress', 'ms.': 'miss', 'jr.': 'junior', 'sr.': 'senior',
#                  'i.e.': 'for example', 'e.g.': 'for example', 'vs.': 'versus', 'mr' : 'mister'}
# terminators = ['.', '!', '?']
# wrappers = ['"', "'", ')', ']', '}']


# def find_sentences(paragraph):  #This like the template to read untill the end of the sentence
#    end = True                   #But,i don' think you allow us to copy others code
#    sentences = []               #So i made myown code(simpler code) but, if you wanna try this code just simply unccomand this code and commend my simple code Thank youu :)
#    while end > -1:
#        end = find_sentence_end(paragraph)
#        if end > -1:
#            sentences.append(paragraph[end:].strip())
#            paragraph = paragraph[:end]
#    sentences.append(paragraph)
#    sentences.reverse()
#    return sentences


# def find_sentence_end(paragraph):
#     [possible_endings, contraction_locations] = [[], []]
#     contractions = abbreviations.keys()
#     sentence_terminators = terminators + [terminator + wrapper for wrapper in wrappers for terminator in terminators]
#     for sentence_terminator in sentence_terminators:
#         t_indices = list(find_all(paragraph, sentence_terminator))
#         possible_endings.extend(([] if not len(t_indices) else [[i, len(sentence_terminator)] for i in t_indices]))
#     for contraction in contractions:
#         c_indices = list(find_all(paragraph, contraction))
#         contraction_locations.extend(([] if not len(c_indices) else [i + len(contraction) for i in c_indices]))
#     possible_endings = [pe for pe in possible_endings if pe[0] + pe[1] not in contraction_locations]
#     if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
#         max_end_start = max([pe[0] for pe in possible_endings])
#         possible_endings = [pe for pe in possible_endings if pe[0] != max_end_start]
#     possible_endings = [pe[0] + pe[1] for pe in possible_endings if sum(pe) > len(paragraph) or (sum(pe) < len(paragraph) and paragraph[sum(pe)] == ' ')]
#     end = (-1 if not len(possible_endings) else max(possible_endings))
#     return end


# def find_all(a_str, sub):
#     start = 0
#     while True:
#         start = a_str.find(sub, start)
#         if start == -1:
#             return
#         yield start
#         start += len(sub)

# az = open(thefile,"r")
# azz = az.read()
# aa = find_sentences(azz) #we call the function and put our text as a paramater
# output = open(thefile,"w")
# for i in aa :
#     print(i) 
#     a = (i,"\n")
#     output.writelines(a) 

#text = " Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
text1 = input("Enter your file with filename.txt template: ") #taking your file name
text2 = open(text1,"r") #open the file to read
text = text2.read() #read the file
output = open(text1,"w")    #open the file again to write
b = text.split() #splitting the text

a = []

for i in b :
    if (i[len(i)-1]) == "." or (i[len(i)-1]) == "!" or (i[len(i)-1]) == "?":
        if i == "Dr." or i == "dr." or i == "mr." or i == "Mr." or i == "mrs." or i == "Mrs." or i == "Jr." or i == "jr." or i == "Sr." or i == "sr." or i == "i.e." or i == "e.g." or i == "vs."  :
            a.append(i)
        else :
            a.append(i) 
            a.append("\n") #looping until we can seperate the sentences and append it into a list
    else : 
        a.append(i)
a.pop() #To pop out the last "\n"


words = ""         #I know we can use join, but it is so boring and it will give a space(so not cool)
for i in a :        #with this code you can take the words and print it without any awkward space.
    if i == "\n" :
        words = words + i
    else: 
        words = words + i + " "

output.writelines(words)
print(words) #so you can see my code is right. You can uncommend line 58, and commend on line 59,60,61,62, and 86
 
