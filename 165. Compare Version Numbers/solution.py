class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_array = version1.split('.')
        version2_array = version2.split('.')
        n = max(len(version1_array), len(version2_array))

        for i in range(n):
            v1 = 0
            v2 = 0
            if i < len(version1_array):
                v1 = int(version1_array[i])
            if i < len(version2_array):
                v2 = int(version2_array[i])
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0
