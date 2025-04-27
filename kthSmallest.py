# Approach:
# - Use Binary Search on the value range between the smallest and largest elements.
# - For each mid-value, count how many elements are less than or equal to mid using a staircase-like search.
# - Narrow the search range based on the count until low meets high.
#
# Time Complexity: O(n log(max-min)), where n is the number of rows (or columns), and max/min are the largest and smallest elements.
# Space Complexity: O(1), no extra space used apart from a few variables.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][-1]

        def countLessEqual(mid):
            count = 0
            row = n - 1
            col = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
