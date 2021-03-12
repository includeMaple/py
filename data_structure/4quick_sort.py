
def part(li, left, right):
  temp = li[left]
  # 以li[left]为标杆，分别从左边找比他小的和右边找比他大的，并且每次寻找后移动left和right
  # 所以循环的截至情况是当left=right时
  while left < right:
    # temp = li[left]就是拿走了最左边的数，所以下一步是从右边找到一个比temp小的数
    # 停止条件有：
    # 1、找到一个符合条件的数
    # 2、left和right碰头，找到头也没找到
    while temp <= li[right] and left < right:
      # 没有找到时，一直移动right向左
      right -= 1
    # 结束循环也就是找到了一个或者找到头了
    li[left] = li[right]
    # 从左边开始找比temp大的数
    while temp >= li[left] and left < right:
      left += 1
    li[right] = li[left]
    # print(li)
  li[left] = temp
  return left

def quick_sort(li, left, right, positive=True):
  if left < right:
    mid = part(li, left, right)
    quick_sort(li, left, mid-1)
    quick_sort(li, mid+1, right)
  return li

li = [5, 2, 3, 1, 9, 5, 4, 8]
print(quick_sort(li, 0, len(li)-1))
  