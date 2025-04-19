import sys

def check_match(s: str) -> bool:
    stack = []
    
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        
        elif ch in ')}]':
            if not stack:
                return False
            
            open_ch = stack.pop()
            if (open_ch, ch) not in {('(', ')'), ('{', '}'), ('[', ']')}:
                return False
    return not stack

out = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if line == '.':
        break

    out.append("yes" if check_match(line) else "no")

sys.stdout.write("\n".join(out))
