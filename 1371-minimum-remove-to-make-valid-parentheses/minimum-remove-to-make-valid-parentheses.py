class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_p, close_p = 0, 0
        ans_list = []

        ## 2 tur atmamiz gerekiyor, ilkinde ( kullanmak serbest ama ) sayisini kontrol altinda tutuyoruz
        ## 2. turu tersten atiiyoruz, bu kez fazla ( varsa bunlari siliyoruz.

        for c in s:
            if c == "(":
                open_p += 1
                ans_list.append(c)
            elif c == ")":
                if open_p > close_p:

                    close_p += 1
                    ans_list.append(c)
            else:
                ans_list.append(c)
                

        ## acma kapamalar esit sonucu bulduk
        if open_p == close_p:
            return "".join(ans_list)

        ## ac parantezler daha fazla onlari tersten giderek iptal etmeliyiz.
        else:
            res = []

            for i in range(len(ans_list)-1,-1,-1):
                cur = ans_list[i]

                if cur == "(":
                    if open_p <= close_p:
                        res.append(cur)
                    else:
                        open_p -= 1
                elif cur == ")":
                    res.append(cur)
                else:
                    res.append(cur)

            return "".join(reversed(res))
        










'''if open just add to stack
if close check last, if open remove both and continue, if empty or last is close, do not add this paranthesis
stack: (()

lee ( t ( c ) o ) de )'''