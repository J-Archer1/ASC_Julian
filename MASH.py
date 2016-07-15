from random import *
buildings = ["Mansion","Apartment","Shack","House"]
incomes = ["$.01","$1","$1000","A small loan of a million dollars"]
cars = ["Lamborghini","Porsche","BMW","Rust-bucket","Clown car","Mini-van"]
jobs= ["Doctor", "Lawyer","Waitress/Waiter","Astronaut","Unemployed person","Game Designer","Computer Scientist"]
lifeadvice= ["get a life", "pray to Julian, the GOD", "get more sleep","don't waste your time playing this", "brush yo' stank yellow teeth", "PUT ON SOME DEODORANT"]
user_input = []
get_name=raw_input("What's your name?")
user_input.append(get_name)
user_input = []
get_input=raw_input("What kind of house do you want to live in?")
user_input.append(get_input)
user_input = []
get_input=raw_input("How much do you want to make a year?")
user_input.append(get_input)
user_input = []
get_input=raw_input("What kind of car do you want?")
user_input.append(get_input)
user_input = []
get_input=raw_input("What job do you see yourself doing in 10 years?")
user_input.append(get_input)
rand_building=randint(0,len(buildings)-1)
rand_income=randint(0,len(incomes)-1)
rand_car=randint(0,len(cars)-1)
rand_job=randint(0,len(jobs)-1)
rand_lifeadvice=randint(0,len(lifeadvice)-1)
print("Hello,", get_name,"!")
print("You will live in a", buildings[rand_building])
print("You will make", incomes[rand_income],"a year.")
print("You will drive a", cars[rand_car])
print("You will be a(n)",jobs[rand_job])
print("Also, do youself a favor and", lifeadvice[rand_lifeadvice])