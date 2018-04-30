##Problema B

def annograms(word):
  result = []
  words = [w.rstrip() for w in open('WORD.LST')]
  sameLen = list(filter(lambda x: len(x) == len(word),words))
  
  for str1 in sameLen:
    if(anagramSolution1(str1,word)):
      result = [str1] + result 
  print result
  
def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK  

if __name__ == "__main__":
	print(annograms("train"))
	print('--')
	print(annograms('drive'))
	print('--')
	print(annograms('python'))