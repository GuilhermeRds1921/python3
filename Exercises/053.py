# Develop a program that reads any sentence 
# and says if it is a palindrome, disregarding spaces.

phrase = str(input('Write a phrase: ')).strip().upper()
word = phrase.split()
togheter = ''.join(word)
reverse = togheter[::-1]
print(reverse)
if reverse == togheter:
    print('This is a Palindrome. ')
else:
    print('This ISNT a Palindrome. ')


'''reverse =''
for i in range(len(togheter)-1, -1, -1):
   reverse += togheter[word]'''