phrase = str (input())

def removeSpaces(string):
  currentSpace = True
  space = " "
  result = ""
  for i in string:
    
    if i != space:
      currentSpace = True
      result += i
    elif currentSpace:
      result += '_'
      currentSpace = False
  return str(result)


phrase1 = removeSpaces(phrase)

print(phrase1)