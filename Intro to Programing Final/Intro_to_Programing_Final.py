import random
## This is the global verables

class Hero:
    def __init__(self, name, strength, charisma, intelligence, vitality, melee_bonus, range_bonus, gold, orc_relationship, elf_relationship, dwarf_realtionship, human_relationship, hit_points, level):
        self.name= name
        self.stats = dict()
        self.stats['strength'] = strength
        self.stats['charisma'] = charisma
        self.stats['intelligence'] = intelligence
        self.stats['vitality'] = vitality
        self.stats['melee_bonus'] = melee_bonus
        self.stats['range_bonus'] = range_bonus
        self.stats['gold'] = gold
        self.stats['orc_relationship'] = orc_relationship
        self.stats['elf_relationship'] = elf_relationship
        self.stats['dwarf_relationship'] = dwarf_realtionship
        self.stats['human_relationship'] = human_relationship
        self.stats['hit_points'] = hit_points + vitality
        self.stats['level'] = level
        self.weapon = Weapon("fist",5, 10, True)
    def get_name(self):
        return self.name

    def set_stat(self, stat_name, value):
        assert stat_name in self.stats, f"Invalid stat {stat_name}"

        self.stats[stat_name] = value
    def get_stat(self, stat_name):
        assert stat_name in self.stats, f"Invalid stat {stat_name}"
        return self.stats[stat_name]
    def add_stat(self, stat_name, value):
        assert stat_name in self.stats, f"Invalid stat {stat_name}"

        self.stats[stat_name] += value
    def print_character(self):
        for stat in ['name', 'gold']:
            print(stat, self.stats[stat])
        self.weapon = Weapon("fist", 5, 10, True) 
    
    def __str__(self):
        return f"{self.name} {self.stats['hit_points']} {self.stats['strength']} {self.stats['charisma']} {self.stats['intelligence']} {self.stats['vitality']} {self.stats['melee_bonus']} {self.stats['range_bonus']} {self.stats['gold']} {self.stats['orc_relationship']} {self.stats['elf_relationship']} {self.stats['dwarf_relationship']} {self.stats['human_relaionship']} {self.stats['level']}"

    def is_alive(self):
        return self.stats['hit_points'] > 0

    def take_damage(self, damage):
        self.stats['hit_points'] -= damage
        if self.stats['hit_points'] < 0:
            self.stats['hit_points'] = 0
        print(f"{self.name} takes {damage} damage. New health is {self.stats['hit_points']}.")

    def equip(self, weapon):
        self.weapon = weapon

    def attack(self, enemy_combatants, is_attacking_melee):
       chance_to_hit = self.weapon.to_hit_target()
       if self.get_equipped_weapon().is_melee():
            chance_to_hit += self.melee_bonus
            if is_attacking_melee and chance_to_hit > enemy_combatants.melee_armor:
                enemy_combatants.melee_take_damage(1)
            elif is_attacking_melee == False:
                chance_to_hit -= 20
                if chance_to_hit > enemy_combatants.ranged_armor:
                    enemy_combatants.range_take_damage(1)
            print("you have missed")

       else:
            chance_to_hit+= self.range_bonus
            if is_attacking_melee:
                chance_to_hit -= 20
                if chance_to_hit > enemy_combatants.melee_armor:
                    enemy_combatants.melee_take_damage(1)
            elif chance_to_hit > enemy_combatants.ranged_armor:
                    enemy_combatants.range_take_damage(1)

    def get_equipped_weapon(self):
        return self.weapon

class Weapon:
    def __init__(self, name, base_to_hit, random_to_hit, is_melee):
        self.name = name
        self.base_to_hit = base_to_hit
        self.random_to_hit = random_to_hit
        self.is_melee_weapon = is_melee

    def __str__(self):
        return f"{self.name} {self.base_to_hit} - {self.base_to_hit + self.random_to_hit}"

    def to_hit(self):
        to_hit_target = self.base_to_hit + random.randrange(0, self.random_to_hit)
        return to_hit_target

    def is_melee(self):
        return self.is_melee_weapon

    
class Enemy_Battlefield:
    def __init__(self, melee_enemies, ranged_enemies, melee_armor, ranged_armor):
        self.melee_enemies = melee_enemies
        self.ranged_enemies = ranged_enemies
        self.melee_armor = melee_armor
        self.ranged_armor = ranged_armor

    def is_alive(self):
        return self.melee_enemies > 0 and self.ranged_enemies > 0
    def range_damage(self,hero):
        if hero.get_equipped_weapon().is_melee():
            hero.take_damage(random.randrange(10,15))
        else:
            hero.take_damage(10)

    def melee_damage(self, hero):
        if hero.get_equipped_weapon().is_melee():
            hero.take_damage(10)
        else:
            hero.take_damage(random.randrange(10,15))

    def attack(self, hero):
        for ii in range(self.ranged_enemies): 
            self.range_damage(hero)
        for ii in range(self.melee_enemies):
            self.melee_damage(hero)
    def melee_take_damage(self, deaths):
        self.melee_enemies -= deaths
        if self.melee_enemies < 0:
            self.melee_enemies = 0
    def range_take_damage(self, deaths):
        self.ranged_enemies -= deaths
        if self.ranged_enemies < 0:
            self.ranged_enemies = 0



sword = Weapon("sword", 0, 100, True)
bow = Weapon("bow", 0, 100, False)

def input_non_empty_string(promt):
    while True:
        user_input = input(promt)
        if len(user_input) > 0:
            break
        print('Input can not be empty.')
    return user_input
def input_choices(prompt, choices):
    print(prompt)
    for item_num, item in enumerate(choices):
        print('   ', item_num + 1, item)
    selection = input_number("choice: ",1,len(choices))
    return selection

def input_number(prompt, min, max):
    while True:
        input_str = input(prompt)
        if input_str.isdigit():
          
            selection = int(input_str)
            if selection >= min and selection <= max:
                break
        print(f"Invalid input must be between {min} and {max} ")
    return selection 
## Story Starts
def main():
    print(
    f"The Continent of Silthia was broken into 4 different kingdoms.  These Kingdoms were: The Gorthomons (Dwarfs) , The Warsong(Orcs), The Timberwolfs(Elfs), and Foxborough(Humans).\n"  
    f"Foxborough while quite advanced for their race and sees themselves quite highly the rest of the Continent The Vulpigs.  The nations had been at war with each other for millennia.\n" 
    f"This war was over The Timberwolfs wanting Warsong to back off their deforest station quest.  While the Gorthomons wanted the mines that resided in the Warsong Territory.\n" 
    f"Warsong just wanted territory and slaves. Timberwolfs also wanted the libraries that resided in the core of Gorthomon. \n" 
    f"Foxborough while maintaining relatively neutrals grounds would eventually be brought into this war after raid by the Timberwolfs and sacrifices done by the Warsong.\n"
    f"There had been a time of peace for about 2 years while all the nations battled Pyeonghwa. Now it has been 100 years since the peace.  \n"
    )
    input("During dialong or narration please press enter continue.")

    ## Character Creation time
    ## Naming Character
    
    print("Time to create your Character")
    name = input_non_empty_string("Please enter your character's name: ")
    hero = Hero(name,0,0,0,0,40,40,0,0,0,0,50,100,1 )
    
    total_combatants = Enemy_Battlefield(5,5,50,50)
    total_combatants.attack(hero)
    
    ##Chosing Background
               
    background_choice = input_choices("Please choose a background", ["You grew up as an indentured servant in Gorthomon.", "You grew up a slave to the Orcs.", "You grew up as book keep in Timberwolf.", "You grew up as a prince in Foxborough"])
    if background_choice==1:
        hero.add_stat('strength', 5)
        hero.add_stat('dwarf_relationship', 5)
    elif background_choice==2:
        hero.add_stat('vitality', 5)
        hero.add_stat('orc_relationship',5)
    elif background_choice==3:
        hero.add_stat('intelligence',5)
        hero.add_stat('elf_relationship', 5)
    elif background_choice==4:
        hero.add_stat('charisma', 5)
        hero.add_stat('gold',100)
    else:
        assert False, "Bug Here"



    ## Choosing Training
    training_choice = input_choices("Please chose a training. After leave home you chose to learn the art of:", ["Range fighting while traveling with a hunting party.", "Sword fighting while being a squire for some traveling Knights.", "Negotiation while traveling with a party of traders."])
        
    if training_choice == 1:
        hero.add_stat('range_bonus', 5)
    elif training_choice == 2:
        hero.add_stat('melee_bonus', 5)      
    elif training_choice == 3:
        hero.add_stat("charisma", 5)      
    else:
        assert False, "Bug Here"

    ## Time for the Game to Start
    ## Story Time
    print("Present Day:\n You have been summoned before the King of Foxborough")
    input()
    print(
        F"{hero.name}: Hello, King Remzii, you have summoned me today\n"
        "King: Yes, PN I have summoned you today to ask you to deliver my daughter Gorthomon for a marriage peace deal.\n"  
        "You will have to travel undercover as it can not be known that we have a peace deal in the works with the Dwarves.\n"
        "we would incur an attack and full-on invasion from the Elfs is this was to become known.\n"
        )
    ## First Conversation playing has control in
    while True:
        conversation_choice = input_choices("",["Why would this incur an invasion?", "Why did the Dwarves agree to this deal?", "Ok Sir I will make sure she gets there unharmed and secretly."])
        if conversation_choice == 1:
            print("Elfs have long for a true reason to invade us.  A human and Dwarf alliance would be just the thing they need.")
        elif conversation_choice==2:
            print("They have been one of the nations that have often been helpful to us when we needed it but they are also tired of fighting a war on three fronts so turning it into a 2 war front is massive for them.")
        elif conversation_choice==3:
            print("King: You will at Dusk")
            break
        else:
            assert False, f" bad {conversation_choice}"

    print(f"you rest until it is dusk then leave with the Princess.\n As you cross the boarders a group of orcs attack.")

    ## First Battle
    enemy_battlefield=10
    def Fight(hero):
        while hero.is_alive() and enemy_battlefield >= 0:
    
            print(enemy_battlefield)
            print(hero_health)
            print(turn_counter)
            if hero_health <= 0:
                print("You have been beaten back and the princess kidnapped.  You now must go rescue her.")
                break
            if enemy_battlefield ==0:
                print("You have beaten them back! Now enjoy and continue")
                break

            battle_discussion=input_choices(["Ranged Attack", "Melee Attack", "Discussion", "Defend"])

            if battle_discussion==1:

                hero.equip(bow)
                hero.attack(enemy_battlefield)
                range_attack=hero_bow_bonus+random.randrange(100)
                if range_attack >= 10:
                        enemy_battlefield-=1
                if enemy_battlefield ==0:
                    print("You have beaten them back! Now enjoy and continue")
                    break

                enemy_attack=random.randrange(100)
                if enemy_attack >= 50:
                    hero_health -=15

            if battle_discussion==2:
                melee_attack=hero_sword_bonus+random.randrange(100)
                if melee_attack >= 60:
                        enemy_battlefield-=1
                if enemy_battlefield ==0:
                    print("You have beaten them back! Now enjoy and continue")
                    break
                enemy_attack=random.randrange(100)
                if enemy_attack >= 50:
                    hero_health -=15

            if battle_discussion==3:
                discussion_attack=hero_char+random.randrange(100)
                if discussion_attack >= 60:
                        enemy_battlefield-=1
                if enemy_battlefield ==0:
                    print("You have beaten them back! Now enjoy and continue")
                    break
                enemy_attack=random.randrange(100)
                if enemy_attack >= 50:
                    hero_health -=15

            if battle_discussion==4:
                enemy_attack=random.randrange(100)
                if enemy_attack >= 75:
                    hero_health -=15
                else:
                    print("You have succesfully defended agsint their attacks. ")
           
            if battle_discussion<1 or battle_discussion>5:
                print("This is not an option")
            else:
                assert False, "Bug Here"



    print("You have been beaten back and the princess kidnapped. Your Journey ends here.")

main()   


