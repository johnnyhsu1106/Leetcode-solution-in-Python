'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
link: https://leetcode.com/problems/rectangle-area/description/
Assume that the total area is never beyond the maximum possible value of int.
'''
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_1 = (C - A) * (D - B)
        area_2 = (G - E) * (H - F)

        if self.is_overlap(A, B, C, D, E, F, G, H):
            overlap_area = (min(C, G)- max(A, E)) * (min(D, H) - max(B, F))
            return area_1 + area_2 - overlap_area
        else:
            return area_1 + area_2

    def is_overlap(self, A, B, C, D, E, F, G, H):
        '''
        :rtype: boolean
        '''
        '''
        idea:
        this is a function, which return True if two rectangle ara overlap; otherwise return False
        '''
        # if rectangle 1 is on the left/right of rectangle 2 and no overlap (only consider x-axis)
        if E >= C or A >= G:
            return False
        # if rectangle 1 is above/below rectangle 2 and no overlap (only consider u-axis)
        if F >= D or B >= H:
            return False

        return True
