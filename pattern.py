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
       # pattern  question     

        for i in range(1,n+1):
            for j in range(i):
                print(chr(ord('A')+n-i+j),end="")
            print()    

#problem 19
        for i in range(n,0,-1):
            
            #left    
            for j in range(i):
                print("*",end="")
            #space
            for j in range(2*(n-i)):
                print(" ",end="")

        
            #right
            for j in range(i):
                print("*",end="")
            print()    
        for i in range(1,n+1):
                    
                    #left    
                    for j in range(i):
                        print("*",end="")
                    #space
                    for j in range(2*(n-i)):
                        print(" ",end="")
        
                
                    #right
                    for j in range(i):
                        print("*",end="")
                    print()       
        #problem 20
        for i in range(1,n+1):
            #left
            for j in range(i):
                print("*",end="")     
            #space
            for j in range(2*(n-i)):
                print(" ",end="")
            #right
            for j in range(i):
                print("*",end="")    
            print()
            #downward
        for i in range(n-1,0,-1):
            #left
            for j in range(i):
                print("*",end="")     
                        #space
            for j in range(2*(n-i)):
                print(" ",end="")
                        #right
            for j in range(i):
                print("*",end="")    
            print()

        for i in range(n-1,-1,-1):
            for j in range(n):
                if i==0 or i==n-1 or j==0 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")    

            
            print()     

        for i in range(2*n-1):
            for j in range(2*n-1):
                top=i
                left=j
                right=(2*n-2)-j
                bottom=(2*n-2)-i
                print(n-min(min(top,right),min(bottom,left)),end="")
            print()    









obj=Solution()
obj.pattern1(5)