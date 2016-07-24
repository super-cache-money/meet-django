import random

def checkGuess(solution, guess):
    solution = solution.lower()
    guess = guess.lower()

    correct_position_and_colour_count = 0
    correct_color_count = 0

    # we'll use this string to check for color (not necessarily position) matches against guess
    # if there's a match, we remove the character, otherwise we'll get duplicates
    unmatched_solution = solution

    for charPos in range(len(guess)):

        # check for correct position and colour
        if guess[charPos] == solution[charPos]:
            correct_position_and_colour_count += 1

        # check for correct colour only
        if guess[charPos] in unmatched_solution:
            correct_color_count += 1
            # remove matched colour to dedupe matches
            unmatched_solution.replace(guess[charPos], '', 1)

    # when a colour is found in the correct position, it's also counted as just a correct colour
    # that's why we need to subtract the correct_position_and_colour_count to get instances where only Colour was correct
    return {
        'correct_color': correct_color_count,
        'correct_position_and_color': correct_position_and_colour_count
    }


def generate_solution():
    key = ''
    length = 4
    for i in range(length):
        key = '%s%s' % (key, random.choice('RGBY'))
    return key
