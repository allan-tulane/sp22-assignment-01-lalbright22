"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
    if (x <= 1):
        return x
    else:
        ra,rb = (foo(x-1)),(foo(x-2))
        return ra+rb


def longest_run(mylist, key):
  count = 0
  max_count = 0
  for i in mylist:
    if i == key:
        count +=1
    else:
      if count >= max_count:
        max_count = count
      count = 0
  return max_count
      


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return (
            'longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def longest_run_recursive(mylist, key):
  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1,1,1,True)
    else:
      return Result(0,0,0,False)
  else:
    mid = len(mylist)//2

    ls = longest_run_recursive(mylist[:mid], key)
    rs = longest_run_recursive(mylist[mid:],key)

    left = ls.longest_size
    right = rs.longest_size
    longest = None
    entire = None

    if ls.is_entire_range and rs.is_entire_range:
      left = len(mylist)
      right = len(mylist)
      longest = len(mylist)
      entire = True
    elif ls.is_entire_range and not rs.is_entire_range:
      longest = left + rs.left_size
      entire = False
    elif rs.is_entire_range and not ls.is_entire_range:
      longest = right + ls.right_size
    else:
      longest = max(left, right)
      entire = False

  return Result(left, right, longest, entire)
      

    


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
