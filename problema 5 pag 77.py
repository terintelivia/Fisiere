f=open("C:\\Users\Admin4ik\Desktop\Informatica\\Caractere.txt",'w')
a=str(input("Introduceti un sir:"))
f.write(a)
f.close()

f=open("C:\\Users\Admin4ik\Desktop\Informatica\\Caractere.txt",'r')
c=f.read()
print("Sirul:",c)
f.close()

vocale=[]
nrvocale=0
for i in range(0,len(c)):
    if c[i]=='o' or c[i]=='a' or c[i]=='i' or c[i]=='e' or c[i]=='u' or c[i]=='O' or c[i]=='A' or c[i]=='I' or c[i]=='E' or c[i]=='U':
         nrvocale+=1 
         vocale.extend(c[i])

f=open("C:\\Users\Admin4ik\Desktop\Informatica\\Vocale.txt",'w')
f.write(a)
f.close()
print("Numarul de vocale este:",nrvocale,"\n","Vocalele sunt:",vocale)     