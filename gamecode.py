import sqlite3
from random import random

db = sqlite3.connect('database.db')
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
db.row_factory = dict_factory

def get_random_enemy():
    cursor = db.cursor()
    res = cursor.execute('SELECT * FROM enemies ORDER BY RANDOM() LIMIT 1').fetchone()
    print(res)

def roll_character(player):
    pass
    # get the rank needed
    
    # get random character based on rank

    # if already have, increase count

    # else create new player_character

    # return character

def get_random_rank():
    rate = random() * 100
    if rate < 30: # 30%
        return 1
    if rate < 60: # 30%
        return 2
    if rate < 85: # 25%
        return 3
    if rate < 95: # 10%
        return 4
    if rate < 99: # 04%
        return 5
    return 6      # 01%

def get_action_sequence(state):
    pass
    # check who goes first

    # check accuracy of first attack

    # calculate damage

    # if char/enemy dead, end sequence

    # check accuracy of second attack

    # calculate damage

    # if char/enemy dead, end sequence

    # return final sequence

def calculate_damage(attacker, defender):
    pass
    '''
    love_score = (love / 25) MAX 100
    level_score = level * (rank * 0.2) MAX 100
    item_score = attacker_attack * ((100 + item)/100)
    mul = love_score * level_score
    acting_atk = (attacker_attack + item_score) * mul
    damage = (int) ((acting_atk/acting_def) * 10) * rand
    '''