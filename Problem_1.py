class Problem: 
    #Solution : Venkatesh M
    def sumTriangle(self,a):
        if len(a)==1:
            print(a)
            return a[0]
        res=[]
        for i in range(len(a)-1):
            j= i+1
            res.append(a[i]+a[j])
        result = self.sumTriangle(res)
        print(a)
        return result
    def Optimizied_sumTriangle(self,a):
        if len(a)==0:
            return []
        res=[]
        for i in range(len(a)-1):
            j= i+1
            res.append(a[i]+a[j])
        self.Optimizied_sumTriangle(res)
        print(a)
    def findMinMax(self,a,res,n):
        if a[n]>res[0]:
            res[0] = a[n]
        if a[n]<res[1]:
            res[1] = a[n]
        if n == 0:
            return res
        return self.findMinMax(a,res,n-1)
    def binarySearch(self,a,s,e,t):
        if(s<=e):
            m = (s+e)//2
            if(a[m]==t):
                return m
            elif (a[m]<t):
                return self.binarySearch(a,m+1,e,t)
            else:
                return self.binarySearch(a,s,e-1,t)
        return -1
    def findFirstUpper(self,s,n):
        if (n<0):
            return -1
        if(s[n].isupper()):
            return s[n]
        else: 
            return self.findFirstUpper(s,n-1)
    def reverseStr(self,s,n):
        if n<=0:
            return s[0]
        return s[n]+self.reverseStr(s,n-1)


obj = Problem()
#Problem 1: Sum Triangle from Array
# obj.Optimizied_sumTriangle([1, 2, 3, 4, 5])

#Problem 2: Recursive Programs to find Minimum and Maximum elements of array
# a = [1, 4, 45, 6, 10, -8]
# res = [0,0]
# result = obj.findMinMax(a,res,len(a)-1)
# print("min=",result[1],", max=",result[0])

#Problem 3: Binary Search
# nums = [-1,0,3,5,9,12]
# print(obj.binarySearch(nums,0,len(nums)-1,9))

#Problem 4: First Uppercase Letter in a String
# s = "geeksforgEeks"
# print(obj.findFirstUpper(s,len(s)-1))

#Problem 5: Reverse String
# s = "hello world"
# print(obj.reverseStr(s,len(s)-1))