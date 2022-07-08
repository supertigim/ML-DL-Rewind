# -*- coding: utf-8 -*-
from functools import cmp_to_key
from pprint import pprint


def print_param(*args):
    print(args)
    for arg in args:
        print(arg)

def main() -> None:
    ''' Test a sample & simple code here '''
    print("hello tester!")

    l: list(int) = list()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(100)

    print_param(*l)


    nums = [1, 0, 0, 2]

    for i, n in enumerate(nums):
        nums[i] = str(n)

    def compare(n1:str, n2:str) -> int:
        if n1 + n2 > n2 + n1: return -1
        else:                 return 1
    
    nums = sorted(nums, key=cmp_to_key(compare))
    print(str(int("".join(nums))))

    

if __name__ == "__main__":
    main()

# end of file 