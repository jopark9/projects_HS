# for waiting_no in [1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1,6): #1,2,3,4,5
#     print("대기번호 : {0}".format(waiting_no))
    

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다." .format(customer))
 
 
    
# while
# customer = "유빈"
# index = 5
# while index >= 1 :
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요." .format(customer,index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기 처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회" .format(customer,index))
#     index += 1

# absent = [2,5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent :
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와" .format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#출석번호가 1 2 3 4 ....  앞에 100을 붙이기로 함 -> 101, 102, 103...
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#학생  이름을 길이로 반환
# students = ["Iron man", "Thor", "I am groot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

#학생  이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# print(students)
# students = [i.upper() for i in students]
# print(students)

# [0] 3번째 손님 (소요시간 :5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2분

from random import *
cnt = 0 # 총 답승 승객 수
for i in range(1,51) : # 1~50 이라는 수 (승객)
    time = randrange(5,51) #5~50분 소요 시간
    if 5<= time <=15: #5~15분 이내의 손님, 탑승 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else: #매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승 승객 : {0} 분" .format(cnt))