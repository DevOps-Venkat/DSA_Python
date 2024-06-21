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
    

obj = Problem()
obj.Optimizied_sumTriangle([1, 2, 3, 4, 5])