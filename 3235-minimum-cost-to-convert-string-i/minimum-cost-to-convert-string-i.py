class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        

        adj_mat = [[sys.maxsize]*26 for i in range(26)]

        for i in range(26):
            adj_mat[i][i] = 0

  
        for i in range(len(original)):
            u = original[i]
            v =  changed[i]
            wt = cost[i]

            adj_mat[ord(u)-ord('a')][ord(v)-ord('a')] = min(wt , adj_mat[ord(u)-ord('a')][ord(v)-ord('a')])

    
        # apply floyd warshal algo

        for via in range(26):
            for i in range(26):
                for j in range(26):

                    adj_mat[i][j] = min(adj_mat[i][j] , adj_mat[i][via]+adj_mat[via][j])
        
        ans = 0
   
        for i in range(len(source)):

            if  source[i]==target[i]:
                continue;

            else:
                index = ord(source[i])-ord('a')
                tobe = ord(target[i])-ord('a')

                if adj_mat[index][tobe]==sys.maxsize:
                    return -1
             
                else:
          
                    ans+=adj_mat[index][tobe]

        return ans


         