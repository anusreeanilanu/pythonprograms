import csv 
dict_value = [
{"name":"ARUNIMA","MFC":36,"DC":59,"DS":40,"ASE":54},
{"name":"SARANYA","MFC":46,"DC":49,"DS":56,"ASE":44},
{"name":"RUSHALI","MFC":66,"DC":39,"DS":32,"ASE":44},
{"name":"GAYATHRI","MFC":56,"DC":29,"DS":90,"ASE":24},
{"name":"SRUTHI","MFC":56,"DC":50,"DS":60,"ASE":34},
{"name":"NOUBIMA","MFC":46,"DC":39,"DS":60,"ASE":34},
{"name":"HANIMA","MFC":36,"DC":49,"DS":56,"ASE":33},
{"name":"DRISHYA","MFC":46,"DC":39,"DS":60,"ASE":46},
{"name":"VINAYA","MFC":56,"DC":40,"DS":95,"ASE":34},
{"name":"NAMITHA","MFC":36,"DC":56,"DS":66,"ASE":44},]

fields = ["name","MFC","DC","DS","ASE"]

with open('student.csv','w') as c:
    writer = csv.DictWriter(c,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    c.close()
mfc=0
dc=0
ase=0
ds=0
with open('student.csv','r') as cfiles:
     reader = csv.DictReader(cfiles)
     for row in reader:
         print(row['name'],":",(int(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100)
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ase=ase+int(row['ASE'])
         ds=ds+int(row['DS'])
print("\n\nAverage of subjcts")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)
