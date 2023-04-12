class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for d in path:
            if d == '': continue
            elif d == '..':
                if stack: stack.pop()
            elif d != '.': stack.append(d)
        return '/' + '/'.join(stack)