'''
Initial: A for Rock, B for Paper, and C for Scissors
response: X for Rock, Y for Paper, and Z for Scissors
'''
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def rps_outcome(initial, response):
    '''
    score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
    '''
    rps_scoring = {'A':{'X':3,'Y':6,'Z':0},'B':{'X':0,'Y':3,'Z':6},'C':{'X':6,'Y':0,'Z':3}}

    logging.info(f'{initial}:{response} scores {rps_scoring[initial][response]}')

    return rps_scoring[initial][response]

def rps_shape_score(initial):
    '''
    score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    '''
    shape_scores = {'X':1, 'Y': 2, 'Z':3}
    logging.info(f'{initial} scores {shape_scores[initial]}')
    return shape_scores[initial]

def rps_total(initial, response):
    return rps_outcome(initial, response) + rps_shape_score(response)

def score_guide(guide):
    score = 0
    logging.info(f'Guide is {guide}')
    for line in guide.splitlines():
        logging.info(f'line is {line}')
        round = tuple(line.split(' '))
        logging.info(f'Round is {round}')
        score += rps_total(round[0], round[1])
        logging.info(f'score is now {score}')
    return score

if __name__ == '__main__':
    with open('guide.txt','r') as file:
        the_guide = file.read()
        print(f'outcome is: {score_guide(the_guide)}')