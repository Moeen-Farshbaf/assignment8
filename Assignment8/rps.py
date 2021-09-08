import random

options = ['rock','paper','scissor']

scoreboard = {'user':0, 'computer':0}
def endgame():
    if scoreboard['computer'] >= scoreboard['user']:
        print('Computer won scoring '+str(scoreboard['computer'])+' you scored: '+str(scoreboard['user']))
    elif scoreboard['user'] >= scoreboard['computer']:
        print('User won scoring '+str(scoreboard['user'])+' computer scored: '+str(scoreboard['computer']))
    elif scoreboard['user'] == scoreboard['computer']:
        print('Tie!')
        will = input('Wanna play another round to determine the winner?(y/n)')
        if will == 'y':
            rps()
        if will == 'n':
            print('Goodluck')

def judge(x,y):
    return  x+y

def rps():
        computer_choice = random.choice(options)
        user_choice = input('Rock, paper, scissor?')

        winner = ['rockscissor', 'paperrock', 'scissorpaper']
        tie = ['rockrock', 'paperpaper', 'scisorscissor']



        user_win  = judge(user_choice, computer_choice)
        pc_win = judge(computer_choice, user_choice)


        if user_win in winner:
            print('User earned a score')
            scoreboard['user'] +=1
        elif pc_win in winner:
            print('Computer earned a score')
            scoreboard['computer'] +=1
        elif pc_win or user_win in tie:
            print('This round is a tie')
active = True
while active:

    for i in range(10):
        rps()

    endgame()
