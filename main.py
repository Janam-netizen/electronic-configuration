atomicnumber=int(input('pls enter atomic  num'))
EC=[]
n=1
while sum(EC)<atomicnumber:
    EC.append(2*n**2)
    n+=1

EC.remove(EC[len(EC)-1])

copyEC=[]
for num in EC:
    copyEC.append(num)
index=len(copyEC)-1
def function(atomicnumber,EC,copyEC,index):
  while atomicnumber-sum(EC)>copyEC[index]:
    EC.append(copyEC[index])
  
while atomicnumber-sum(EC)>8:
  if  atomicnumber-sum(EC)<copyEC[index]:
    while atomicnumber-sum(EC)<copyEC[index]:
      index-=1 
    function(atomicnumber,EC,copyEC,index)
  else:
    function(atomicnumber,EC,copyEC,index)

EC.append(atomicnumber-sum(EC))
print(EC)
