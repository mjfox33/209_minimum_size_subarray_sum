from code_209_minimum_size_subarray_sum import Solution

def test_example_1():
    s = Solution()
    nums = [2,3,1,2,4,3]
    target = 7
    output = 2
    assert s.minSubArrayLen(target, nums) == output

def test_example_2():
    s = Solution()
    nums = [1,4,4]
    target = 1
    output = 1
    assert s.minSubArrayLen(target, nums) == output

def test_example_3():
    s = Solution()
    nums = [1,1,1,1,1,1,1,1]
    target = 11
    output = 0
    assert s.minSubArrayLen(target, nums) == output

def test_failed_11():
    s = Solution()
    nums = [1,2,3,4,5]
    target = 11
    output = 3
    assert s.minSubArrayLen(target, nums) == output