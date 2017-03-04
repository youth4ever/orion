#=======================================================================
# Author: Isai Damier
# Title: Two Way Partition
# Project: geekviewpoint
# Package: algorithms
#
# Statement:
#   Given n bags of candies, divide the candies between two kids
#   as evenly as possible without splitting individual bags. The candies
#   are valued by weight, in ounce (oz).
#
# Time Complexity: O(n*w)
#    where w is the total weight of all the candies together.
#
# Dynamic Programming Strategy:
#
#   The difference between this problem and the "Positive Subsequence
#   Sum" problem is that here, instead of solving for a given weight
#   x, we are asked to come up with x given the constraint that x must
#   be as close to T/2 as possible.
#
#   So let's do this. Instead of wasting too much time thinking about x,
#   let x = T/2 so that we can proceed as we did for the "Positive
#   Subsequence Sum" problem. Then after we are done filling sum[]
#   completely, we will walk the list backward until we find a positive
#   weight. For our illustration, we will use sequence S=[2,4,7,9].
#   Here are the steps:
#
#   0] Create a boolean array called sum of size x+1:
#     As you might guess, when we are done filling the array, all the
#     sub-sums between 0 and x that can be calculated from S will be
#     set to true and those that cannot be reached will be set to false.
#     For example if S=[2,4,7,9] then sum[5]=False while sum[13]=True
#     because 4+9=13.
#
#   1] Initialize sum[] to False:
#      Before any computation is performed, assume/pretend that each
#      sub-sum is unreachable. We know that's not true, but for now
#      let's be outrageous.
#
#   2] Set sum at index 0 to true:
#     This truth is self-evident. By taking no elements from S, we end
#     up with an empty sub-sequence. Therefore we can mark sum[0]=true,
#     since the sum of nothing is zero.
#
#   3] To fill the rest of the array, we are going to use the following
#     trick. Starting with 0, each time we find a positive sum, we will
#     add an element from S to that sum to get a greater sum. For example,
#     since sum[0]=true and 2 is in S, then sum[0+2] must also be true.
#     Therefore, we set sum[0+2]=sum[2]=true. Then from sum[2]=true and
#     element 4, we can say sum[2+4]=sum[6]=true, and so on.
#
#   4] Recall that we decided to let x=T/2. In an ideal world, we will
#    split the candies and the kids will get exactly the same amount.
#    But since that's not likely to happen in real life, here is a
#    sensible strategy. After we finish filling the sum[] array, starting
#    at x=T/2 we will check to see if sum[x] equals true. If it is, we
#    are done. If not, we decrease x by one and keep checking, until we
#    find sum[x]==true.
#=======================================================================

def subsetSumDivideByTwo( S ):
    # preliminary
    T = 0
    for a in S:
      T += a

    x = T // 2 + 1

    weight = [False] * ( x + 1 )
    weight[0] = True
    for a in S:
        for i in range( x, a - 1, -1 ):
            if not weight[i] and weight[i - a]:
                weight[i] = True

    for i in range( x, -1, -1 ):
        if weight[i]:
            return [i, T - i]


S = [3, 5, 7, 8, 11, 13, 17, 21, 34]
expResult = [60, 59]
result = subsetSumDivideByTwo( S )
print(result)

# S = [3, 5, 7, 8, 13, 17, 21, 34]
# S = [11, 29, 37, 45, 59, 67, 89, 97, 37]
