# 정수 N, M 입력하기
n, m = map(int, input().split())
# N개의 화폐단위 정보입력
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m + 1)

# dynamic programming 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # (i-k) 원을 만드는 방법이 존재할 경우
            print("d[j] : {}, d[j - array[i]]+1 : {}, array[i] : {}, j : {}".format(d[j], d[j - array[i]] + 1, array[i],
                                                                                    j))
            d[j] = min(d[j], d[j - array[i]] + 1)
    print(d)
    # 계산 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
