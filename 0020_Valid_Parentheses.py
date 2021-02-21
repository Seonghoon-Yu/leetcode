def isValid(self, s):
    table = {
        ')':'(',
        ']':'[',
        '}':'{',
    }
    stack = []
    
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack)
