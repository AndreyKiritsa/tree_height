def search(count, data): #поиск самого длинного пути от листа до вершины дерева
    resList = []
    for i in range(int(count))[::-1]:
        ask = i+1
        if data[i][1] == 0 and data[i][2] == 0:
            result = 1
            for j in range(i)[::-1]:
                if ask == data[j][1] or ask == data[j][2]:
                    result +=1
                    ask = j + 1
            resList.append(result)
    return resList

def doit(data): #переработка данных в двоичный массив
    readyData = []
    for i in data:
        x = list(map(int,i.split()))
        readyData.append(x)
    return readyData

def PrintData(data):
    with open('output.txt', 'w', encoding = 'utf8') as outputData: #запись результатов
        outputData.write(data)

def main():
    with open('input.txt', 'r', encoding = 'utf8') as file: #считывание данных
        count = int(file.readline())
        inputData = file.read().split('\n')
    if count == 0 or count == 1:
        PrintData(str(count))
    else:
        data = doit(inputData)
        data = search(count, data)
        PrintData(str(max(data)))


if __name__ == '__main__':
    main()