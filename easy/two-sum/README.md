# Two Sum
Dificulty: Easy
## Problem
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

## Example
Input: nums = [2, 7, 11, 15], target = 9

Output: [0, 1]

Explanation: nums[0] + nums[1] = 2 + 7 = 9

## Approaches

### Brute Force (solution_brute.py)
- Compare every pair of elements to check if their sum equals the target.
- Time Complexity: O(n²)
- Space complexity: O(1)

### Optimized Approach (Hashmap - `solution_hashmap.py`)
- Instead of checking all pairs, store previously seen numbers in a hashmap
- Time complexity: O(n)
- Space complexity: O(n)

## Key Insight
Using a hashmap allows us to reduce the problem from checking all pairs (O(n²)) to finding complements in constant time, resulting in O(n).

## Implementations
- Brute Force -> `solution_brute.py`
- Optimized -> `solution_hashmap.py`

## Topics
- Array
- Hashmap
- Optimization
