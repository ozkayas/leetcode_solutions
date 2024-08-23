class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stack = [defaultdict(int)]
        i = 0
        while i < N:
            ch = formula[i]
            if ch == "(":
                stack.append(defaultdict(int))
                i += 1
            elif ch == ')':
                curMap = stack.pop()
                i += 1
                coef = ""
                while i < N and formula[i].isdigit():
                    coef += formula[i]
                    i += 1
                if coef:
                    for atom in curMap:
                        curMap[atom] *= int(coef)
                for atom in curMap:
                    stack[-1][atom] += curMap[atom]

            else:
                curAtom = ch
                i += 1
                while i < N and formula[i].islower():
                    curAtom += formula[i]
                    i +=1
                curCount = ""
                while i < N and formula[i].isdigit():
                    curCount += formula[i]
                    i += 1
                if curCount == "":
                    stack[-1][curAtom] += 1
                else:
                    stack[-1][curAtom] += int(curCount) 

        final_map = dict(sorted(stack[0].items()))

        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans





        