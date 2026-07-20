class Solution:
    #problem 1
    def countDigit(self, n):
          count=0
          if n==0:
            return 1
          while n > 0:
            n=n//10
            count+=1
          return count 
       #problem 2
    def reverse(self,n):  
        reverse=0
        if n==0:
            return 0
        while n>0:
            last_digit=n%10  
            reverse=reverse*10+last_digit
            n=n//10  
         
        return reverse
    #problem 3
    def isPalindrome(self, n):
        s=str(n)
        for i in range(len(s)):
            if s[i] !=s[len(s)-i-1]:
                return False
        return True
#problem 4
    def GCD(self, n1, n2):
      small=min(n1,n2)
      gcd=1
      for i in range(1,small+1):
        if n1%i==0 and n2%i==0:
            gcd=i
      return gcd    


#problem 5
    def isArmstrong(self, n):
        number=0
        digits=len(str(n))
        original=n
        while n>0:
            last_digit=n%10
            number+=last_digit**digits
            n=n//10
        if original==number:
            return True
        return False
#problem 6
    def divisors(self, n):
        x=[]
        for i in range(1,n+1):
            if n%i==0:
                x.append(i)
        return x   


obj=Solution()
print(obj.countDigit(590900009900))
print(obj.reverse(89))
print(obj.isPalindrome(121))
print(obj.GCD(24,56))
print(obj.isArmstrong(153))
print(obj.divisors(8))