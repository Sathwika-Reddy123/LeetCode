class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def fun(exp):
            r=[]
            for i in range(len(exp)):
                if exp[i] in "*+-":
                    left=fun(exp[:i])
                    right=fun(exp[i+1:])
                    for l in left:
                        for ri in right:
                            if exp[i]=="+":
                                r.append(l+ri)
                            elif exp[i]=="-":
                                r.append(l - ri)
                            else:
                                r.append(l*ri)
            if not r:
                r.append(int(exp))
            return r
        return fun(expression)
       
        


        