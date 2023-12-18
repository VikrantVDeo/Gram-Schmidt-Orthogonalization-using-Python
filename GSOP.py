#Gram-Schmidt Orthogonalization Process by Vikrant
#Importing Numpy
import numpy as np
def GSA():
    i=0
    j=0
    #Generating a random matrix a
    a = np.random.randint(10, size=(3, 3))
    print("Matrix A = ",a)
    #Creating a vector representing aColumn Vector 1 in a
    column1=a[:,0]
    print("Column1=",column1)
    #Normalizing column1 of Matrix A
    nc1 = np.linalg.norm(column1)
    #Defining and Generating a unit Vector
    u1=column1/nc1
    A=a.astype(float)
    #Updating the matrix with the unit vector as 1st column vector
    A[:,0]=u1
    print("Modified A = ", A)
    length_of_A= len(A[:,0])
    num=j+1
    #Using While Loop for iterating through other columns:
    while i< length_of_A and num< length_of_A:
        print("A is",A)
        #Performing Gram-Schmidt Process:
        #Calculating Projection
        Proj=((A[:,num])*(A[:,j]))
        #Finding the vector
        k=(A[:,num]) -  (Proj*(A[:,j]))
        #Normalizing the vector
        kn=np.linalg.norm(k)
        #Defining and generating a unit vector for all the remaining columns through while loop
        u2=k/kn
        #Updating the matrix
        A[:,num]=u2
        print("J : ",j, " Num :  ",num, A)
        i+=1
        j+=1
        num+=1
        #Taking transpose of the orthonormal matrix
    AT=A.transpose()
    print("ATranspose: ",AT)
    #Multiplying the orthonormal matrix A with it's transpose to generate an identity matrix
    print("Identity Matrix = " ,np.dot(AT,A))
    #Calling the GSA Function
GSA()