# You can express a 3D vector as a tuple (x, y, z). Write a program that
# i. sums two such vectors, and returns the result in a new vector.
# ii. Find the dot product of two such vectors

vector_1 = (10,20,32)
vector_2 = (5,10,25)

sum = (vector_1[0]+vector_2[0],
          vector_1[1]+vector_2[1],
          vector_1[2]+vector_2[2],)

dot_product = (vector_1[0]*vector_2[0],
          vector_1[1]*vector_2[1],
          vector_1[2]*vector_2[2],)

print(f"The sum result is {sum}")
print(f"The dot product result is {dot_product}")