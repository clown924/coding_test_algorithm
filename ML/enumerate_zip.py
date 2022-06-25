# Enumerate
# - List의 element를 추출할 때 번호를 붙여서 추출
for i, v in enumerate(['tic','tac','toc']):
    print(i,v) # i에는 index 번호, v에는 내용이 unpacking

mylist = ["a","b","c","d"]
print(list(enumerate(mylist)))
dict1 = {i:j for i,j in enumerate('Inha University is an academic institute located in \
South Korea.'.split())}
print(dict1)

# Zip
# - 두 개의 list의 값을 병렬적으로 추출함
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a, b in zip(alist,blist):
    print(a,b)

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
list1 = [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
print(list1)

# Enumerate & Zip
for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)