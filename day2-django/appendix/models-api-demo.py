from mastermind.models import *

#No games in the system yet
Game.objects.all()

#so lets create a new game
game1 = Game(solution="RGBY",handle="mcrainman")
# we can interpret this as an instantiation of our model (which can be thought of as a class)

#lets save this to the database
game1.save()

#now that it has been saved in the database, it will have automatically been assigned a primary key (this is a setting specified in the models.py file -- check if you don't remember)
game1.id

#let's make another game
Game(solution="BGRG",handle="mcrainman").save()

#Django provides a built in database lookup API that is driven by keyword arguments

Game.objects.filter(id=1)
Game.objects.filter(solution__startswith="BG")

# Now let's give the Game a couple of "guesses". The create call constructs a new
# Attempt object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Attempt object. Django creates
# a set to hold the "other side" of a ForeignKey relation (remember that this is a "One-to-Many" relation)
# (e.g. a question's choice) which can be accessed via the API.
g = Game.objects.get(id=1)
# Display any attempts from the related object set -- none so far.
g.attempt_set.all()

#Let's create a few attempts
g.attempt_set.create(guess="BBBB")
g.attempt_set.create(guess="BBBR")
g.attempt_set.create(guess="RGBY")

#and let's see all the game attempts
g.attempt_set.all()

#now lets make a query
query = g.attempt_set.filter(guess__startswith="BB")

#and check
query

# and now we delete,
query.delete()
#so that we keep our perfect record

