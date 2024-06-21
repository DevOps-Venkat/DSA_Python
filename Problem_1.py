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

obj = Problem()
obj.sumTriangle([1, 2, 3, 4, 5])