# file_name : pr_01_print_func.py

# print 함수 
# 기본 구분자     - sep= " "  (변경가능)
# 기본 끝맺음문자 - end= " "  (변경가능)


print("F1", "Ferrari", "Verstappen", sep=" - ")
print("F1", "Ferrari", "Verstappen", sep=" * ")

print("Hello", end=".")
print("Hello", end=" ! ")
print("Hello")
print("Hello", end=" ! ")

# 출력시도 
# 해당 폴더 경로 이동한 이후에는  (아닐경우 경로 지정 실행 권장)
# $ python ./pr_01_print_func.py

# 출력
# F1 - Ferrari - Verstappen
# F1 * Ferrari * Verstappen
# Hello.Hello ! Hello
# Hello !

