# List Comprehensions
result = []
for i in range(10):
    result.append(i)
print(result)

# List Comprehensions
result = [i for i in range(10)] 
print(result)

# Filter 사용
result = [i for i in range(10) if i % 2 == 0] 
print(result)

# 이중 for 문
word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2]
# for i in word_1 :
#   for j in word_2 :
#       result += (i + j) 와 같다
print(result)

case_1 = ["A","B","C"]
case_2 = ["D","E","A"]
result = [i + j for i in case_1 for j in case_2 if not(i==j)]
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [[w.upper(),w.lower(),len(w)] for w in words]
for i in stuff:
    print(i)