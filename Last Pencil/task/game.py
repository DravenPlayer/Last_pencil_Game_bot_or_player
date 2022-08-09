import random
while True:
    choice = input('Do you want to play against a bot or with another player ? bot/player')
    if choice in ['bot','player']:
        break
if choice =='bot':
    bot=True
else:
    bot=False
def check_num(string):
    while True:
        try:
            num_removed = int(input(string))
        except:
            print('Possible values: \'1\', \'2\' or \'3\'')
            string = ''
            continue
            
        if (num_removed in [1,2,3]) ==False:
            print('Possible values: \'1\', \'2\' or \'3\'')
            string=''  
            continue
        elif num_removed>pencils_num:
            print('Too many pencils were taken')
            string=''
            continue
        else:
            return num_removed
def check_win(pencils_num):
    i=1
    lose_positions= []
    while i<=pencils_num:
        lose_positions.append(i)
        i+=4
    if pencils_num in lose_positions:
        return (False,lose_positions)
    else:
        return (True,lose_positions)
def win_strat(pencils_num,lose_positions):
    x = pencils_num-max(lose_positions)
    return x
while True:
    pencils_num = (input('How many pencils would you like to use:\n'))
    if pencils_num.isdigit():
        pencils_num = int(pencils_num)
    else:
        print('The number of pencils should be numeric')
        continue
    if pencils_num==0:
        print('The number of pencils should be positive')
    else:
        break
while True:
    first_player = input('Who will be the first (John, Jack):\n')
    if first_player in ['John', 'Jack']:
        break
    else:
        print('Choose between \'John\' and \'Jack\'')
if first_player == 'Jack':
    strat = True
else:
    strat=False
print(f'{pencils_num *"|"}')
while pencils_num>0:
    string = f'{first_player}\'s turn:\n'
    
    if first_player =='John':
        num_removed = check_num(string)
    else :
        if bot==True:
            print(string, end='')
            if strat == True:
                winnable, lose_positions = check_win(pencils_num)[0], check_win(pencils_num)[1]
                if winnable == True:
                    num_removed = win_strat(pencils_num, lose_positions)
                    print(num_removed)
                else:
                    if pencils_num > 3:
                        x = 3
                    else:
                        x = pencils_num
                    num_removed = random.randint(1, x)
                    print(num_removed)
            else:
                winnable, lose_positions = check_win(pencils_num)[0], check_win(pencils_num)[1]
                if winnable == True:
                    num_removed = win_strat(pencils_num, lose_positions)
                    print(num_removed)
                else:
                    if pencils_num > 3:
                        x = 3
                    else:
                        x = pencils_num
                    num_removed = random.randint(1, x)
                    print(num_removed)
        else:
            num_removed = check_num(string)

    pencils_num-=num_removed
    if first_player =='John':
        first_player='Jack'
    else:
        first_player = 'John'
    if pencils_num ==0:
        print(f'{first_player} won!')
        break
    print(f'{pencils_num *"|"}')