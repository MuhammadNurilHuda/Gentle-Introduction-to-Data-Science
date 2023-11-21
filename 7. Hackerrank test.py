# # If-else
# if __name__ == '__main__':
#     n = int(input().strip())

# if n%2==1:
#     print('Weird')
# elif n%2==0 and 1<n<6:
#     print('Not Weird')
# elif n%2==0 and 5<n<21:
#     print('Weird')
# else:
#     print('Not Weird')
# #===========================

# # Write a Function
# def is_leap(year):
#     leap = False
#     if year%400==0:
#         leap = True
#     elif year%100!=0 and year%4==0:
#         leap = True
#     return leap

# year = int(input())
# print(is_leap(year))
# #============================

# # Nested List
# students = []
# scores = []
# for _ in range (int(input())):
#     name = input()
#     score = float(input())
#     students+=[[name,score]]
#     scores+=[score]
# b=sorted(list(scores))[0]
# for a,c in students:
#     if c==b:
#         print(a)
# #========================

# # sWAP cASE
# def swap_case(s):
#     swap=s.swapcase()
#     return swap

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
# #===========================

# l=[]
# N = int(input())

# for _ in range (0,N):
#     cmd=input().split()
#     if cmd[0]=='insert':
#         l.insert(int(cmd[1]), int(cmd[2]))
#     elif cmd[0]=='print':
#         print(l)
#     elif cmd[0]=='remove':
#         l.remove(cmd[1])
#     elif cmd[0]=='append':
#         l.append(cmd[1])
#     elif cmd[0]=='sort':
#         l.sort()
#     elif cmd[0]=='pop':
#         l.pop()
#     elif cmd[0]=='reverse':
#         l.reverse()
# #===========================

# def count_substring(string, sub_string):
#     if len(string)>=1 and len(string)<=200:
#         count = 0
#         for i in range (len(string)):
#             if string[i:len(string)].startswith(sub_string):
#                 count+=1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)
# #===========================

# if __name__ == '__main__':
#     s = input()
#     if 0<len(s)<1000:
#         print(any(i.isalnum() for i in s))
#         print(any(i.isalpha() for i in s))
#         print(any(i.isdigit() for i in s))
#         print(any(i.islower() for i in s))
#         print(any(i.isupper() for i in s))
# #===========================

