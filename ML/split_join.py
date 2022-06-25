# Split 함수
items = 'zero one two three'.split()
print(items)
example = 'python,jquery,javascript'
a,b,c = example.split(",") # 리스트에 있는 각 값을 a,b,c 변수로 unpacking
print(a,b,c)

# Join 함수
colors = ['red','blue','green','yellow']
result = ''.join(colors)
print(result)