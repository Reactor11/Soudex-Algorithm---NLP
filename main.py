def remove_adjacent(seq):
  s = seq
  seq = list()
  for i in s:
      seq.append(str(i))
  i = 1
  n = len(seq)
  while i < n:
    if seq[i] == seq[i-1]:
      del seq[i]
      n -= 1
    else:
      i += 1
  s = ''
  for i in seq:
      s = s + str(i)
  return s

print("Soundex Algorithm : Natural Language Processing.")
print("Checks if the two words have same sound or not.")
print("For e.g. grate,great.\n\n\n")

w1 = input("Enter the first word : ").upper()
w2 = input("Enter the second word : ").upper()

w1_clean = w1[0]
w2_clean = w2[0]

rm_list = ['A','E','I','O','U','H','W','Y']

for i in range(1,len(w1)):
    if(w1[i] not in rm_list):
        w1_clean = w1_clean + w1[i]
        
for i in range(1,len(w2)):
    if(w2[i] not in rm_list):
        w2_clean = w2_clean + w2[i]

table = {'B':1,'F':1,'P':1,'V':1,'D':3,'T':3,'L':4,'M':5,'N':5,'R':6}

w1 = w1_clean[0]
w2 = w2_clean[0]

for i in range(1,len(w1_clean)):
    if(w1_clean[i] in table.keys()):
        w1 = w1 + str(table[w1_clean[i]])
    else:
        w1 = w1 + '2'

for i in range(1,len(w2_clean)):
    if(w2_clean[i] in table.keys()):
        w2 = w2 + str(table[w2_clean[i]])
    else:
        w2 = w2 + '2'

w1_clean = w1[0] + remove_adjacent(w1[1:])
w2_clean = w2[0] + remove_adjacent(w2[1:])

if(len(w1_clean) < 4):
    w1_clean = w1_clean + ('0' * (4 - len(w1_clean)))
if(len(w2_clean) < 4):
    w2_clean = w2_clean + ('0' * (4 - len(w2_clean)))

del i,rm_list,table,w1,w2

if(w1_clean == w2_clean):
    print("Both the words have same sound.")
else:
    print("Both the words do not have same sound.")






