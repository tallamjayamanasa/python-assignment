file = open("sample.txt", "r")

while True:
    ch = file.read(1)

    if ch == "":
        break

    print(ch)

file.close()