x=int(input("Enter one number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))
n=int(input("Enter an integer"))

possible_results = []
# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#             sum=i+j+k
#             if ( sum <= n):
#                 result=[i,j,k]
#                 [possible_results.append(result)]
#
# print(possible_results)

result= [ (i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k)<=n]
possible_results.append(result)
print(possible_results)