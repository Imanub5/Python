# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Iman"
print( "Hello", name, "!")   # with a comma
print( "Hello "  + name + "!")  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 1
print ("Hello, 1") # with a comma
print ("Hello" +str(1) + "!" ) # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "Halal Munchies"
fave_food2 = "Dumplings"
print ("I love to eat {} and {}". format(fave_food1,fave_food2) ) # with .format()
print (f"i love to eat {fave_food1} and {fave_food2}" ) # with an f string
# Ninja Bonus: Print favorite TV Shows with the Shows in a variables
fave_Shows1 = "Cobra Kai"
fave_Shows2 = "Money Heist"
print ("My Favorite TV Shows are {} and {}". format(fave_Shows1,fave_Shows2) )
print (f"My Favorite TV Shows are {fave_Shows1} and {fave_Shows2}" )
