# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 집합 (set)
# 중복 안됨 ,순서없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print( java & python) 
# print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu,type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))
