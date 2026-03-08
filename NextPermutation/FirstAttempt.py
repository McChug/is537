def NextPermutation(nums: list[int]) -> None:
  def palindrome(left: int, right: int):
      while left < right:
          nums[left], nums[right] = nums[right], nums[left]
          left += 1
          right -= 1

  def bubble_from(left: int, length: int):
      iteration = 0
      for _ in range(left, length - 1):
          for b in range(left, length - iteration - 1):
              if nums[b] > nums[b+1]:
                  nums[b], nums[b+1] = nums[b+1], nums[b]
          iteration += 1

  length = len(nums)
  high = -1
  low = -1

  for i in range(length - 1, 0, -1):
      for j in range(i, -1, -1):
          if nums[i] > nums[j]:
              if low == -1 or low < j:
                  high = i
                  low = j

  if high != -1 and low != -1:
      nums[high], nums[low] = nums[low], nums[high]
      bubble_from(low+1, length)
  else:
      palindrome(0, length - 1)

tests = [[1, 2, 3], [3, 2, 1], [5, 3, 7, 2, 0, 9]]
for test in tests:
    print(f"The next permutation for {test} is . . .")
    NextPermutation(test)
    print(test)