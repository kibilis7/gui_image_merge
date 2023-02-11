#zip 사용법

kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng))) # 리스트를 세로로(!) 합쳐준다.
# [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # *이 붙으면 unzip(분리)
# [('사과', '바나나', '오렌지'), ('apple', 'banana', 'orange')]  

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)

