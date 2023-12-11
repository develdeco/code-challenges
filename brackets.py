def isValid(s: str):
  pending = []

  matchMap = {
    '{': '}',
    '[': ']',
    '(': ')'
  }

  for bracket in line:
    size = len(pending)
    if size == 0 or bracket in matchMap:
      pending.append(bracket)
    elif pending[size - 1] not in matchMap:
      return False
    elif matchMap[pending[size - 1]] == bracket:
      pending.pop()
    else:
      pending.append(bracket)

  return len(pending) == 0

if __name__ == '__main__':
  line = input()
  if isValid(line):
    print('valid')
  else:
    print('invalid')