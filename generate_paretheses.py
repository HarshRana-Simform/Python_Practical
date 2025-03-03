# 2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#     Constraints:
#         - 1 <= n <= 8

#     Example 1:
#         - Input: n = 3
#         - Output: ["((()))","(()())","(())()","()(())","()()()"]

#     Example 2:
#         - Input: n = 1
#         - Output: ["()"]


from typing import List

def gen_paren(n :int) -> List[str]:
    """
    Generates all valid combinations of n pairs of parentheses using backtracking through recursion.

    Parameters:
    n (int): The number of pairs of parentheses to generate.

    Returns:
    List[str]: A list of strings, where each string represents a valid combination
               of n pairs of parentheses.
    """

    # Stores an individual valid parenthesis combination
    stack = []
    # Appends all the valid combinations from the stack
    res = []

    def backtrack(open_count :int, closed_count :int):

        if (open_count == closed_count == n):
            res.append("".join(stack))
            return

        if (open_count < n):
            stack.append("(")
            backtrack(open_count + 1, closed_count)
            stack.pop()

        if (open_count > closed_count):
            stack.append(")")
            backtrack(open_count, closed_count + 1)
            stack.pop()

    backtrack(0,0)

    return res

def main():

    try:
        n = int(input("Enter a value: "))

        if n >= 1  and n<=8:
            print(gen_paren(n))
        else:
            print("Invalid input! The constraints only allow numbers between 1 to 8.")

    except:
        print("Invalid input!! Please enter a number between 1 to 8.")



if __name__ == '__main__':
    main()