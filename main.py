def binarySearch(myList, key):
  left = 0
  right = len(myList) - 1
  while left <= right:
    mid = left + ((right - left) // 2)
    if (myList[mid] == key):
      return mid
    elif key < myList[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return None


# Code to test the function

testList = [1, 10, 15, 18, 20, 21]
key = int(input("Number to find: "))
result = binarySearch(testList,key)

if (result is not None):
  print("%s was found at position %s."%(key, result))
else:
  print("%s was not found in the list."%(key))
