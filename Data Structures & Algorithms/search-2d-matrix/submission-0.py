class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        j=len(matrix)-1
        while i<j:
            middle_list=(i+j)//2
            if target==matrix[middle_list][-1]:
                return True
            elif target<matrix[middle_list][-1]:
                j=middle_list
            else:
                i=middle_list+1
        #now we have the i and j that is both equal and are the index of that array that has the target, means we can now implement binary search in that array
        target_array=matrix[i]
        i=0
        j=len(target_array)-1
        while i<=j:
            middle=(i+j)//2
            if target==target_array[middle]:
                return True
            elif target<target_array[middle]:
                j=middle-1
            else:
                i=middle+1
        return False



        #solving in notebook