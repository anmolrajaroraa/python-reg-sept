import random

gamePositions = [1,2,3,4,5,6,7,8,9]
availablePositions = [1,2,3,4,5,6,7,8,9]
zeroOrX = input("What do you want to choose (X or 0): ").upper()
cpuInput = '0' if zeroOrX == 'X' else 'X'
userTurn = True

print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3],gamePositions[4],gamePositions[5],gamePositions[6],gamePositions[7],gamePositions[8]))

while True:
    if userTurn:
        positionChoice = int( input(
            f"At which position do you want to place {zeroOrX} : " ) )
        if positionChoice not in availablePositions :
            print( 'Position already occupied' )
            continue
        availablePositions.remove(
            positionChoice )
        gamePositions[ positionChoice - 1 ] = zeroOrX
        userTurn = False
    else:
        cpuChoice = random.choice(availablePositions)
        availablePositions.remove(cpuChoice)
        gamePositions[cpuChoice - 1] = cpuInput
        userTurn = True
        print( '''
        {} | {} | {}
        ------------
        {} | {} | {}
        ------------
        {} | {} | {}
        '''.format( gamePositions[ 0 ] ,
                    gamePositions[ 1 ] ,
                    gamePositions[ 2 ] ,
                    gamePositions[ 3 ] ,
                    gamePositions[ 4 ] ,
                    gamePositions[ 5 ] ,
                    gamePositions[ 6 ] ,
                    gamePositions[ 7 ] ,
                    gamePositions[ 8 ] ) )

    if gamePositions[0] == gamePositions[1] and gamePositions[1] == gamePositions[2]:
        print("User won") if not userTurn else print('Cpu won')
        break
    elif gamePositions[3] == gamePositions[4] and gamePositions[4] == gamePositions[5]:
        print(
            "User won" ) if not userTurn else print(
            'Cpu won' )
        break
    elif gamePositions[6] == gamePositions[7] and gamePositions[7] == gamePositions[8]:
        print(
            "User won" ) if not userTurn else print(
            'Cpu won' )
        break
    elif gamePositions[0] == gamePositions[3] and gamePositions[3] == gamePositions[6]:
        print(
            "User won" ) if not userTurn else print(
            'Cpu won' )
        break
    elif gamePositions[1] == gamePositions[4] and gamePositions[4] == gamePositions[7]:
        print(
            "User won" ) if not userTurn else print(
            'Cpu won' )
        break
    elif gamePositions[2] == gamePositions[5] and gamePositions[5] == gamePositions[8]:
        print(
            "User won" ) if not userTurn else print(
            'Cpu won' )
        break
    elif gamePositions[0] == gamePositions[4] and gamePositions[4] == gamePositions[8]:
        print(
            "User won" ) if not userTurn else print(
            'Cpu won' )
        break
    elif gamePositions[2] == gamePositions[4] and gamePositions[4] == gamePositions[6]:
        print(
            "User won" ) if not userTurn else print(
            'Cpu won' )
        break
