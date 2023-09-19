
with open("file.txt","r") as IA:
    content=IA.readlines()  # para un archivo json seria json.load()
    newArray=[]
    for line in content:
        newArray.append(line.upper())
    print(len(newArray))
    print(newArray)
    
mydict={
    "name":"pablo",
    "lastname":"silva",
    "age":30

}
print(mydict.get("name"))
print(mydict.keys())
print(mydict["lastname"])
print(mydict.values())