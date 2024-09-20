from stack_basics import Stack
def is_valid_parentheses(str_paren):
    """
    Description:
        Check if the parentheses in the expression are balanced.
    Parameters:
        str_paren: The string containing parentheses.
    Returns:
        bool: True if the parentheses are balanced, False otherwise.
    """
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in str_paren:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    print(is_valid_parentheses("({({)})}"))