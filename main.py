import requests, json,csv

url = requests.get("https://rickandmortyapi.com/api/character/?Species=Human&status=Alive&Origin=Earth")
text = url.text
data = json.loads(text)

res=data["results"]

with open('rickandmorty.json', 'w') as f:
    json.dump(data, f)


#
header = ['name','location','image']
with open('rickandmorty.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
names=[]
locations=[]
links=[]
#res["id"]
res_dict = {}
for character in res:
# print(character)
    name=character["name"] 
    loc=(character["location"]["name"])
    link=character["image"]
    names.append( name )
    locations.append (loc)
    links.append(link)
    row=[name,loc,link]
  
    with open('rickandmorty.csv', 'a', encoding='UTF8') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(row)
        

print (res_dict)
 
