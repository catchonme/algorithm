#!/usr/bin/python3
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findKth(A, pa, B, pb, k):
            res = 0
            m = 0
            while pa < len(A) and pb < len(B) and m < k:
                if A[pa] < B[pb]:
                    res = A[pa]
                    m += 1
                    pa += 1
                else:
                    res = B[pb]
                    m += 1
                    pb += 1

            while pa < len(A) and m < k:
                res = A[pa]
                pa += 1
                m += 1

            while pb < len(B) and m < k:
                res = B[pb]
                pa += 1
                m += 1
            return res

        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return findKth(nums1, 0, nums2, 0, n / 2 + 1)
        else:
            smaller = findKth(nums1, 0, nums2, 0, n / 2)
            bigger = findKth(nums1, 0, nums2, 0, n / 2 + 1)
            return (smaller + bigger) / 2.0


sol = Solution()
end = sol.findMedianSortedArrays([1, 2], [3, 4])
print(end)