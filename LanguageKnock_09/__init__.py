import random
#文字列をスペースで区切り、単語が4文字より長い場合は最初と最後を残してランダムに並び替える
def typoglycemia(targetString):
    resultArray=[]
    targetArray=targetString.split(' ')
    for i in range(len(targetArray)):
        if len(targetArray[i])>4:
            resultArray.insert(i, makeRandom(targetArray[i]))
        else:
            resultArray.insert(i, targetArray[i])
    result=' '.join(resultArray)
    print(result,end="")
    return result


#文字の最初と最後を残してランダムに並び替える
def makeRandom(target):
    charSplit=[]
    #文字列を文字の配列にする
    for i in range(len(target)):
        charSplit.append(str(target[i]))
    #最初と最後の文字をtemp保存
    first=charSplit[0]
    last=charSplit[len(charSplit)-1]
    #シャッフル用に最初と最後のもじを削除
    del charSplit[0]
    del charSplit[len(charSplit)-1]
    #配列をシャッフル
    random.shuffle(charSplit)
    #最初と最後の文字を復元
    charSplit.insert(0, str(first))
    charSplit.append(str(last))
    result=''.join(charSplit)
    return result

x=input("x= ")
typoglycemia(x)