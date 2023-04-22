from random import random, randrange, choice
from gamecode import *
from faker import Faker
import sqlite3
import string

db = sqlite3.connect('database.db')
cursor = db.cursor()

fake = Faker()

def get_random_image():
    return 'data:image/png;base64,' + ''.join(choice(string.ascii_letters) for x in range(1024))

def get_character_rank(char):
    sum = char['HP'] + char['P_ATK'] + char['A_ATK'] + char['M_ATK'] + char['P_DEF'] + char['A_DEF'] + char['M_DEF'] + char['R_DEF'] + char['SPEED']
    avg = sum / 9
    if avg < 50:
        return 1
    if avg < 55:
        return 2
    if avg < 60:
        return 3
    if avg < 65:
        return 4
    if avg < 70:
        return 5
    return 6

# load characters
for i in range(100):
    char = {
        'NAME': fake.name(),
        'DESC': fake.sentence(),
        'RANK': None,
        'HP': randrange(25, 100, 5),
        'P_ATK': randrange(25, 100, 5),
        'A_ATK': randrange(25, 100, 5),
        'M_ATK': randrange(25, 100, 5),
        'P_DEF': randrange(25, 100, 5),
        'A_DEF': randrange(25, 100, 5),
        'M_DEF': randrange(25, 100, 5),
        'R_DEF': randrange(25, 100, 5),
        'SPEED': randrange(25, 100, 5),
        'SPRITE_IDLE_1': get_random_image(),
        'SPRITE_IDLE_2': get_random_image(),
        'SPRITE_P_ATK': get_random_image(),
        'SPRITE_A_ATK': get_random_image(),
        'SPRITE_M_ATK': get_random_image(),
        'SPRITE_DAMAGE': get_random_image(),
        'SPRITE_DODGE': get_random_image(),
        'SPRITE_VICTORY_1': get_random_image(),
        'SPRITE_VICTORY_2': get_random_image(),
        'SPRITE_DEFEAT_1': get_random_image(),
        'SPRITE_DEFEAT_2': get_random_image(),
    }
    char['RANK'] = get_character_rank(char)
    script = f'''
            INSERT INTO characters 
            (name, desc, rank, hp, p_atk, a_atk, m_atk, p_def, a_def, m_def, r_def, speed, sprite_idle_1, sprite_idle_2, sprite_p_atk, sprite_a_atk, sprite_m_atk, sprite_damage, sprite_dodge, sprite_victory_1, sprite_victory_2, sprite_defeat_1, sprite_defeat_2)
            VALUES
            ("{char['NAME']}", "{char['DESC']}", {char['RANK']}, {char['HP']}, {char['P_ATK']}, {char['A_ATK']}, {char['M_ATK']}, {char['P_DEF']}, {char['A_DEF']}, {char['M_DEF']}, {char['R_DEF']}, {char['SPEED']}, "{char['SPRITE_IDLE_1']}", "{char['SPRITE_IDLE_2']}", "{char['SPRITE_P_ATK']}", "{char['SPRITE_A_ATK']}", "{char['SPRITE_M_ATK']}", "{char['SPRITE_DAMAGE']}", "{char['SPRITE_DODGE']}", "{char['SPRITE_VICTORY_1']}", "{char['SPRITE_VICTORY_2']}", "{char['SPRITE_DEFEAT_1']}", "{char['SPRITE_DEFEAT_2']}")
            '''
    cursor.execute(script)

# load enemies
for i in range(10):
    char = {
        'NAME': fake.name(),
        'DESC': fake.sentence(),
        'HP': randrange(25, 100, 5),
        'ATK': randrange(25, 100, 5),
        'ATK_TYPE': choice(['P', 'A', 'M']),
        'P_DEF': randrange(20, 105, 5),
        'A_DEF': randrange(20, 105, 5),
        'M_DEF': randrange(20, 105, 5),
        'R_DEF': randrange(20, 105, 5),
        'SPEED': randrange(20, 105, 5),
        'SPRITE_IDLE_1': get_random_image(),
        'SPRITE_IDLE_2': get_random_image(),
        'SPRITE_ATK': get_random_image(),
        'SPRITE_DAMAGE': get_random_image(),
        'SPRITE_DODGE': get_random_image(),
        'SPRITE_VICTORY_1': get_random_image(),
        'SPRITE_VICTORY_2': get_random_image(),
        'SPRITE_DEFEAT_1': get_random_image(),
        'SPRITE_DEFEAT_2': get_random_image(),
    }
    script = f'''
            INSERT INTO enemies 
            (name, desc, hp, atk, atk_type, p_def, a_def, m_def, r_def, speed, sprite_idle_1, sprite_idle_2, sprite_atk, sprite_damage, sprite_dodge, sprite_victory_1, sprite_victory_2, sprite_defeat_1, sprite_defeat_2)
            VALUES
            ("{char['NAME']}", "{char['DESC']}", {char['HP']}, {char['ATK']}, "{char['ATK_TYPE']}", {char['P_DEF']}, {char['A_DEF']}, {char['M_DEF']}, {char['R_DEF']}, {char['SPEED']}, "{char['SPRITE_IDLE_1']}", "{char['SPRITE_IDLE_2']}", "{char['SPRITE_ATK']}", "{char['SPRITE_DAMAGE']}", "{char['SPRITE_DODGE']}", "{char['SPRITE_VICTORY_1']}", "{char['SPRITE_VICTORY_2']}", "{char['SPRITE_DEFEAT_1']}", "{char['SPRITE_DEFEAT_2']}")
            '''
    cursor.execute(script)

# load items
for i in range(100):
    char = {
        'NAME': fake.company(),
        'DESC': fake.sentence(),
        'RANK': None,
        'STAT_TARGET': choice(['P_ATK', 'A_ATK', 'M_ATK', 'P_DEF', 'A_DEF', 'M_DEF', 'R_DEF', 'SPEED']),
        'STAT_BONUS': randrange(10, 70, 10),
        'SPRITE': get_random_image()
    }
    char['RANK'] = int(char['STAT_BONUS']/10)
    script = f'''
            INSERT INTO items 
            (name, desc, rank, stat_target, stat_bonus, sprite)
            VALUES
            ("{char['NAME']}", "{char['DESC']}", {char['RANK']}, "{char['STAT_TARGET']}", {char['STAT_BONUS']}, "{char['SPRITE']}")
            '''
    cursor.execute(script)

# load players
for i in range(5):
    cursor.execute('INSERT INTO players DEFAULT VALUES')

db.commit()
cursor.close()
print('\nDatabase seeded successfully')