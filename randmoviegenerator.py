#We need this
from random import *
#Random words for movies
list1=["The Return of", "The Rise of", "The Downfall of", "The Army of", "The Massacre of","The Tale of","The Story of","The Revenge of", "The Adventure of"]
list2=["the Hipster","the Killer", "the Evil","the Goofy", "the Annoying", "the Violent", "the Cunning", "the Sneaky"]
list3=["Pokemon Go Trainers", "Giraffes", "Scouts", "Soldiers", "Pyros","Demolitions Man", "Heavy Weapons Guy", "Engineers", "Spies", "Medics","Snipers"]
#Randomizing...
rand_list= randint(0,len(list1)-1)
rand_list2= randint(0,len(list2)-1)
rand_list3= randint(0,len(list3)-1)
#It's finished
print(list1[rand_list],list2[rand_list2],list3[rand_list3])