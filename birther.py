#!/usr/bin/env python3
import random
from person import *
from family import *
#read in file




def make_person():
    g = random.randint(0,1)
    fname = ""
    mname = ""
    lname = ""

    if g == 1:
        gender = "male"
        lname = random.choice(l_names)
        mname = random.choice(male_m_names)
        fname = random.choice(male_f_names)
    else:

        gender = "female"
        lname = random.choice(l_names)
        mname = random.choice(female_m_names)
        fname = random.choice(female_f_names)
    


    p = person(fname,mname,lname,gender)



def create_people(config):
    config = open("config.txt").read().splitlines()
    #config= f.readlines()

    #catagorise config file

    male_f_names = []
    male_m_names = []
    l_names = []
    female_f_names = []
    female_m_names = []
    number_villagers = 2
    race = []
    people = []

    catagory = ""


    #TODO: make this way less shit
    for i in config:
        #skip empty lines
        if i == "":
            continue
        #set catagory
        elif i.startswith("["): #and i.endswith("]"):
            if i == "[male_first_names]":
                catagory = "male_f_names"
            if i == "[male_middle_names]":
                catagory = "male_m_names"
            if i == "[last_names]":
                catagory = "l_names"
            if i == "[female_first_names]":
                catagory = "female_f_names"
            if i == "[female_middle_names]":
                catagory = "female_m_names"
            if i == "[number_villagers]":
                catagory = "number_villagers"

        #we have a normal line
        else:
            if catagory == "male_f_names":
                male_f_names.append(i)
            if catagory == "male_m_names":
                male_m_names.append(i)
            if catagory == "female_f_names":
                female_f_names.append(i)
            if catagory == "female_m_names":
                female_m_names.append(i)
            if catagory == "l_names":
                l_names.append(i)
            if catagory == "number_villagers":
                number_villagers = i
            

    for x in range(int(number_villagers)):
                p = make_person()
                people.append(p)

    for x in range(len(people)):
        print(people[x].to_string())

    return people


def get_pair(males, females):
    x = random.randint(0,len(males) -1)
    y = random.randint(0,len(females) -1)
    
    #TODO: make this more than just random chance to decide.
    #maybe use wealth or something

    print(x,y)
    print("males left   ", len(males))
    print("females left ", len(females))

    #congrats to the happy couple
    pair = (males[x], females[y])
    males.pop(x)
    females.pop(y)
    return pair


def make_familes(people):
    #split male and female
    males = []
    females = []
    for x in people:
        if x.gender == "male":
            males.append(x)
        else:
            females.append(x)
    print("### Males")
    print (len(males))

    print("### Females")
    print (len(females))

    #TODO: currently this will marry everyone possible. 
    #this should be scaled back later
    pairs = []
    if len(males) > len(females):
        for i in females:
            pairs.append(get_pair(males, females))
    else:
        for i in males:
            pairs.append(get_pair(males, females))

    print (len(pairs))
    for item in pairs:
        print (item[0].to_string(), ", ", item[1].to_string())


    #ok, now we have a few pairs, we will make some families
    for i in pairs:
        #x =  family(i[0],i[1])
        x = family.__init__(i[0],i[1])
        
    
    #lets make some babies *giggidy*

