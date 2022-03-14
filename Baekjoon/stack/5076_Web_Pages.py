while True:
    data = input()
    if data == '#':
        break
    else:
        s = []
        check = False
        temp = ''
        for i in range(len(data)):
            if data[i] == '<':
                check = True
            elif data[i] == '>':
                check = False
                if temp and temp[-1] == '/':
                    temp = ''
                    continue
                elif s and s[-1] == temp[1:]:
                    s.pop()
                else:
                    s.append(temp)
                temp = ''

            if check and data[i] == ' ' and data[i + 1] != '/':
                check = False

            if check and data[i] != '<':
                temp += data[i]

        print("illegal" if s else "legal")