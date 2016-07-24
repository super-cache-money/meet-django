from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from mastermind_engine import check_guess
from mastermind.models import Game, Attempt

def play(request, id):

    # Let's get the current Game from the database
    curr_game = Game.objects.get(id=id)

    if request.method == "POST":
        pos_one = request.POST['pos_one']
        pos_two = request.POST['pos_two']
        pos_three = request.POST['pos_three']
        pos_four = request.POST['pos_four']

        guess = pos_one + pos_two + pos_three + pos_four


        attempt = Attempt() # Let's create a new attempt instance

        attempt.game = curr_game # associate attempt to current game
        attempt.guess = guess # set actual guess
        attempt.save() # persist

        # Check if the attempt is correct feedback.correct_position_and_color is equal to 4

    # let's pull out all the attempts associated to this game
    attempts = Attempt.objects.filter(game=curr_game)


    for attempt in attempts: # calculate feedback for each guess
        attempt.result = check_guess(curr_game.solution, attempt.guess)

    context = RequestContext(request, { 'attempts': attempts})

    return render(request, 'play_full.html', context)
