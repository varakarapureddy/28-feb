def findRepeating(nums):

    xor = 0
    for i in nums:
        xor ^= (1 << i)

    print('The odd occurring elements are ', end='')
    for i in nums:
        if xor & (1 << i):
            print(i, end=' ')
            xor ^= (1 << i)


if __name__ == '__main__':

    nums = [1,2,3,2,1,3,2,1,2,2]
    findRepeating(nums)
