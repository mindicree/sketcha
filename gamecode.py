import sqlite3
from random import random
import bcrypt
from exceptions import *
import logging
import os
from datetime import datetime

# setup database configuration
db = sqlite3.connect('database.db', check_same_thread=False)
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
db.row_factory = dict_factory

# setup logging configuration
try:
    os.mkdir('logs')
except Exception as e:
    pass

try:
    logging.basicConfig(filename=f'logs\log_{datetime.now().strftime("%Y_%m_%d")}.txt',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info('Importing gamecode')
except Exception as e:
    print(e)
    exit()

def get_player_data(player_id):
    cursor = db.cursor()
    char_data = get_player_chars(cursor, player_id)
    item_data = get_player_items(cursor, player_id)
    player_data = cursor.execute(f'SELECT coins, streak FROM players WHERE rowid = {player_id} LIMIT 1').fetchone()
    cursor.close()
    return {
        'char_data': char_data,
        'item_data': item_data,
        'player_data': player_data
    }

def get_player_chars(cursor, player_id):
    script = f'''
    SELECT player_characters.rowid, * FROM player_characters
    INNER JOIN characters ON (player_characters.character_id = characters.rowid)
    WHERE player_characters.player_id = {player_id}
    ORDER BY level DESC
    '''
    res = cursor.execute(script).fetchall()
    return res

def get_player_items(cursor, player_id):
    script = f'''
    SELECT player_items.rowid, * FROM player_items
    INNER JOIN items ON (player_items.item_id = items.rowid)
    WHERE player_items.player_id = {player_id}
    ORDER BY name DESC
    '''
    res = cursor.execute(script).fetchall()
    return res
    
def get_random_enemy():
    cursor = db.cursor()
    enemy = cursor.execute('SELECT rowid, * FROM enemies ORDER BY RANDOM() LIMIT 1').fetchone()
    if not enemy:
        raise EnemyNotFoundException('Random enemy could not be retrieved')
    cursor.close()
    return enemy

def roll_character(player_id, rank=None):
    try:
        cursor = db.cursor()

        # get player info
        player = get_player_info(cursor, player_id)

        # get the rank needed
        rank = get_random_rank() if rank is None else rank
        
        # get random character based on rank
        character = get_random_character(cursor, rank)

        # if new, create, else increase count
        p_char = get_p_character(cursor, player_id = player['rowid'], char_id = character['rowid'])
        if not p_char:
            p_char_id = create_p_character(cursor, player['rowid'], character['rowid'])
        else:
            p_char_id = p_char['rowid']
            level_up_p_character(cursor, p_char_id)

        # commit changes
        db.commit()
    except Exception as e:
        p_char = None
        logging.error(e)
    finally:
        # return character
        cursor.close()
        return p_char

def roll_item(player_id, rank=None):
    try:
        cursor = db.cursor()

        # get player info
        player = get_player_info(cursor, player_id)

        # get the rank needed
        rank = get_random_rank() if rank is None else rank

        # get random character based on rank
        item = get_random_item(cursor, rank)
        
        # add item to player inventory
        add_item_to_player(cursor, player['rowid'], item['rowid'])

        # commit changes
        db.commit()
    except Exception as e:
        item = None
        logging.error(e)
    finally:
        # return character
        cursor.close()
        return item

def add_item_to_player(cursor, player_id, item_id):
    cursor.execute(f'INSERT INTO player_items (player_id, item_id) VALUES ({player_id}, {item_id})')

def get_random_item(cursor, rank):
    item = cursor.execute(f'SELECT rowid, * FROM items WHERE rank = {rank} ORDER BY RANDOM() LIMIT 1').fetchone()
    if not item:
        raise ItemNotFoundException(f'No item with rank {rank} found. Check for db initialization.')
    return item

def create_new_player(username=None, password=None):
    cursor = db.cursor()
    if username and password:
        cursor.execute(f'INSERT INTO players (username, password) VALUES ("{username}", "{get_password_hash(password)}")')
    else:
        cursor.execute('INSERT INTO players DEFAULT VALUES')
    new_player_id = cursor.lastrowid
    roll_character(new_player_id)
    roll_item(new_player_id)
    db.commit()
    cursor.close()
    return new_player_id

def get_password_hash(password):
    # converting password to array of bytes
    bytes = password.encode('utf-8')
    # generating the salt
    salt = bcrypt.gensalt()
    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)
    return hash

def check_password(password, hashed_password):
    # converting password to array of bytes
    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, hashed_password)
    return result

def create_p_character(cursor, player_id, char_id):
    cursor.execute(f'INSERT INTO player_characters (player_id, character_id) VALUES ({player_id}, {char_id})')
    
def level_up_p_character(cursor, p_char_id):
    cursor.execute(f'UPDATE player_characters SET level = level + 1 WHERE rowid = {p_char_id}')

def get_random_character(cursor, rank=1):
    char = cursor.execute(f'SELECT rowid, * FROM characters WHERE rank = {rank} ORDER BY RANDOM() LIMIT 1').fetchone()
    if not char:
        raise CharacterNotFoundException(f'No character with rank {rank} found. Check for db initialization.')
    return char

def get_p_character(cursor = None, p_char_id = None, player_id = None, char_id = None):
    cursor = db.cursor() if not cursor else cursor
    if p_char_id:
        p_char = cursor.execute(f'SELECT rowid, * FROM player_characters WHERE id = {p_char_id} LIMIT 1').fetchone()
        if not p_char:
            raise PlayerCharacterNotFoundException(f'No player character with id {p_char_id} found. Please check implementation.')
    else:
        p_char = cursor.execute(f'SELECT rowid, * FROM player_characters WHERE player_id = {player_id} AND character_id = {char_id}').fetchone()
    return p_char

def get_player_info(cursor, player_id):
    player = cursor.execute(f'SELECT rowid, * FROM players WHERE rowid = {player_id} LIMIT 1').fetchone()
    if not player:
        raise PlayerNotFoundException(f'No player with id {player_id} found. Check for db seed')
    return player

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
    crit = rand < 0.1 ? 1.5 : 1
    mul = love_score * level_score
    acting_atk = (attacker_attack + item_score) * mul
    damage = (int) ((acting_atk/acting_def) * 10) * rand
    '''