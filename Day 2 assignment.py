#string functions

#1.capitalize function
str1 = "prasad"
str1.capitalize()
print(str1)

#2.len function
str2 = "hello ra how are you ra"
print(len(str2))

#3.isalpha function
str3 = "heloo prasad"
print(str3.isalpha())

#4. isdigit function
str4 = "9596329"
print(str4.isdigit())

#5. swapcase function
str5 = "HELLO PRASAD"
print(str5.swapcase())







#list functions

list1 = ['apple','banana','orange','mango']
#replace function
list1[2] = "grapes"
print(list1)

#append function
list1.append("papaya")
print(list1)

#sort function
list1.sort()
print(list1)

#insert function
list1.insert(1,"berry")
print(list1)

#reverse function
list1.reverse()
print(list1)






#dictionary functions

dict1 = {1:"prasad",2:"haha",3:"ayya"}

#1.length of dict
print(len(dict1))

#2. membership operators in dict
print(1 in dict1)
print(4 in dict1)

#3. get function
print(dict1.get(1))

#4. inseting function
dict1[4] = "ball"
print(dict1)

#5.update function
dict1[3] = "bat"
print(dict1)
      
      
