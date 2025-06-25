import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[1])
        nbCourses = 0
        heap = []
        for course in courses:
            dur = course[0]
            lastD = course[1]
            nbCourses += dur
            heapq.heappush(heap, -dur)
            if nbCourses > lastD:
                nbCourses += heapq.heappop(heap)
        return len(heap)
