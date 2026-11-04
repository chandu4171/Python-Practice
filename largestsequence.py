# 1.Find the longest consecutive even-number sequence.

# numbers = [1, 3, 5, 2, 4, 6, 8, 7, 9]
# count=0
# max_count=0
# res=[]
# temp=[]
# for i in range(len(numbers)):
#     if numbers[i]%2==0:
#         count+=1
#         res.append(numbers[i])
#     else:
#         count=0

        
#     if count>max_count:
#         max_count=count
#         temp=res.copy()
# print(temp)
# print(max_count)




# 2. Find the longest consecutive odd-number sequence anywhere in the list.

# numbers = [2, 4, 3, 5, 7, 9, 6, 11, 13]
# count=0
# max_count=0
# res=[]
# temp=[]
# for i in range(len(numbers)):
#     if numbers[i]%2!=0:
#         count+=1
#         res.append(numbers[i])
#     else:
#         count=0
#         res=[]
        
#     if count>max_count:
#         max_count=count
#         temp=res.copy()
        
# print(temp)
# print(max_count)



# 3.write a program to print the highest decreasing sequence and its count

# numbers = [20, 18, 15, 12, 14, 10, 8, 6, 9]
# res=[]
# count=1
# max_count=0
# temp=[]
# for i in range(len(numbers)-1):
#     if numbers[i]>numbers[i+1]:
#         res.append(numbers[i+1])
#         count+=1
        
#     else:
#         count=0
#         res=[]
        
#     if count>max_count:
#         max_count=count
#         temp=res.copy()
        
# print(f'sequence is {temp} and count is {max_count}')



# 4. write a program to print highest frequence which the number is divisible by 3 

# numbers = [4, 6, 9, 12, 7, 15, 18, 21, 24, 10]
# res=[]
# temp=[]
# count=0
# max_count=0
# for i in range(len(numbers)-1):
#     if numbers[i]%3==0:
#         res.append(numbers[i])
#         count+=1
#     else:
#         count=0
#         res=[]
        
#     if count>max_count:
#         max_count=count
        
# print(f'sequence is {res}')
# print(f'count is: {count}')



#5. move all zeroes to the end side and print new list

# numbers = [0, 5, 0, 3, 8, 0, 2, 7]
# result=[]
# for i in numbers:
#     if i>0:
#         result.append(i)
# for i in numbers:
#     if i<=0:
#         result.append(i)
# print(result)

# 6.Find the Longest Word in a Sentence
sentence = "Python programming improves logical thinking"
res = sentence.split()
max_count = 0
longest_word = ''

for word in res:
    count = len(word)

    if count > max_count:
        max_count = count
        longest_word = word

print(f'Longest word is: {longest_word}')
print(f'Length is: {max_count}')














