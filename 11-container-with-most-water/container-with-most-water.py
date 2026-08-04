class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        m = 0
        while i<j:
            area = (j-i) * min (height[i],height[j])
            m = max(area,m)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return m
