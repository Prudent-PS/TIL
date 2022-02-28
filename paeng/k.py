def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command             #command가 [2, 5, 3]이라면
                                    #i = 2, j = 5, k = 3
        answer.append(list(sorted(array[i-1:j]))[k-1])
        # list()는 넣어도되고 안 넣어도 될듯!
    return answer


a = [1, 5, 2, 6, 3, 7, 4]  
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]  

print(solution(a,c))