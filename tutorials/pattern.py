def is_valid(s: str) -> str:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'  # Pop from stack or use dummy value
            if bracket_map[char] != top_element:
                return "invalid"
        else:
            stack.append(char)
    
    return "valid" if not stack else "invalid"

# Test cases
print(is_valid("()"))        # valid
print(is_valid("()[]{}"))    # valid
print(is_valid("([]]"))        # invalid
print(is_valid("([])"))      # invalid
print(is_valid("{[]}"))      # valid