# list = [1,2,3,4,5]
# print(list)

# list.reverse() # 역순이 됨 (리턴 값 없이 내부 값 위치만 변동)
# print(list)

lst2 = [1,2,3,4,5]
print("리스트 2 뒤집기 전: ", lst2)

# reverse와 다르게 reversed()는 실제 매개변수에 들어있는
# 리스트의 값이 변하지 않는다! (새로운 값으로 나온다.)
lst3 = reversed(lst2)
print("리스트 2 뒤집은 후: ", lst2)
print("리스트3: ",list(lst3))
