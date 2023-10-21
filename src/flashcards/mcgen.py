import random
import samplesets 
from pprint import pprint

def createQuiz(deck):
    pprint(deck)
    terms = []
    definitions = []
    newquiz = []

    # Insert all terms and their respective correct definitions into the quiz
    for i in range(len(deck)):
        newquiz.append({
            'question': deck[i]['t'],
            'answeroptions': [{'option': deck[i]['d'], 'isCorrect': True}]
        })
        terms.append(deck[i]['t'])
        definitions.append(deck[i]['d'])

    # Go through all quiz questions
    for i in range(len(newquiz)):
        # Insert other random definitions (up to 3 and at least 1) for each term
        if len(definitions) < 4:
            # Go through all definitions
            for j in range(len(definitions)):
                # If not the correct definition, add the definition to options
                if definitions[j] != newquiz[i]['answeroptions'][0]['option']:
                    newquiz[i]['answeroptions'].append({'option': definitions[j], 'isCorrect': False})
        else:
            # Add a limit of 3 definitions
            for j in range(3):
                matches = True
                randef = 'ERROR'
                # Get a random definition until it's not already in options
                while matches:
                    randef = random.choice(definitions)
                    # Iterate through options
                    for x in range(len(newquiz[i]['answeroptions'])):
                        duplicate = False
                        for y in range(len(newquiz[i]['answeroptions'])):
                            if randef == newquiz[i]['answeroptions'][y]['option']:
                                duplicate = True
                        if not duplicate:
                            matches = False
                newquiz[i]['answeroptions'].append({'option': randef, 'isCorrect': False})
        random.shuffle(newquiz[i]['answeroptions'])

    # Shuffle quiz questions and return quiz
    random.shuffle(newquiz)
    print('finished creating quiz:')
    pprint(newquiz)
    return newquiz

createQuiz(samplesets.sampleSet(0))
