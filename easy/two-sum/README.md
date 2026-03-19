# Two Sum

## Problem
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

## Example
Input: nums = [2, 7, 11, 15], target = 9

Output: [0, 1]

Explanation: nums[0] + nums[1] = 2 + 7 = 9

## Approaches

### Brute Force (solution_brute.py)
- Compare the sum of every pair of elements to the target
- Time Complexity: O(n²)
- Space complexity: O(n)

### Optimized Approach (Hashmap - `solution_hashmap.py`)
- Instead of checking all pairs, store previously seen numbers in a hashmap
- Time complexity: O(n)
- Space complexity: O(n)

## Implementations
- Brute Force -> `solution_brute.py`
- Optimized -> `solution_hashmap.py`

## Topics
- Array
- Hashmap
- Optimization
