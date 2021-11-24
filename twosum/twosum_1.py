
def twoSum(A, target):
    sum = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            sum = A[i]+A[j]
            if sum == target:
                return[i, j]



A = [2,6,11,15,3]
target = 9
result = twoSum(A, target)
print(result)



