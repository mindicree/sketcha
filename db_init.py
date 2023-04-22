import sqlite3
import os
import yaml

# initial setup
try:
    os.remove('database.db')
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
except Exception as e:
    print(f'Could not initialize database. Error: {e}')
    exit()

# setup tables
try:
    with open('sql/table_init.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    cursor.executescript(sql_script)
except Exception as e:
    print(f'Could not run table creation script. Error: {e}')
    exit()

# load characters
try:
    char_files = os.listdir('characters')
    char_files.remove('_template.yaml')
    for char_file in char_files:
        with open(f'characters/{char_file}', 'r') as file:
            char = yaml.safe_load(file.read())
            script = f'''
            INSERT INTO characters 
            (name, desc, rank, hp, p_atk, a_atk, m_atk, p_def, a_def, m_def, r_def, speed, sprite_idle_1, sprite_idle_2, sprite_p_atk, sprite_a_atk, sprite_m_atk, sprite_damage, sprite_dodge, sprite_victory_1, sprite_victory_2, sprite_defeat_1, sprite_defeat_2)
            VALUES
            ("{char['NAME']}", "{char['DESC']}", {char['RANK']}, {char['HP']}, {char['P_ATK']}, {char['A_ATK']}, {char['M_ATK']}, {char['P_DEF']}, {char['A_DEF']}, {char['M_DEF']}, {char['R_DEF']}, {char['SPEED']}, "{char['SPRITE_IDLE_1']}", "{char['SPRITE_IDLE_2']}", "{char['SPRITE_P_ATK']}", "{char['SPRITE_A_ATK']}", "{char['SPRITE_M_ATK']}", "{char['SPRITE_DAMAGE']}", "{char['SPRITE_DODGE']}", "{char['SPRITE_VICTORY_1']}", "{char['SPRITE_VICTORY_2']}", "{char['SPRITE_DEFEAT_1']}", "{char['SPRITE_DEFEAT_2']}")
            '''
            cursor.executescript(script)
except Exception as e:
    print(f'Could not load character data into database. Error: {e}')
    exit()

# load items
try:
    item_files = os.listdir('items')
    item_files.remove('_template.yaml')
    for item_file in item_files:
        with open(f'items/{item_file}', 'r') as file:
            item = yaml.safe_load(file.read())
            script = f'''
            INSERT INTO items 
            (name, desc, rank, stat_target, stat_bonus, sprite)
            VALUES
            ("{item['NAME']}", "{item['DESC']}", {item['RANK']}, "{item['STAT_TARGET']}", {item['STAT_BONUS']}, "{item['SPRITE']}")
            '''
            cursor.executescript(script)
except Exception as e:
    print(f'Could not load item data into database. Error: {e}')
    exit()

# conclude
cursor.close()
print('\nDatabase successfully initialized.')

