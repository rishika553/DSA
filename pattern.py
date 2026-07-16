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
           
            print()
obj=Solution()
obj.pattern1(5)