class Solution(object):
    def calPoints(self, operations):
        li=[]
        for op in operations:
            if op == "C":
                li.pop()
            elif op == "D":
                li.append(li[-1]*2)
            elif op == "+":
                li.append(li[-1] + li[-2])
            else:
                li.append(int(op))

        return sum(li)


        


        