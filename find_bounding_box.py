import os

talkingpaul = os.fsencode("talkingpaulframes")
talkingleo = os.fsencode("talkingleoframes")
silentpaul = os.fsencode("silentpaulframes")
silentleo = os.fsencode("silentleoframes")

sumw = 0
sumh = 0

num = 0

for file in os.listdir(talkingpaul):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        f = open("talkingpaulframes/" + filename)
        for line in f:
            line = line.strip()
            line = line.split()
            x = int(line[0])
            y = int(line[1])
            w = int(line[2])
            h = int(line[3])
        sumw += w / h
        # sumh += h
        num += 1

print("1")

for file in os.listdir(talkingleo):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        f = open("talkingleoframes/" + filename)
        for line in f:
            line = line.strip()
            line = line.split()
            x = int(line[0])
            y = int(line[1])
            w = int(line[2])
            h = int(line[3])
        sumw += w / h
        # sumh += h
        num += 1

print("2")

for file in os.listdir(silentpaul):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        f = open("silentpaulframes/" + filename)
        for line in f:
            line = line.strip()
            line = line.split()
            x = int(line[0])
            y = int(line[1])
            w = int(line[2])
            h = int(line[3])
        sumw += w / h
        # sumh += h
        num += 1

print("3")

for file in os.listdir(silentleo):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        f = open("silentleoframes/" + filename)
        for line in f:
            line = line.strip()
            line = line.split()
            x = int(line[0])
            y = int(line[1])
            w = int(line[2])
            h = int(line[3])
        sumw += w / h
        # sumh += h
        num += 1

print("4")

print("Average ratio: %f" % (sumw / num))
# print("Average h: %f" % (sumh / num))
