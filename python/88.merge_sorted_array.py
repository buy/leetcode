# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    # 8:57
    def merge(self, nums1, m, nums2, n):
        indexM, indexN = m - 1, n - 1

        while indexM > -1 and indexN > -1:
            index = indexM + indexN + 1
            if nums1[indexM] > nums2[indexN]:
                nums1[index] = nums1[indexM]
                indexM -= 1
            else:
                nums1[index] = nums2[indexN]
                indexN -= 1

        if indexN > -1:
            nums1[:indexN + 1] = nums2[:indexN + 1]
