## This is the global verables
hero_name="Bill"
hero_str=0 
hero_char=0
hero_int=0
hero_vit=0
hero_sword_bonus=0
hero_bow_bonus=0
hero_gold=0
hero_health=100+hero_vit
hero_lvl=1
hero_orc_relationship=0
hero_elf_relationship=0
hero_dwarf_relationship=0
hero_human_relationship=50
## important random
import random

## Story Starts

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
print("Time to create your Character")

hero_name=input(str("Plesae enter your charcter's name: "))

while True:
           background_choice=int(input("Please choose a background\n 1-You grew up as an indentured servant in Gorthomon.\n 2-You grew up a slave to the Orcs.\n 3-You grew up as book keep in Timberwolf. \n 4-You grew up as a prince in Foxborough\n"))
           if background_choice==1:
               hero_str+=5
               hero_dwarf_relationship+=5
               break

           elif background_choice==2:
               hero_vit+= 5
               hero_orc_relationship+=5
               break

           elif background_choice==3:
               hero_int+=5
               hero_elf_relationship+=5
               break

           elif background_choice==4:
               hero_char+=5
               hero_gold+=100
               break

           else:
               print("Please chose one of the avalabe choices")

while True:
    training_choice=int(input("Please chose a training.\n After leave home you chose to learn the art of:\n 1-Range fighting while traveling with a hunting party. \n 2-Sword fighting while being a squire for some traveling Knights \n 3-Negotiation while traveling with a party of traders. \n"))
    if training_choice==1:
        hero_bow_bonus+=5
        break
    elif training_choice==2:
        hero_sword_bonus+=5
        break
    elif training_choice==3:
        hero_char+=5
        break
    else:
        print("Please chose one of the avalabe choices")

print("Present Day:\n You have been summoned1 before the King of foxborough")
input()
print(
    F"{hero_name}: Hello, King Remzii, you have summoned me today\n"
    "King: Yes, PN I have summoned you today to ask you to deliver my daughter Gorthomon for a marriage peace deal.\n"  
    "You will have to travel undercover as it can not be known that we have a peace deal in the works with the Dwarves.\n"
    "we would incur an attack and full-on invasion from the Elfs is this was to become known.\n"
    )
while True:
    conversation_choice=int(input("1-Why would this incur an invasion?\n 2-Why did the Dwarves agree to this deal?\n 3-Ok Sir I will make sure she gets there unharmed and secretly.\n"))
    if conversation_choice==1:
        print("Elfs have long for a true reason to invade us.  A human and Dwarf alliance would be just the thing they need.")
    elif conversation_choice==2:
        print("They have been one of the nations that have often been helpful to us when we needed it but they are also tired of fighting a war on three fronts so turning it into a 2 war front is massive for them.")
    elif conversation_choice==3:
        print("King:  You will at Dusk")
        break
    else:
        print("Please choose a valid option")

print(f"you rest until it is dusk then leave with the Princess.\n As you cross the boarders a group of orcs attack.")

   