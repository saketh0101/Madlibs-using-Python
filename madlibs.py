# string concatenation (aka how to put the string together ) 
# suppose we want to create a string that says "subscribe to ______"
#youtuber = "Saketh" # some string variable


# a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Dear Saketh, I know about you, that you are {adj}, Try to be {verb1}, and make your life as {verb2} as {verb2}. And Be like a {famous_person} "
print(madlib)