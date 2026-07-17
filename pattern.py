class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()    


        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()


        for i in range(n):
            for j in range(i+1):
                print(j+1 ,end="")
            print()

        for i in range(1,n):
            for j in range(i+1):
                print(i ,end="")
            print()    

        for i in range(n,-1,-1):
            for j in range(i):
                print(j+1,end="")
            print() 


        for i in range(n):

            for j in range(n-i-1):
                print(" ",end="")

            for j in range(2*i+1):
                print("*",end="")
            print()   

        for i in range(n,-1,-1):

            for j in range(n-i+1):
                print(" ", end="")

            for j in range(2*i-1):
                print("*",end="")
            print()   

                     
        for i in range(n):
            if i%2==0:
                start=1
            else:
                start=0
            for j in range(i+1):
                print(start,end="")
                start=1-start

           

        for i in range (1,n+1):
           #left number
           for j in range(1,i+1):
               print(j,end="")
            #space
           for j in range(2*(n-1)):
               print(" ",end="")
            #right number 

           for j in range(i,0,-1):
               print(j,end="")

           print()       
                

        num=1
        for i in range(1,n+1):

            for j in range(1,i+1):
                print(num,end="")
                num+=1
            print()


        for i in range(n+1,-1,-1):

            for char in range(1,i+1):
                print(chr(ord('A') + char-1 ),end="")
            print()

        for i in range(1,n+1):
            for char in range(1,i+1):
                print(chr(ord('A')+ i -1),end="")
            print()  

        for i in range(1,n+1):
            #space
            for j in range(n-i,0,-1):
                print(" ",end='')
            #left 
            for j in range(1,i+1):
                print(chr(ord('A') +j-1),end="")
            #right
            for j in range(i-1,0,-1):
                print(chr(ord('A')+j-1),end="")
            print()    
obj=Solution()
obj.pattern1(5)