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
input("During dialong or narration please press space continue.")

## Character Creation time
print("Time to create your Character")

hero_name=input(str("Plesae enter your charcter's name"))

while True:
           background_choice=int(input("Please choose a background\n 1-You grew up as an indentured servant in Gorthomon.\n 2-You grew up a slave to the Orcs.\n 3-You grew up as book keep in Timberwolf. \n 4-You grew up as a prince in Foxborough"))
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

print("test")
               
   