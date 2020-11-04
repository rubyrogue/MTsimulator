from tape_X import Tape_X
from tape_Y import Tape_Y
from tape_Z import Tape_Z

class State:
    def __init__(self, state, tapeX, position_tape, tapeY, positionY, tapeZ, positionZ, alias):
        self.state = state
        self.tapeX = tapeX
        self.position_tape = position_tape
        self.tapeY = tapeY
        self.positionY = positionY
        self.tapeZ = tapeZ
        self.positionZ = positionZ
        self.alias = alias

    def operation(self, state):
        self.state = state
        tX = Tape_X(self.tapeX, self.position_tape)
        tY = Tape_Y(self.tapeY, self.positionY)
        tZ = Tape_Z(self.tapeZ, self.positionZ)

        tapeX_content = tX.getTape_X()
        tapeY_content = tY.getTape_Y()
        tapeZ_content = tZ.getTape_Z()
        if len(self.state) == 9:
            stateNumber = int(self.state[0])
            nextState, self.position_tape, self.tapeY, self.positionY, self.tapeZ, self.positionZ =\
                tX.operation(self.state, self.tapeX, self.tapeY, self.positionY, self.tapeZ, self.positionZ, self.alias)
            tapeY_content = self.tapeY
            tapeZ_content = self.tapeZ
            if nextState == -1:
                nextState = stateNumber
            tapeX_content = tX.getTape_X()

            print(state)

            print('X: ' + tapeX_content)
            print('Y: <' + tapeY_content + '>')
            print('Z: <' + tapeZ_content + '>')
            print('--------------------')
            return nextState, tapeX_content, self.position_tape, tapeY_content, tY.position, tapeZ_content, tZ.position
        else:
            return -1, tapeX_content, self.position_tape, tapeY_content, tY.position, tapeZ_content, tZ.position
