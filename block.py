from state import State

class Block:
    def __init__(self, listBlock, cont, tapeX, position, tapeY, positionY, tapeZ, positionZ, blockNameList,
                 contBlockList, listStates, curState, alias, flag):
        self.listBlock = listBlock
        self.cont = cont
        self.tapeX = tapeX
        self.position_tape = position
        self.tapeY = tapeY
        self.positionY = positionY
        self.tapeZ = tapeZ
        self.positionZ = positionZ
        self.contBlockList = contBlockList
        self.contBlock = 0
        self.listStates = listStates
        self.blockNameList = blockNameList
        self.curStateOp = curState
        self.curState = 0
        self.blockName = 0
        self.flag = flag
        self.alias = alias

    def blockCreatorOperation(self):
        flag = False
        if self.listBlock[self.cont][0] == 'inicio':
            self.blockName = self.listBlock[self.cont][1]
            self.blockNameList.append(self.blockName)
            self.curState = int(self.listBlock[self.cont][2])
            print("Início do bloco")
            print(self.listBlock[self.cont])
            self.cont += 1
        elif int(self.listBlock[self.cont][0]) == self.curStateOp:
            self.curState = self.curStateOp
        while self.listBlock[self.cont][0] != 'fim':
            if self.listBlock[self.cont][0] != ';':
                if self.curState == int(self.listBlock[self.cont][0]):
                    if len(self.listBlock[self.cont]) == 9:
                        currentState = State(self.listBlock[self.cont], self.tapeX, self.position_tape, self.tapeY,
                                             self.positionY, self.tapeZ, self.positionZ, self.alias)
                        self.curState, self.tapeX, self.position_tape, self.tapeY, self.positionY, self.tapeZ, \
                        self.positionZ = currentState.operation(self.listBlock[self.cont])
                        self.cont += 1
                    elif len(self.listBlock[self.cont]) == 3:
                        self.curState = int(self.listBlock[self.cont][2])
                        self.listStates.append(self.curState)
                        self.blockName = self.listBlock[self.cont][1]
                        #self.blockNameList.append(blockName)
                        self.contBlock = self.cont
                        self.contBlockList.append(self.contBlock)
                        self.cont += 1
                        self.flag = True
                        return self.cont, self.curState, self.blockNameList, self.blockName, self.contBlock, \
                               self.contBlockList, self.listStates, self.position_tape, self.positionY, self.positionZ
                    elif len(self.listBlock[self.cont]) == 2:
                        if self.listBlock[self.cont][1] == 'rejeita':
                            self.cont += 1
                            return -3, 0, self.blockNameList, self.blockName, self.contBlock, self.contBlockList, \
                                   self.listStates, self.position_tape, self.positionY, self.positionZ
                        elif self.listBlock[self.cont][1] == 'aceita':
                            if (self.tapeX[self.position_tape] == '"') or (self.tapeX[self.position_tape+1] == '"'):
                                self.cont += 1
                                return 0, 0, self.blockNameList, self.blockName, self.contBlock, self.contBlockList, \
                                       self.listStates, self.position_tape, self.positionY, self.positionZ
                            else:
                                self.cont += 1
                                return -3, 0, self.blockNameList, self.blockName, self.contBlock, self.contBlockList, \
                                       self.listStates, self.position_tape, self.positionY, self.positionZ
                    else:
                        return -3, 0, self.blockNameList, self.blockName, self.contBlock, self.contBlockList, \
                               self.listStates, self.position_tape, self.positionY, self.positionZ
                else:
                    self.cont += 1
            else:
                self.cont += 1
        if self.listBlock[self.cont][0] != ';':
            if len(self.listBlock[self.cont]) == 2:
                if self.listBlock[self.cont][0] == 'fim':
                    if self.listBlock[self.cont][1] == self.blockNameList[-1]:
                        if len(self.contBlockList) != 0:
                            self.cont = self.contBlockList.pop() + 1
                        if len(self.listStates) != 0:
                            self.curState = self.listStates.pop()
                        if len(self.blockNameList) != 0:
                            self.blockNameList.pop()
                            self.flag = False
                            if len(self.blockNameList) != 0:
                                self.blockName = self.blockNameList[-1]
                            else:
                                self.blockName = ""
                        return self.cont, self.curState, self.blockNameList, self.blockName, self.contBlock, \
                               self.contBlockList, self.listStates, self.position_tape, self.positionY, self.positionZ
                    elif self.listBlock[self.cont][1] == self.blockNameList[0]:
                        return -3, 0, self.blockNameList, self.blockName, self.contBlock, self.contBlockList, \
                               self.listStates, self.position_tape, self.positionY, self.positionZ
        return self.cont, self.curState, self.blockNameList, self.blockName, self.contBlock, self.contBlockList, \
               self.listStates, self.position_tape, self.positionY, self.positionZ
