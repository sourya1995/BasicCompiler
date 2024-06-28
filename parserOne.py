def parse_expr(s: str, index: int):
    index = skip_space(s, index)
    if s[index] == '(':
        # a list
        index += 1 
        l = []
        while True:
            index = skip_space(s, index)
            if index >= len(s):
                raise Exception('unbalanced parenthesis')
            if s[index] == ')':
                index += 1
                break

            index, v = parse_expr(s, index)
            l.append(v)
        return index, l
    elif s[index] == ')':
        raise Exception('bad parenthesis')
    else:
        start = index
        while index < len(s) and (not s[index].isspace()) and s[index] not in '()':
            index += 1
        if start == index:
            raise Exception('empty program')
        return index, parse_atom(s[start:index])
    
def skip_space(s, index):
    while index < len(s) and s[index].isspace():
        index += 1
    return index

def parse_atom(s):
    #TODO
    import json
    try:
        return ['val', json.loads(s)]
    except json.JSONDecodeError:
        return s
    
def pl_parse(s):
    index, node = parse_expr(s, 0)
    index = skip_space(s, index)
    if index < len(s):
        raise ValueError('trailing garbage')
    return node

def pl_eval(node):
    if len(node) == 0:
        raise ValueError('empty list')
    
    if len(node) == 2 and node[0] == 'val':
        return node[1]