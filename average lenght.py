import os
os.chdir('C:/Users/Asus')
file1 = open("66684-0.txt","r") 
s = file1.read()
cc = s.lower()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for ele in cc:      #Remove the punctuation unbarbaric way
	if ele in punc:
		cc = cc.replace(ele, "")

aa = cc.split() #splitting the text and make it into a list

x = 0
y = 0 
for i in aa :
    x = x + len(i)  #getting to know the total of letter in the text
    y = y + 1       #getting total of words

print(x)
print(y)
z = x/y  #we divide the total letter with total of words
print(f"This is the average lenght of word : {z}") #printing the answer :)