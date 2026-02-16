

#1. Two Sum:

class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            needed=target-num
            if needed in seen:
                return [seen[needed],i]
            seen[num]=i

#2. Contains Duplicate:

class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

#3. Best time to buy and sell stock

class Solution(object):
    def maxProfit(self, prices):
        min_price=float('inf')
        max_profit=0
        for x in prices:
            if x<min_price:
                min_price=x
            max_profit=max(max_profit,x-min_price)
        return max_profit        

#4. Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False

        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1

        for ch in t:
            if ch not in count:
                return False
            count[ch]-=1
            if count[ch]==0:
                del count[ch]
        return len(count)==0
        
#5. 3Sum

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1

                elif total<0:
                    left+=1
                else:
                    right-=1
        return res

#6. Reverse a linked list:
class Solution(object):
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev

#7. Loop detection in linked list

class Solution(object):
    def hasCycle(self, head):
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

            if slow==fast:
                return True

        return False
        
#8. Find minimum in rotated array

class Solution(object):
    def findMin(self, nums):
        left,right=0,len(nums)-1

        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid

        return nums[left]

#9. Remove Nth Node from the end of the list
#Define ListNode class for linked list problems
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy

        for _ in range(n):
            fast=fast.next
        
        while fast.next:
            fast=fast.next
            slow=slow.next
        
        slow.next=slow.next.next

        return dummy.next
       
#10. Number of islands:
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        islands=0

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0":
                return
            
            grid[r][c]="0"

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    islands+=1
                    dfs(r,c)

        return islands        


