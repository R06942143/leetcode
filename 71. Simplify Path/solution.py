class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        path_stack = []
        
        for name in path_list:
            if not(name == '/' or name == ''):
                if name == '..':
                    if path_stack:
                        path_stack.pop()
                elif name == '.':
                    pass
                else:
                    path_stack.append(name)
        return '/' + '/'.join(path_stack)