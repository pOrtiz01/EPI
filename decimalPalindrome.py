import math
#O(n) time
#O(n) space
def findPalindrome(pal):
    #negative
    if(pal<0):
        return -1
    pal=str(pal)
    #if string is empty
    if(len(pal)==0):
        return -1
    #if string is one character
    if(len(pal)==1):
        return 1
    left = 0
    right =len(pal)-1
    #check
    while(left<=right):
        if(pal[left]!=pal[right]):
            return -1
        left=left+1
        right=right-1
    return 1

#O(n) time
#O(1) space
def optimal(x):
    if x<=0:
        return x==0
    num_digits = math.floor(math.log10(x)) +1
    msd_mask = 10**(num_digits-1)
    for i in range(num_digits//2):
        if x//msd_mask != x%10:
            return False
        x %=msd_mask
        x //=10
        msd_mask //=100
    return True

# print(findPalindrome(-1331))
# print(findPalindrome(1))
# print(findPalindrome(1221))
# print(findPalindrome(1231))
# print(findPalindrome(12321))
# print(findPalindrome(12322))


# print(optimal(0))
# print(optimal(1))
# print(optimal(7))
# print(optimal(11))
# print(optimal(121))
# print(optimal(333))

#-1 1 1 -1 1 -1