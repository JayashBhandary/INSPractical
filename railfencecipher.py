pt = "defendtheeastwall"
print(len(pt))
x = (pt[0])
y = ""
for i in range(1,len(pt)):
    if (i%2==0):
        x += pt[i]
    else:
        y += pt[i]
final = x+ ' ' +y

print(final)

def merge(x,y):
   result=""
   y1 = y.replace(" ","")
   i=0
   while(i<len(x) or i<len(y1)):
      if(i<len(x)):
         result += x[i]
      if(i<len(y1)):
         result += y1[i]
      i+=1
   return result

print(merge(x,y))