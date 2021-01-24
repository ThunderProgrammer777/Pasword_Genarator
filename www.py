info = []
marks =[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    info.append({"name":name,'score':score})

for i in range(len(info)):
    marks.append(info[i]['score'])
m = max(marks)
print(m)

for i in range(len(info)-1):
    if info[i]['score'] == m:
        info.remove(info[i])
        marks.remove(m)
        break
m2 = max(marks)
for i in range(len(info)-1):
    if info[i]['score'] == m2:
        print(info[i]['score'])
        info.remove(info[i])
        marks.remove(m2)
        break
m3 = max
for i in range(len(info)-1):
    if info[i]['score'] == m3:
        print(info[i]['score'])
        info.remove(info[i])
        marks.remove(m3)
        break



