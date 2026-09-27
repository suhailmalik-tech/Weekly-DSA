#Solution-1#
 
class Solution:
    def punishmentNumber(self, n:int) -> int:

        def backtrack(s:str, index:int, curr_target:int) -> bool:
            if index == len(s):
                return curr_target == 0
            if curr_target < 0:
                return False

            num = 0
            for j in range(index, len(s)):
                num = num * 10 + int(s[j])

                if num > curr_target:
                    break
                if backtrack(s, j+1, curr_target - num):
                    return True

            return False

        punishment_sum = 0
        for i in range(1, n+1):
            sq_str = str(i*i)
            if backtrack(sq_str, 0, i):
                punishment_sum += i*i

        return punishment_sum


    #Solution-2#

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        res = []

        def backtrack(index, curr_path):
            res.append(curr_path.copy())


            for i in range(index, len(nums)):
                curr_path.append(nums[i])
                backtrack(i + 1, curr_path)
                curr_path.pop()

        backtrack(0, [])
        return res

        #Solution-3#

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(index, curr_path, rem_target):
            if rem_target == 0:
                res.append(curr_path.copy())
                return

            if rem_target < 0:
                return
            
            for i in range(index, len(candidates)):
                curr_path.append(candidates[i])
                backtrack(i, curr_path, rem_target - candidates[i])
                curr_path.pop()


        backtrack(0, [], target)
        return res



      #Solution-4#

class Solution:
    def uniqueCombinations(self, arr, target):
        
        res = []
        arr.sort()
        
        def back(index, curr, rem_target):
            if rem_target == 0:
                res.append(curr.copy())
                return
            
            if rem_target < 0:
                return
            
            
            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i-1]:
                    continue
                
                if arr[i] > rem_target:
                    break
                curr.append(arr[i])
                back(i + 1, curr, rem_target - arr[i])
                curr.pop()
                
        back(0, [], target)
        return res
                
        