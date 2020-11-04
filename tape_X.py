from tape_Y import Tape_Y
from tape_Z import Tape_Z

class Tape_X:
    def __init__(self, entry, position):
        self.entry = entry
        self.position = position

    def createTape_X(self):
        self.entry = self.entry
        print(self.entry)

    def getTape_X(self):
        return self.entry

    def tapeStep(self, stateOperation):
        if stateOperation == 'd':
            self.position += 1
        elif stateOperation == 'e':
            self.position -= 1
        elif stateOperation == 'i':
            pass
        else:
            return -2
        return self.position

    def operation(self, stateOperation, tapeX, tapeY, positionY, tapeZ, positionZ, alias):
        self.entry = tapeX
        iniPosition = self.position
        auxPosition = self.position
        tY = Tape_Y(tapeY, positionY)
        tZ = Tape_Z(tapeZ, positionZ)
        if (stateOperation[1] == 'X') or (stateOperation[1] == 'x'):
            if (stateOperation[2] == '*') or (stateOperation[2] == '∗'): #deals with unicode characters as well
                pass
            elif stateOperation[2] == '$d':
                for i in alias:
                    if i == '"':
                        pass
                    elif self.entry[auxPosition] == i:
                        auxPosition += 1
                    else:
                        return -1, self.position, tY.entry, tY.position, tZ.entry, tZ.position
                self.position = auxPosition
                self.position = self.tapeStep(stateOperation[3])
                if self.position == auxPosition + 1:
                    self.position -= 1
                elif self.position == auxPosition - 1:
                    self.position = iniPosition - 1
                    auxPosition = iniPosition - 1
                elif self.position == auxPosition:
                    self.position = iniPosition
                    auxPosition = iniPosition
            elif stateOperation[2] == self.entry[self.position]:
                self.position = self.tapeStep(stateOperation[3])
            else:
                return -1, self.position, tY.entry, tY.position, tZ.entry, tZ.position

            if (stateOperation[4] == '--') or (stateOperation[4] == '−−'):
                nextState = int(stateOperation[5])
                if (stateOperation[6] == 'X') or (stateOperation[6] == 'x'):
                    if stateOperation[7] == '$d':
                        for i in alias:
                            if i == '"':
                                pass
                            else:
                                self.entry = self.entry[:auxPosition] + i + self.entry[auxPosition + 1:]
                                auxPosition += 1
                        self.position = auxPosition
                        self.position = self.tapeStep(stateOperation[8])
                        if self.position == auxPosition + 1:
                            self.position -= 1
                        elif self.position == auxPosition - 1:
                            self.position = iniPosition - 1
                            auxPosition = iniPosition - 1
                        elif self.position == auxPosition:
                            self.position = iniPosition
                            auxPosition = iniPosition
                    elif (stateOperation[7] == '*') or (stateOperation[2] == '∗'):
                        pass
                    else:
                        self.entry = self.entry[:self.position] + stateOperation[7] + self.entry[self.position+1:]
                    self.position = self.tapeStep(stateOperation[8])
                    return nextState, self.position, tY.entry, tY.position, tZ.entry, tZ.position
                elif (stateOperation[6] == 'Y') or (stateOperation[6] == 'y'):
                    tY.operation(stateOperation, alias)
                    return nextState, self.position, tY.entry, tY.position, tZ.entry, tZ.position
                elif (stateOperation[6] == 'Z') or (stateOperation[6] == 'z'):
                    tZ.operation(stateOperation, alias)
                    return nextState, self.position, tY.entry, tY.position, tZ.entry, tZ.position
            else:
                return -2, self.position, tY.entry, tY.position, tZ.entry, tZ.position

        elif (stateOperation[1] == 'Y') or (stateOperation[1] == 'y'):
            tY.position = tY.readOp(stateOperation, alias)
            #nextState = tY.__getstate__()
            if tY.position == positionY:
                return -1, self.position, tY.entry, tY.position, tZ.entry, tZ.position
            elif tY.position == -2:
                return -2, self.position, tY.entry, tY.position, tZ.entry, tZ.position
            if (stateOperation[4] == '--') or (stateOperation[4] == '−−'):
                nextState = int(stateOperation[5])
                if (stateOperation[6] == 'X') or (stateOperation[6] == 'x'):
                    if stateOperation[7] == '$d':
                        for i in alias:
                            if i == '"':
                                pass
                            else:
                                self.entry = self.entry[:auxPosition] + i + self.entry[auxPosition + 1:]
                                auxPosition += 1
                        self.position = auxPosition
                        self.position = self.tapeStep(stateOperation[8])
                        if self.position == auxPosition + 1:
                            self.position -= 1
                        elif self.position == auxPosition - 1:
                            self.position = iniPosition - 1
                            auxPosition = iniPosition - 1
                        elif self.position == auxPosition:
                            self.position = iniPosition
                            auxPosition = iniPosition
                    elif (stateOperation[7] == '*') or (stateOperation[7] == '∗'):
                        pass
                    else:
                        self.entry = self.entry[:self.position] + stateOperation[7] + self.entry[self.position+1:]
                    self.position = self.tapeStep(stateOperation[8])
                    return nextState, self.position, tY.entry, tY.position, tZ.entry, tZ.position
                elif (stateOperation[6] == 'Y') or (stateOperation[6] == 'y'):
                    tY.operation(stateOperation)
                elif (stateOperation[6] == 'Z') or (stateOperation[6] == 'z'):
                    tZ.operation(stateOperation)
            else:
                return -2, self.position, tY.entry, tY.position, tZ.entry, tZ.position

        elif (stateOperation[1] == 'Z') or (stateOperation[1] == 'z'):
            tZ.position = tZ.readOp(stateOperation)
            if tZ.position == positionZ:
                return -1, self.position, tY.entry, tY.position, tZ.entry, tZ.position
            elif tZ.position == -2:
                return -2, self.position, tY.entry, tY.position, tZ.entry, tZ.position

            if (stateOperation[4] == '--') or (stateOperation[4] == '−−'):
                nextState = int(stateOperation[5])
                if (stateOperation[6] == 'X') or (stateOperation[6] == 'x'):
                    if stateOperation[7] == '$d':
                        for i in alias:
                            if i == '"':
                                pass
                            else:
                                self.entry = self.entry[:auxPosition] + i + self.entry[auxPosition + 1:]
                                auxPosition += 1
                        self.position = auxPosition
                        self.position = self.tapeStep(stateOperation[8])
                        if self.position == auxPosition + 1:
                            self.position -= 1
                        elif self.position == auxPosition - 1:
                            self.position = iniPosition - 1
                            auxPosition = iniPosition - 1
                        elif self.position == auxPosition:
                            self.position = iniPosition
                            auxPosition = iniPosition
                    elif (stateOperation[7] == '*') or (stateOperation[7] == '∗'):
                        pass
                    else:
                        self.entry = self.entry[:self.position] + stateOperation[7] + self.entry[self.position+1:]
                    self.position = self.tapeStep(stateOperation[8])
                    return nextState, self.position, tY.entry, tY.position, tZ.entry, tZ.position
                elif (stateOperation[6] == 'Y') or (stateOperation[6] == 'y'):
                    tY.operation(stateOperation)
                elif (stateOperation[6] == 'Z') or (stateOperation[6] == 'z'):
                    tZ.operation(stateOperation)
            else:
                return -2, self.position, tY.entry, tY.position, tZ.entry, tZ.position

        else:
            return -2, self.position, tY.entry, tY.position, tZ.entry, tZ.position