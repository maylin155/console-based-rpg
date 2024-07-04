from time import sleep
import random



class Game:
    def __init__(self, EXP=0, char_name=''):
        self.char_name = chname
        self.char_type = 'Character'
        self.attributes = {'HP': 100,
                           'FULLHP': 100,
                           'ATK': 0,
                           'DEF': 0,
                           'EXP': 0,
                           'RANK': 1,
                           'LIVE': True}
        # 0     #1

    def __repr__(self):
        # User's unit type and name
        for i in range(unit_amount):
            unit_char = f'\nUnit Type = ' + self.char_type + '\nUnit Name = ' + self.char_name + '\n'

        # User's Unit attributes:
        for a, c in self.attributes.items():
            unit_char += '{0}: {1}  '.format(a, c)
            return unit_char

    def attack(self, target):
        # Calculate damage
        damage = self.attributes['ATK'] - target + random.randint(-5, 10)

        # attacker.EXP increase based on the calculated damage point.
        if damage > 0:
            self.attributes['EXP'] += damage
        # If no damage received, damage = 0
        return damage

    def receive_attack(self, damage):
        # If damage received > 10, gain extra 20% EXP:
        if damage > 10:
            self.attributes['EXP'] += int(damage * 1.2)
            self.attributes['HP'] -= damage
        # If damage received <= 0, gain extra 50% EXP:
        elif damage <= 0:
            self.attributes['EXP'] += int(abs(damage) * 1.5)
        # If no damage taken, EXP = 0
        else:
            self.attributes['EXP'] += damage
            # target.HP deducted based on the calculated damage point:
            self.attributes['HP'] -= damage

        # Unit will be died if HP = 0
        if self.attributes['HP'] <= 0:
            self.attributes['HP'] = 0
            self.attributes['LIVE'] = False

    def rank_up(self):
        # A unit will be promoted (level up) when the EXP point reached 100:
        self.attributes['RANK'] += 1
        # EXP will be deducted by 100 point:
        self.attributes['EXP'] -= 100

    def get_char_name(self):
        return self.char_name

    def get_char_type(self):
        return self.char_type

    def is_live(self):
        return self.attributes['LIVE']

    def get_hp(self):
        return f"{self.attributes['HP']} / {self.attributes['FULLHP']}"

    def get_def(self):
        return self.attributes['DEF']


class Warrior(Game):
    def __init__(self, EXP=0, char_name=''):
        super().__init__(EXP=EXP, char_name=char_name)
        self.char_type = 'Warrior'
        self.attributes['ATK'] += random.randint(5, 20)
        self.attributes['DEF'] += random.randint(1, 10)

    def attack(self, target):
        damage = super().attack(target)
        self.count_level()
        return damage

    def receive_attack(self, damage):
        super().receive_attack(damage)
        if super().is_live():
            self.count_level()

    def rank_up(self):
        # When unit's rank up, its EXP will be deducted
        super().rank_up()

        # Attributes(ATK, DEF, HP) for each warrior
        self.attributes['ATK'] += random.randint(5, 20)
        self.attributes['DEF'] += random.randint(1, 10)
        self.attributes['FULLHP'] += 10

        self.attributes['HP'] += int(self.attributes['FULLHP'] * 0.1)
        if self.attributes['HP'] > self.attributes['FULLHP']:
            self.attributes['HP'] = self.attributes['FULLHP']

    def count_level(self):
        if self.attributes['EXP'] >= 100:
            for c in range(int(self.attributes['EXP'] / 100)):
                self.rank_up()
            self.attributes['EXP'] = self.attributes['EXP'] % 100


class Tank(Game):
    def __init__(self, EXP=0, char_name=''):
        super().__init__(EXP, char_name=char_name)
        self.char_type = 'Tank'
        self.attributes['ATK'] += random.randint(1, 10)
        self.attributes['DEF'] += random.randint(5, 15)

    def attack(self, target):
        damage = super().attack(target)
        self.count_level()
        return damage

    def receive_attack(self, damage):
        super().receive_attack(damage)
        if super().is_live():
            self.count_level()

    def rank_up(self):
        # When unit's rank up, its EXP will be deducted
        super().rank_up()

        # Attributes(ATK, DEF, HP) for each tank
        self.attributes['ATK'] += random.randint(1, 10)
        self.attributes['DEF'] += random.randint(5, 15)
        self.attributes['FULLHP'] += 10

    def count_level(self):
        if self.attributes['EXP'] >= 100:
            for c in range(int(self.attributes['EXP'] / 100)):
                self.rank_up()
            self.attributes['EXP'] = self.attributes['EXP'] % 100


class Enemy(Game):
    def __init__(self, EXP=0, char_name=''):
        super().__init__(EXP=EXP, char_name=char_name)
        self.char_type = AI_chtype
        self.char_name = AI_chname
        if self.char_type == 'Warrior':
            self.attributes['ATK'] += random.randint(5, 20)
            self.attributes['DEF'] += random.randint(1, 10)

        elif self.char_type == 'Tank':
            self.attributes['ATK'] += random.randint(1, 10)
            self.attributes['DEF'] += random.randint(5, 15)

    def attack(self, target):
        damage = super().attack(target)
        self.count_level()
        return damage

    def receive_attack(self, damage):
        super().receive_attack(damage)
        if super().is_live():
            self.count_level()

    def rank_up(self):
        # When unit's rank up, its EXP will be deducted
        super().rank_up()

        # Attributes(ATK, EXP, FULLHP) for each warrior
        self.attributes['ATK'] += random.randint(4, 15)
        self.attributes['DEF'] += random.randint(1, 10)
        self.attributes['FULLHP'] += 10

    def count_level(self):
        if self.attributes['EXP'] >= 100:
            for c in range(int(self.attributes['EXP'] / 100)):
                self.rank_up()
            self.attributes['EXP'] = self.attributes['EXP'] % 100


all_unit_names = []
all_unit_types = []
all_unit_attributes = []
all_AI_chtypes = []
unit_amount = 0
chname = ''


# Ask user how many unit do he/she wish to create
def create_no_unit():
    global unit_amount
    while True:
        try:
            unit_amount = int(input('\nEnter number of units you wish to create: '))
            # Input Validation:
            if unit_amount < 3:  # Checking whether the unit amount is greater than or equal to 3 or not:
                print('ERROR: You have to make at least 3 units to play the game')
            else:  # If more than 3, break the input validation loop
                break
        except ValueError:  # If user's input is not integer
            print('ERROR: Enter only a number')


# Creating User's Units
def create_unit():
    global all_unit_attributes
    global all_unit_types
    global all_unit_names
    global chname
    global ch_unit1
    print('\n' + 'Creating units...')
    # Using for loop, how many units to be created:
    for i in range(unit_amount):
        print('Unit no:', i + 1)
        # Inputting User's Unit Type:
        while True:  # input validation loop
            chtype = input('Enter unit type (Warrior/Tank) no. {} [w/t]: '.format(
                i + 1)).lower()  # Using .lower() to make the input can be uppercase letter
            # Input Validation:
            if chtype == 'w' or chtype == 't':  # If User's input is w/W, t/T, then break the loop
                break
            # Checking the name, is it only blank or user's input is space or blank only
            elif chtype.isspace() or chtype == '':
                print('ERROR: Cannot contain only space or blank for your unit no.', i + 1)
            # If User's input is not w/W, t/T
            else:
                print('ERROR: You can only select either Warrior or Tank for your unit No. {} [w/t]\n'.format(i + 1))

        # Inputting User's Unit Name:
        while True:
            chname = input('Enter unit name no. {}: '.format(i + 1))
            # Input Validation: Checking the name is it the same as the previous one. If yes:
            if chname in all_unit_names:
                print('ERROR: Cannot use the same name for your unit no.', i + 1)
            # Checking the name, is it only blank or user's input is space or blank only
            elif chname.isspace() or chname == '':
                print('ERROR: Cannot contain only space or blank for your unit no.', i + 1)
            # If the name not same(unique):
            else:
                # Collect the user's name & store in variable all_unit_names
                all_unit_names.append(chname)

                # Assigning attributes for each unit
                if chtype == 'w':  # If unit = Warrior
                    chtype = 'Warrior'
                    ch_unit1 = Warrior()  # Call the warrior function in class Warrior
                    all_unit_types.append('Warrior')  # Collect & store in variable all_unit_types
                    all_unit_attributes.append(ch_unit1)  # This to collect all attributes of units
                elif chtype == 't':  # If unit = Tank
                    chtype = 'Tank'
                    ch_unit1 = Tank()  # Call the Tank function in class Warrior
                    all_unit_types.append('Tank')  # Collect & store in variable all_unit_types
                    all_unit_attributes.append(ch_unit1)  # This to collect all attributes of units

                # Printing the User's Unit Type, Unit Name, Attributes (for each round)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', '\nYour Unit {}: '.format(i + 1),
                      ch_unit1, '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                i += 1
                break

    # User now can play the game because their units are sufficient, i.e. greater than or equal to 3
    print(
        '~ Well Done! You have created your units successfully!~\n~     You can Play the game now! Enter 2 to play.     ~\n')


all_AI_attributes = []
AI_chtype = ''
AI_chname = ''
all_AI_types = []
all_AI_names = []


# Create enemies:
def create_AI():
    global AI_chtype
    global AI_chname
    global AI_chunit1
    # Choices for AI type:
    AI_setup = ['Warrior', 'Tank']

    for a in range(unit_amount):
        # Making the AI name:
        AI_chname = 'AI' + str(random.randint(10, 99))
        all_AI_names.append(AI_chname)  # Collect & Store the AI names in variable all_AI_names
        # Selecting AI Types randomly:
        AI_chtype = ''.join(random.choices(AI_setup))
        # Assigning attributes for each AI unit:
        if AI_chtype == 'Warrior':  # If AI unit = Warrior
            AI_chunit1 = Enemy()  # Call the Enemy function in class Enemy
            all_AI_types.append('Warrior')  # Collect & Store AI types in variable all_AI_types
            all_AI_attributes.append(AI_chunit1)  # This to collect all attributes of AI units
        elif AI_chtype == 'Tank':  # If AI unit = Tank
            AI_chunit1 = Enemy()  # Call the Enemy function in class Enemy
            all_AI_types.append('Tank')  # Collect & Store AI types in variable all_AI_types
            all_AI_attributes.append(AI_chunit1)  # This to collect all attributes of AI units


# This is the function to restart game:
def restart_game():
    # Asking once again whether user want to restart the game and delete all of their units:
    while True:
        restart = input('Do you want to start over and DELETE all your units? [y/n]: ').lower()
        # If yes:
        if restart == 'y':
            # Clear the variable all_unit_types, all_unit_names, all_unit_attributes
            # so that it will overwrite the previous list
            all_unit_types.clear()
            all_unit_names.clear()
            all_unit_attributes.clear()
            all_AI_chtypes.clear()
            all_AI_names.clear()
            all_AI_attributes.clear()
            print('You have restarted the game.\n')
            break  # break the loop & units and game are restarted

        # If no:
        elif restart == 'n':
            print('Your Units are stored\n')
            break  # break the loop & units and game are restored
        else:  # If user's input other than y/n:
            print('Please enter either y/n')
        # Will loop back to top to enter choices y/n


def menu_player():
    players_title = '=== All Player Units ==='.center(54)  # To make it in the middle
    # Printing all unit attributes, names, types
    print(players_title,
          '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ''.join(map(str, all_unit_attributes)), '\n')


def menu_enemies():
    enemies_title = '=== Your Opponents ==='.center(54)
    print(enemies_title,
          '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' + ''.join(map(str, all_AI_attributes)),
          '\n')


def begin_game(units):
    # Printing all the User's Unit Type & Unit Name, Attributes (After creating units)
    print('\n', '\nGame has begun. The following characters are present:')
    menu_player()
    while True:
        print('\nLoading... Creating your enemies...\n')
        sleep(1)
        # Printing AI units & attributes:
        menu_enemies()
        # Start playing:
        # Begin the battle:
        play(all_unit_attributes, all_AI_attributes)
        break


'''
        if not play(all_unit_attributes, all_AI_attributes):
            print('GAME OVER')
            print('Thank you for playing!')
            break
'''


def players_dead(units):
    for player_unit in units:
        if player_unit.is_live():
            return False
    return True


def enemies_dead(enemy_units):
    for enemy in enemy_units:
        if enemy.is_live():
            return False
    return True


# Function to attack with 2 parameters, player and which AI want to be attacked
def player_turn(player_unit, target_unit):
    # Player attacks to AI:
    damage = player_unit.attack(target_unit.get_def())

    # Enemy dealt damages from player:
    target_unit.receive_attack(damage)
    return [player_unit.get_char_name(), target_unit.get_char_name(), damage]


def enemy_turn(units, enemy_units):
    attack_result = []
    live_players = []

    for player_unit in units:
        if player_unit.is_live():
            live_players.append(player_unit)

    for enemy_unit in enemy_units:
        if enemy_unit.is_live():
            target_unit = random.choice(live_players)
            damage = enemy_unit.attack(target_unit.get_def())
            target_unit.receive_attack(damage)

            if not target_unit.is_live():
                live_players.remove(target_unit)

            attack_result.append([enemy_unit.get_char_name(), target_unit.get_char_name(), damage])
    return attack_result


target = 0
rounds = 1


def play(units, enemy_units):
    rounds = 0
    global target, index_unit
    win = False

    while rounds > -1:
        # Players turn:
        print('\n=== Round {} ==='.format(rounds + 1))
        print("Player's Move")
        unit_no = int(input('Select player unit to use [1-3] (depends on how many units created): '))
        for i in range(unit_amount):
            index_unit = units[i - 2]

        # Checking whether unit_no entered is live or not:
        if index_unit.is_live():
            print(f"\nUnit's {index_unit.get_char_type()} {index_unit.get_char_name()}'s turn. Select your target:")
            for i in range(len(enemy_units)):
                print(
                    f"{i + 1}. {enemy_units[i].get_char_type()} {enemy_units[i].get_char_name()}: {enemy_units[i].get_hp()}")

            while True:
                # Check if all enemies has been dead or not:
                if enemies_dead(enemy_units):
                    print('\nEnemies has been killed!')
                    win = True
                    break  # If yes, break the loop, you win and game over
                target = input('Select AI target to attack [1-3] (depends on how many units created) [Q = Quit]: ')
                if int(target) >= 1 and int(target) <= len(enemy_units) and target.isnumeric():
                    if not enemy_units[int(target) - 1].is_live():
                        print(
                            f"{enemy_units[int(target) - 1].get_char_name()} has been killed. Choose a different enemy.")
                    else:
                        # Go to def enemy_turn & print the result of attack
                        round_u_attack_result = player_turn(units[int(unit_no) - 1], enemy_units[int(target) - 1])
                        # If there's damage dealt. Index 2 is the damage point
                        if round_u_attack_result[2] > 0:
                            print(
                                f"\n{round_u_attack_result[0]} has been hit {round_u_attack_result[1]} with {round_u_attack_result[2]} damage")
                        # If no damage dealt:
                        else:
                            print(
                                f"\n{round_u_attack_result[0]} has been hit with {abs(round_u_attack_result[2])} damage, but {round_u_attack_result[1]} avoided.")
                        break
                elif target == 'q'.lower():
                    print('You leave the game')
                    return False
                else:
                    print('ERROR: Enter only number to attack')
            rounds += 1

            if win:
                print('Game Over')
                print('You win.')
                print('Thanks for playing!')
                break

        print('\n=== Round {} ==='.format(rounds + 1))
        print("Opponent's Move")
        print("\nEnemy's turn to attack your unit!")
        AI_attack_result = enemy_turn(units, enemy_units)
        for attack_result in AI_attack_result:
            if int(attack_result[2]) > 0:
                print(f"{attack_result[0]} attacked {attack_result[1]} with {attack_result[2]} damage.")
            else:
                print(
                    f"{attack_result[0]} attacked with {abs(attack_result[2])} damage, but {attack_result[1]} avoided.")

        print('\nYour Units HP Now:')
        for p in range(len(units)):
            print(f'{p + 1}. {units[p].get_char_name()}: {units[p].get_hp()}')

        if players_dead(units):
            print('\nYour unit has been killed! Play the game again?')
            print('Game Over')
            print('You lose')
            print('Thanks for playing!')
            return win
        rounds += 1

    '''
    game_over = False
    turn = 0
    while not game_over:
        print("It's your turn  {0} {1}. Please select an AI to attack:".format(chars[turn].c, chars[turn].name))
        possible = []
        for i in range(len(chars)):
            if not i == turn:
                possible.append(i)
                print(" - ({0}): {1} named {2}".format(i, chars[i].c, chars[i].name))
        sel = -1
        while not sel in possible:
            s = input('Selection: ')
            try:
                sel = int(s)
            except:
                print("That's not a valid choice")

        chars[turn].attack(chars[sel])
        if chars[sel].stats['HP'] <= 0:
            game_over = True
            print("Game Over.".format(chars[sel].name))
        turn += 1
        if turn == len(chars):
            turn = 0
    '''


# Game System:
def game_system():
    # Player Units Setup
    # Create number of unit to be made
    create_no_unit()

    # Creating user's unit (Name, type, attributes to be randomized)
    create_unit()

    # Create AI's unit
    create_AI()


# Start Page of game
title = 'Welcome to Group 8 PSB Battle Game!'.center(78)
print(title)
print("""            
██████╗░░██████╗██████╗░  ██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗
██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝
██████╔╝╚█████╗░██████╦╝  ██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░
██╔═══╝░░╚═══██╗██╔══██╗  ██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░
██║░░░░░██████╔╝██████╦╝  ██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗
╚═╝░░░░░╚═════╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝""")
print('Please select the following choices to begin the game:')
print('1. New Game (Create Your Units Here)')
print('2. Play the Game')
print('3. Quit the Game')
print("4. Rules")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def start_menu():  # Options of the beginning of game
    

    while True:
        try:
            choice = int(input('Enter the choice [1-4]: '))
            if choice == 1:

                if len(all_unit_names) >= 3 and len(all_unit_types) == unit_amount:
                    restart_game()
                else:
                    game_system()

            # If no. of character has not been 3 and want to play game:
            elif choice == 2 and len(all_unit_names) < 3:
                print('\n' + "You haven't created your units. Create your units and try again.")

            # No. of character = 3 and meet the condition to play game:
            elif choice == 2 and len(all_unit_names) >= 3:
                begin_game(all_unit_attributes)

            # If user want to quit the game:
            elif choice == 3:
                print('\n' + 'See you :(')
                break

            # Display game rules    
            elif choice == 4:
                print('\n'," GAME RULES ".center(51,"="),'\n')
                print("1. Select a unit (Warrior/w) or (Tank/t) to play\n")
                print("2. Unit HP equals to less than 0 will be defeated\n   Whoever destroys the unti will be declared the winner\n")
                print("3. If unit's rank up, additional 10HP will be added to their total ")

                d = [ ["Health Point", 100, 100],
                    ["Attack Point", "Range between 5-20", "Range between 1-10"],
                    ["Defence Point", "Range between 1-10", "Range between 5-15"]]

                print(tabulate(d, headers=["Attribute", "Warrior", "Tanker"]))

                print('\n1. New Game (Create Your Units Here)')
                print('2. Play the Game')
                print('3. Quit the Game')


            # If user's input is not in range between 1-3, even though is integer:
            else:
                print('\n' + 'Invalid Input. Select the appropriate choices [1-4] and try again.')

        # If User's Input not Integer [1-3]:
        except ValueError:
            print('\n' + 'Invalid Input. Select the appropriate choices [1-4] and try again.')


def main():
    start_menu()


main()
