rows=int(input("Enter no.of rows: "))
matrices=[]

for i in range(rows):
    n=list(map(int,input().split()))
    sum_of_n=sum(n)
    matrices.append(sum_of_n)
print(matrices)
