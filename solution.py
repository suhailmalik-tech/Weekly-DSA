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
                
        #Solution-Q5#

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(index, curr_path):
            if len(curr_path) == k:
                res.append(curr_path.copy())
                return

            for i in range(index, n+1):
                curr_path.append(i)
                backtrack(i + 1,  curr_path)
                curr_path.pop()

        backtrack(1, [])
        return res


        #Solution-Q6#

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        is_Additive = False

        def backtrack(index:int, num1:int, num2:int, count:int ):
            if index == n:
                return count >= 3

            expected_sum = num1 + num2
            expected_str = str(expected_sum)

            if not num.startswith(expected_str, index):
                return False


            return backtrack(index + len(expected_str), num2 , expected_sum, count + 1)
        
        for i in range(1, n // 2 + 1):
            if num[0] == '0' and i > 1:
                break

            n1 = int(num[:i])

            for j in range(1,n):
                if max(i,j) > n - i - j:
                    break

                if num[i] == '0' and j > 1:
                    break

                n2 = int(num[i:i+j])

                if backtrack(i + j, n1, n2, 2):
                    return True

        return False



        