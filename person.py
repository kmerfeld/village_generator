from family import family
#!/usr/bin/env python3
import random

class person:

    # id number
    id_number = 1
    #default stats
    # name
    first_name = ""
    middle_name = "Bobber"
    last_name   = "Bobbert"
    
    #family info
    dad_family = family() 
    mom_family = family() 

    #clothing
    head        = "cloth hat"
    eyes        = ""
    neck        = ""
    shoulders   = ""
    back        = ""
    torso       = "cloth shirt"
    waist       = "belt"
    arms        = ""
    ring1       = ""
    ring2       = ""
    legs        = "cloth pants"
    feet        = "leather pants"

    #appearence
    race        = "human"
    skin_color  = "white"
    eye_color   = "brown"
    hair_color  = "brown"
    height      = "5.5" #in feet
    weight      = "150" #in pounds
    age         = "35"
    gender      = ""
    birth_family   = "Traveler"
    attractiveness = 10

    #stats
    strength = 0
    dexterity = 0
    constitution = 0
    intellegence = 0
    wisdom = 0
    charisma = 0
    def __init__(self,f_name, m_name,l_name, gend):
        self.first_name = f_name    
        self.middle_name = m_name 
        self.last_name = l_name
        self.gender = gend
     
        self.strength        = random.randint(1, 20) 
        self.dexterity       = random.randint(1, 20) 
        self.constitution    = random.randint(1, 20) 
        self.intellegence    = random.randint(1, 20) 
        self.wisdom          = random.randint(1, 20) 
        self.charisma        = random.randint(1, 20) 

    
    def is_related(self, person):
        if person.last_name == self.last_name:
            return True 
        return False

    
    

    def to_string(self):
         return(self.first_name 
                 + " " + self.middle_name 
                 + " " + self.last_name 
                 + " " + self.gender )
