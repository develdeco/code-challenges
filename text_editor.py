# Found in code signal
def solution(actions):
  cursor = 0
  select = []
  clipboard = []
  res = ''

  for action in actions:
    pre = action.split(' ')
    op = pre[0]
    
    if op == 'TYPE':
      text = ' '.join(pre[1:])

      if len(select) > 0:
        res = res[0:select[0]]+text+res[select[1]:]
        cursor = select[0]+len(text)
      else:
        res = res[0:cursor]+text+res[cursor:]
        cursor += len(text)

      select = []
      
    elif op == 'SELECT':
      select = [int(pre[1]),int(pre[2])+1]

    elif op == 'MOVE_CURSOR':
      offset = int(pre[1])
      cursor += offset
      
      if cursor < 0: cursor = 0
      elif cursor > len(res): cursor = len(res)

      select = []

    elif op == 'COPY':
      if len(select) > 0:
        clipboard.append(res[select[0]:select[1]])

    elif op == 'PASTE':
      steps = int(pre[1]) if len(pre) > 1 else 1
      text = ''

      if steps > 0 and steps <= len(clipboard):
        pos = len(clipboard)-steps
        text = clipboard[pos]
        clipboard = clipboard[:pos]+clipboard[pos+1:]
      else: continue

      if len(select) > 0:
        res = res[0:select[0]]+text+res[select[1]:]
        cursor = select[0]+len(text)
      else:
        res = res[0:cursor]+text+res[cursor:]
        cursor += len(text)

      select = []

  return res

print(solution(['TYPE Great Britain is the capital of London', 'SELECT 0 12', 'COPY', 'SELECT 32 37', 'COPY', 'PASTE 2', 'SELECT 0 12', 'PASTE', 'MOVE_CURSOR 32', 'TYPE !']))