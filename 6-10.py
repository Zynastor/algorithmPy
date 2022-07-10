# N을 입력받기
n = int(input())
# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 역정렬 수행
array = sorted(array, reverse=True)
# 결과 출력
for i in array:
    print(i, end=' ')
