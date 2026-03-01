class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        best = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                width = i - left
                area = height * width
                if area > best:
                    best = area
            stack.append(i)
        heights.pop()
        return best
