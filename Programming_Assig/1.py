

"""
ID : 20CE0015
NAME : Ayush Dabhi
GITHUB REPOSITORY LINK :
"""


a=input()
dic={}
for i in a:
  if dic.get(i)!=None:
    dic[i]+=1
  else:
   dic[i]=1
arr=[dic[i] for i in dic]
arr.sort(reverse=True)

dic1={}
for i in arr:
  for j in dic:
      if dic[j]==i:
         dic1.update({j:i})
         dic.pop(j)
         break
for key,value in dic1.items():
    print(key,value)



