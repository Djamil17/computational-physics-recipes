"""
Script:
Author:
Date Created:
Date of Modifications:
Description


"""

### TODO:




# Problem 1b code here...
def gauss_sum(n1: int, n2: int, step: int) -> int:
    """def gauss_sum()


    """
    return sum(range(n1, n2 + 1, step))


print(f"sum from 10-50 is {gauss_sum(10, 50, 1)}")



if __name__=="__main__":

    # Problem 1a code here...

    sum1 = 0
    sum2 = 0
    for i in range(1, 201):
        if i < 101:
            sum1 = sum1 + i
        else:
            sum2 = sum2 + i

    print(f"sum of 1-100 is {sum1} \nsum of 101-200 is {sum2}")

    print()