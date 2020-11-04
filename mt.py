from block import Block
from tape_X import Tape_X
from tape_Y import Tape_Y
from tape_Z import Tape_Z

file = input("prompt> ")
listFile_ = file.split()
index = 0
position_tape = 1
position_tapeY = 0
position_tapeZ = 0
listFile = list()
word = ""

for j in range(len(listFile_)):
    if listFile_[j][0] == '"':
        word += listFile_[j]
        if listFile_[j][-1] != '"':
            j += 1
            while listFile_[j][-1] != '"':
                word += listFile_[j]
                j += 1
        word += listFile_[j]
        break
    else:
        listFile.append(listFile_[j])
listFile.append(word)

if len(listFile) == 3:
    fileOp = listFile[1]
    tapeX = Tape_X(word, position_tape)
    tapeX.createTape_X()
elif len(listFile) == 4:
    fileOp = listFile[2]
    tapeX = Tape_X(word, position_tape)
    tapeX.createTape_X()

tapeY = Tape_Y("", position_tapeY)
tapeZ = Tape_Z("", position_tapeZ)

content = list()
curState = 0
alias = ""
flag = False
i = 0
contBlock = 0
blockName = 'main'

with open(fileOp) as openFile:
    for line in openFile:
        content.append(line.split())
        if len(line.split()) == 2:
            pass
i = 0
with open(fileOp) as openFile:
    for line in openFile:
        content.append(line.split())
        if len(line.split()) == 2:
            pass

blockNameList = list()
blockContList = list()
blockStateList = list()

while i < len(content):
    if len(content[i]) == 3:
        if content[i][0] == ';':
            i += 1
        elif content[i][0] == '$d':
            if content[i][1] == '=':
                alias = content[i][2]
                i += 1
        elif (content[i][0] == 'inicio') and (content[i][1] == blockName):
            block = Block(content, i, tapeX.entry, position_tape, tapeY.entry, position_tapeY, tapeZ.entry,
                          position_tapeZ, blockNameList, blockContList, blockStateList, curState, alias, flag)
            i, curState, blockNameList, blockName, contBlock, blockContList, \
            blockStateList, position_tape, position_tapeY, position_tapeZ = block.blockCreatorOperation()
            flag = block.flag
            if i == -3:
                print("REJEITA")
                break
            elif i == 0:
                print("ACEITA")
                break
        elif content[i][0] == curState:
            block = Block(content, i, tapeX.entry, position_tape, tapeY.entry, position_tapeY, tapeZ.entry,
                          position_tapeZ, blockNameList, blockContList, blockStateList, curState, alias, flag)
            i, curState, blockNameList, blockName, contBlock, blockContList, \
                blockStateList, position_tape, position_tapeY, position_tapeZ = block.blockCreatorOperation()
            flag = block.flag
            if i == -3:
                print("REJEITA")
                break
            elif i == 0:
                print("ACEITA")
                break
        else:
            i += 1
    elif len(content[i]) == 2:
        if content[i][0] == ';':
            i += 1
        elif not flag:
            if int(content[i][0]) == curState:
                block = Block(content, i, tapeX.entry, position_tape, tapeY.entry, position_tapeY, tapeZ.entry,
                              position_tapeZ, blockNameList, blockContList, blockStateList, curState, alias, flag)
                i, curState, blockNameList, blockName, contBlock, blockContList, \
                    blockStateList, position_tape, position_tapeY, position_tapeZ = block.blockCreatorOperation()
                flag = block.flag
                if i == -3:
                    print("REJEITA")
                    break
                elif i == 0:
                    print("ACEITA")
                    break
        else:
            i += 1
    elif len(content[i]) == 9:
        if not flag:
            if int(content[i][0]) == curState:
                block = Block(content, i, tapeX.entry, position_tape, tapeY.entry, position_tapeY, tapeZ.entry,
                              position_tapeZ, blockNameList, blockContList, blockStateList, curState, alias, flag)
                i, curState, blockNameList, blockName, contBlock, blockContList, \
                    blockStateList, position_tape, position_tapeY, position_tapeZ = block.blockCreatorOperation()
                flag = block.flag
                if i == -3:
                    print("REJEITA")
                    break
                elif i == 0:
                    print("ACEITA")
                    break
        i += 1
    else:
        i += 1
