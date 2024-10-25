class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []

        for f in folder:
            # Eğer ans boşsa veya yeni klasör, önceki klasörün bir alt klasörü değilse ekle
            if not ans or not f.startswith(ans[-1] + '/'):
                ans.append(f)

        return ans

        