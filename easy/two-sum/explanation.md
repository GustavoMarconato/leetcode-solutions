# Two Sum - Explanation

## Problem Summary
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

## Example

Input:
nums = [2, 7, 11, 15], target = 9

Output:
[0, 1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9


## Brute Force Approach (Solution1)

### Idea
Check every possible pair of numbers to see if they sum to the target

### Steps
- Use two nested loops
- Compare each pair `(i, j)`
- If `nums[i] + nums[j] == target`, return the indices

### Drawback
- Very slow for large inputs

### Complexity
- Time: O(n²)
- Space: O(1)

## Optimized Approach (Hashmap - Solution2)

### Idea
Instead of checking all pairs, store previously seen numbers in a hashmap

### Steps
- Create an empty hashmap
- Iterate through the list
- For each number:
  - Calculate `complement = target - num`
  - Check if complement exists in the hashmap
    - If yes -> return indices
    - If no -> store current number with its index

### Why it works 
Because we store past values, we can instantly check if the needed pair already exists

### Complexity
- Time: O(n)
- Space: O(n)

## Key insight
Instead of checking all possible pairs, we transform the problem into finding a complement for each number, which can be done efficiently using a hashmap.

## Topics
- Array
- Hashmap
- Optimization

