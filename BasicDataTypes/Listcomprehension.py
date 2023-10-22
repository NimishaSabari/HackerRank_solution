'''
Let’s learn about list comprehension! You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.

Example
x = 1

y = 1

z = 2

n = 3 

All permutations of [i, j, k] are:

[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]].

Print an array of the elements that do not sum to n = 3.

[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1],  [1, 1, 0],  [1, 1, 2]]

 

Input Format
Four integers x, y, z and n, each on a separate line.

Constraints
Print the list in lexicographic increasing order.
Sample Input 0
1

1

1

2
 

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
 


'''
#solution
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i=0
#print(i)
    j=0
#print(j)
    k=0
#print(k) 
    sum=x+y+z
    output=[]
    output=[[i,j,k] 
      for i in range(0,x+1) 
        for j in range(0,y+1) 
           for k in range(0,z+1) 
             if i+j+k !=  n] 
print(output)
