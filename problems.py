# # problem 1

# numbers = [2, 7, 11, 15, 13, 12, 45, 44, 65, 7, 8, 32, 324, 21, 1, 2, 5, 7, 8]
# total = 329
# def two_sum(nums, target):

#     seen = {}

#     for i,num in enumerate(nums):
#         needed  = target - num
#         if needed in seen:
#             print([seen[needed], i])
#             return [seen[needed], i]
#         seen[num] = i        

# # p1_sol = two_sum(numbers, total)        
# # print(p1_sol)


# # problem 2

# def duplicate(nums):

#     s = set()

#     for num in nums:
#         if num in s:
#             print( "Duplicate Found:", num)
#             break
        
#         s.add(num)
            

# # p2_sol = duplicate(numbers)
# # print(p2_sol)


# # problem 3

# def two_sum_sets(nums, target):
#     seen = set()

#     for num in nums:
#         needed = target - num
#         if needed in seen:
#             return True
#         seen.add(num)

#     return False    


# # problm 4

# def check_repetitions(nums):
#     seen = set()
#     for i in nums:
#         if i in seen:
#             print("Repetition exists for :", i)
        
#         seen.add(i)
#     print("No repetitions found")    

# # problem 5

# nums = [100, 4, 200, 1, 3, 2]

# def longest_consecutive(nums):
#     num_set = set(nums)
#     longest = 0

#     for num in num_set:
#         if num - 1 in num_set:

#             current = num
#             length = 1
#             while current + 1 in num_set:
#                 current+=1
#                 longest+=1

#         longest = max(longest, length)

#     return longest    

# # problem 6

# def is_anagram(s,t):
#     if len(s) != len(t):
#         return False
    
#     count = {}

#     for ch in s:
#         count[ch] = count.get(ch, 0) + 1

#     for ch in t:
#         if ch not in count:
#             return False
#         count[ch] -= 1
#         if count[ch] == 0:
#             del count[ch]

#     return len(count)==0    


# # problem 7

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# def group_anagrams(strs):

#     groups = {}

#     for word in strs:
#         key = ''.join(sorted(word))
#         if key not in groups:
#             groups[key] = []
#         groups[key].append(word)  
#     return list(groups.values())      

# # problem 8

# nums = [1,1,1,2,2,3]
# k = 2

# def topk_frequent(nums):

#     #get frequency
#     count = {}
#     for num in nums:
#         count[num] = count.get(num, 0) + 1

#     # (1 :3) (2:2) (3: 1)    

#     #create buckets
#     freq = [[] for _ in range(len(nums) + 1)] 

#     # populate the frequency buckets
#     for i, j in count.items():
#         freq[j].append(i)

#     # collect top k
#     res = []
#     for i in range(len(freq) -1, 0, -1):
#         for num in freq[i]:
#             res.append(num)
#             if len(res) ==k:
#                 return res






# def two_sum(nums, target):

#     seen = {}

#     for index,num in enumerate(nums):
#         needed = target - num

#         if needed in seen:
#             return [seen[needed], index]

#         else:
#             seen[needed] = index


# from collections import defaultdict

# def valid_anagram(s, t):

#     if len(s) != len(t):
#         return False
    
#     count = {}
#     for i in s:
#         count[i] = count.get(i, 0) + 1

#     for i in t:
#         if i in count:
#             count[i] -= 1
#         else:
#             count[i] = count.get(i, 0) + 1

#     for i in count.keys():
#         if count[i] != 0:
#             return False   

#     return True        
                       

# nums = [2,1,5,1,3,2]
# k = 3

# def max_sum_subarray(nums, k):

#     max_sum = 0
#     previous_sum = sum(nums[0: k])

#     for i in range(1, len(nums) - k):
#         current_sum = previous_sum - nums[i-1] + nums[i+1]
#         if current_sum > max_sum:
#             max_sum = current_sum


# print("Hello from Python")


# s = "abcdabcbbd23456vvvvvvv"
# def longest_substring_in_string(s):
    
#     left = 0
#     longest_substring = 0
#     longest_set = []
#     current_set = set()
#     while left  < len(s):
#         string_chars = []
#         for right in range(left, len(s)):
#             if s[right] not in current_set:
#                 current_set.add(s[right])
#                 string_chars.append(s[right])
#             else:    
#                 left +=1
                
#                 longest_substring = max(longest_substring, len(current_set))
#                 if len(current_set) > len(longest_set):
#                     longest_set = string_chars.copy()
#                 current_set.clear()
#                 string_chars.clear()
#                 break
        
#     return "".join(longest_set)
    
        
# print(longest_substring_in_string(s))     


# s = "abcdecfgh"
# def longest_substring_in_string(s):
    
#     left = 0
#     right = 0
#     max_len = 0
#     current_set = set()
    
#     longest_substring = []
#     current_substring = []
#     while right < len(s):

#         if s[right] not in current_set:
#             print("right:",right)
#             current_set.add(s[right])
#             current_substring.append(s[right])
#             right += 1
            
#         else:
#             print("left:", left)
#             current_set.remove(s[left])
#             current_substring.remove(s[left])
#             left +=1
#         if len(current_substring) > len(longest_substring):
#             longest_substring = current_substring.copy()

#     return "".join(longest_substring)

    
# print(longest_substring_in_string(s))     


# nums = [5,1,9,2,7,3,3,7,5,5,5,5,7]
# k = 3
# import heapq

# def top_k_frequency(nums, k):
#     heap = []
    
#     freq = {}
    
#     for num in nums:
#         freq[num] = freq.get(num, 0) + 1
    
#     for num,count in freq.items():
#         heapq.heappush(heap, (count, num))
        
#         if len(heap) > k:
#             heapq.heappop(heap)
#     # print(heap)     
    
#     top_k = []
#     for i,j in heap:
#         top_k.append(j)
        
#     return top_k

# print(top_k_frequency(nums, k))   


# nums = [5,1,9,2,7,3,3,7,5,5,5,5,7]
# k = 3
# import heapq

# def sort_by_frequency(word):
    
#     heap = []
#     freq = {}
#     for letter in word:
#         freq[letter] = freq.get(letter, 0) + 1
    
#     for letter,count in freq.items():
#         heapq.heappush(heap, (-count,letter))
        
    
#     print(heap)   
#     sorted_word = []
#     for count,letter in heap:
#         for i in range(-count):
#             sorted_word.append(letter)
    
#     return "".join(sorted_word)    
        
        

# print(sort_by_frequency("Tree")   )


# lists = [
#     [1, 4, 5],
#     [1, 3, 4],
#     [2, 6]
# ]
# output = [1, 1, 2, 3, 4, 4, 5, 6]

# # put the first value of each list into a heap
# import heapq
# def merge_k_sorted_lists(lists):
    
#     heap = []
#     for i in range(len(lists)):
            
#         heapq.heappush(heap, (lists[i][0], i , 0))
    
#     result = []
    
#     while heap:
#         value, list_index, element_index = heapq.heappop(heap)
#         result.append(value)
            
#         next_element = element_index + 1
        
#         if next_element < len(lists[list_index]):
#             heapq.heappush(heap, (lists[list_index][next_element], list_index, next_element))
    
#     return result
# print(merge_k_sorted_lists(lists))    

# from collections import deque

# def bfs(graph, start):

#     visited = set()
#     queue = deque()

#     visited.add(start)
#     queue.append(start)

#     while queue:
#         node = queue.popleft()
#         print(node)

#         for nei in graph[node]:
#             if nei not in visited:
#                 visited.add(nei)
#                 queue.append(nei)

# from collections import deque

# def bfs_grid(grid, start_r, start_c):

#     rows,cols = grid.shape[0], grid.shape[1]

#     visited = set()
#     queue = deque()

#     queue.append((start_r, start_c))
#     visited.add((start_r, start_c))

#     directions = [(1, 0), 
#                   (-1, 0),
#                   (0, 1),
#                   (0, -1)]

#     while queue:
#         i, j = queue.popleft()

#         for di, dj in directions:
#             ni = i + di
#             nj = j + dj

#             if 0 <= ni < rows and 0 <= nj < cols:
#                 if (ni, nj) not in visited:
#                     queue.append((ni, nj))
#                     visited.add((ni, nj))



# def rotting_oranges(grid)  :
#     rows, cols = grid.shape[0], grid.shape[1]  

#     rotten = []
#     queue = deque()
#     fresh = 0

#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j]==2:
#                 rotten.append((i,j))
#                 queue.append((i,j))
#             if grid[i][j]==1:
#                 fresh +=1

#     if len(fresh)==0:
#         return 0

#     timesteps = 0

#     while queue:
#         level = len(queue)        
#         # i, j = queue.popleft()

#         directions = [(1, 0), 
#                       (-1, 0), 
#                       (0, 1),
#                       (0, -1) ]   

#         for _ in range(level):
#             i, j = queue.popleft()
#             for di, dj in directions:
#                 ni = i + di
#                 nj = j + dj

#                 if 0 <= ni < rows and 0 <= nj < cols:
#                     if grid[ni][nj]==1:
#                         grid[ni][nj]==2
#                         fresh -=1
#                         queue.append((ni, nj))

#         timesteps +=1
#     if fresh > 0:
#         return -1

#     return timesteps    



# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows, cols = len(grid), len(grid[0])

#         directions = [(1, 0), 
#                         (-1, 0),
#                         (0, 1),
#                         (0, -1)]

#         queue = deque() 
#         num_islands = 0 

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]=="1":
#                     queue.append((r, c))
#                     while queue:
#                         i, j = queue.popleft()
#                         grid[i][j]= "0"

#                         for di, dj in directions:
#                             ni = i + di
#                             nj = j + dj

#                             if 0<=ni<rows and 0<=nj<cols:
#                                 if grid[ni][nj]=="1":
#                                     queue.append((ni, nj))
#                                     grid[ni][nj]= "0"
                                    
#                     num_islands += 1                

#         return num_islands

                        
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows, cols = len(grid), len(grid[0])

#         directions = [(1, 0), 
#                         (-1, 0),
#                         (0, 1),
#                         (0, -1)]

#         queue = deque() 
#         num_islands = 0 

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]=="1":
#                     queue.append((r, c))
#                     while queue:
#                         i, j = queue.pop()
#                         grid[i][j]= "0"

#                         for di, dj in directions:
#                             ni = i + di
#                             nj = j + dj

#                             if 0<=ni<rows and 0<=nj<cols:
#                                 if grid[ni][nj]=="1":
#                                     queue.append((ni, nj))
#                                     grid[ni][nj]= "0"
                                    
#                     num_islands += 1                

#         return num_islands

                        
                        
# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         from collections import deque

#         rows, cols = len(grid), len(grid[0])
#         if grid[0][0] or grid[rows -1][cols -1] != 0:
#             return -1

#         stack = deque()
#         visited = set()

#         directions = [  (-1, 0),
#                         (-1, -1),
#                         (-1, 1),
#                         (0, -1),
#                         (0, 1),
#                         (1, 0),
#                         (1, -1),
#                         (1, 1)   ]

#         stack.append((0, 0))   
#         visited.add((0, 0))      

#         path_len = 0
#         while stack:
#             level = len(stack)

#             for _ in range(level):
#                 i, j = stack.popleft() 
#                 if (i, j) == (rows -1, cols -1):
#                     continue   
#                 for di, dj in directions:
#                     ni = i + di
#                     nj = j + dj
#                     if 0<=ni<rows and 0<=nj<cols:
#                         if grid[ni][nj] == 0:
#                             if (ni, nj) not in visited:
#                                 stack.append((ni, nj))
#                                 visited.add((ni, nj))
                             

#             path_len += 1                
#         if (rows -1, cols -1) in visited:
#             return path_len
#         else:
#             return -1    


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         from collections import deque
#         if root is None:
#             return 0

#         queue = deque()
#         visited = set()
#         queue.append(root)

#         depth = 0
#         while queue:
#             level = len(queue)            
#             for _ in range(level):
#                 node  = queue.popleft()
#                 if node:
#                     if node.left and node.left not in visited:
#                         queue.append(node.left)
#                         visited.add(node.left)
#                     if node.right and node.right not in visited:
#                         queue.append(node.right) 
#                         visited.add(node.right)   
#             depth += 1   

#         return depth      

                

# query = [1.0, 0.0]

# docs = {
#     "doc1": [1.0, 0.0],
#     "doc2": [0.5, 0.5],
#     "doc3": [0.0, 1.0]
# }

# sequences = [
#     [1,2,3],
#     [1,2],
#     [9]
# ]
# max_len = []

# for i in sequences:
#     max_len = max(max_len, len(sequences[i]))

# for i in range(len(sequences)):
#     len_diff = 0
#     if len(sequences[i]) < max_len:
#         for _ in range(len_diff):
#             sequences[i].append(0)

import pandas as pd 

df = pd.read_csv('/Users/avijitkundal/Documents/Data/practice/data.csv')

print(df)