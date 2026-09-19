# Given an array `asteroids` of integers representing asteroids in a row, where the absolute value represents the asteroid's size, and the sign represents its direction (positive meaning right, negative meaning left), each asteroid moves at the same speed.

# Your task is to find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode, and if both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
### Example 1:

# ```
# Input: asteroids = [6,13,-4]
# Output: [6,13]
# Explanation: The 13 and -4 collide resulting in 13. The 6 and 13 never collide.
# ```

# ### Example 2:

# ```
# Input: asteroids = [7,-7]
# Output: []
# Explanation: The 7 and -7 collide exploding each other.
# ```

# ### Example 3:

# ```
# Input: asteroids = [11,3,-6]
# Output: [11]
# Explanation: The 3 and -6 collide resulting in -6. The 11 and -6 collide resulting in 11.
# ```
class Solution:
    def asteroidCollision(self, asteroids):
        aft_col = []
        aft_col.append(asteroids[0])
        for i in range(1, len(asteroids)):
            if asteroids[i] < 0 and aft_col[-1] > 0:
                if abs(aft_col[-1]) == abs(asteroids[i]):
                    aft_col.pop(-1)
                elif abs(aft_col[-1]) < abs(asteroids[i]):
                    while abs(aft_col[-1]) <= abs(asteroids[i]):
                        aft_col.pop(-1)
                    if len(aft_col) == 0:
                        aft_col.append(asteroids[i])
                    if ((aft_col[-1] < 0 and asteroids[i] < 0) or (aft_col[-1] > 0 and asteroids[i] > 0)):
                        aft_col.append(asteroids[i])
            else:
                aft_col.append(asteroids[i])
        return aft_col