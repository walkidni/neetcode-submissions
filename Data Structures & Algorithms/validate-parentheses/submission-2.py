class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            "open": {'(', '[', '{'},
            "close": {')', ']', '}'}
        }
        cl_op = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in par["open"]:
                stack.append(c)
            elif stack:
                if stack[-1] != cl_op[c]:
                    return False
                stack.pop()
            else:
                return False
        
        return len(stack)==0
        