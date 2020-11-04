class Tape_Z:
    def __init__(self, entry, position):
        self.entry = entry
        self.position = position

    def getTape_Z(self):
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

    def operation(self, content, alias):
        auxPosition = self.position
        if (content[2] == '*') or (content[2] == '∗'):
            pass
        elif content[7] == '$d':
            for i in alias:
                if i == '"':
                    pass
                else:
                    self.entry = self.entry + i
                    auxPosition += 1
            self.position = auxPosition
        else:
            self.entry = self.entry + content[7]
        self.position = self.tapeStep(content[8])

    def readOp(self, content, alias):
        auxPosition = self.position
        if (content[2] == '*') or (content[2] == '∗'):
            pass
        elif content[2] == '$d':
            for i in alias:
                if i == '"':
                    pass
                elif self.entry[auxPosition] == i:
                    auxPosition += 1
                else:
                    return self.position
            self.position = auxPosition
        elif content[2] == self.entry[self.position]:
            self.position = self.tapeStep(content[3])
        else:
            return self.position
        return self.position