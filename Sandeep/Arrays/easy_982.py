"""
https://binarysearch.com/problems/First-Fit-Room
"""

def solve(rooms, target):
  for room in rooms:
      if room >= target:
          return room
  return -1

res = solve([1,2,3,3], 3)
print(res)