A = [2,6,8,5,10,11]
target=12

def two_sum(A, target):
    complimentmap = dict()
    for i in range(len(A)):
        compliment = target - A[i]
        if A[i] in complimentmap:
            return[complimentmap[A[i]], i]
        else:
            complimentmap[compliment] = i

print(two_sum(A, target))