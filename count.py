text=open("sample.txt","r")
counts=dict()
for line in text:
    line=line.strip()
    words=line.split(" ")
    for word in words:
        if word in counts:
            counts[word]=counts[word]+1
        else:
            counts[word]=1
for key in list(counts.keys()):
    print(key,":",counts[key])
