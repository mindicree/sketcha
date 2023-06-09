CREATE TABLE IF NOT EXISTS players (
    coins INT DEFAULT 5,
    streak INT DEFAULT 0,
    username TEXT DEFAULT NULL,
    password TEXT DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS characters (
    name TEXT,
    desc TEXT,
    rank INT,
    hp INT,
    p_atk INT,
    a_atk INT,
    m_atk INT,
    p_def INT,
    a_def INT,
    m_def INT,
    r_def INT,
    speed INT,
    sprite_idle_1 TEXT,
    sprite_idle_2 TEXT,
    sprite_p_atk TEXT,
    sprite_a_atk TEXT,
    sprite_m_atk TEXT,
    sprite_damage TEXT,
    sprite_dodge TEXT,
    sprite_victory_1 TEXT,
    sprite_victory_2 TEXT,
    sprite_defeat_1 TEXT,
    sprite_defeat_2 TEXT
);

CREATE TABLE IF NOT EXISTS items (
    name TEXT,
    desc TEXT,
    rank INT,
    stat_target TEXT,
    stat_bonus INT,
    sprite TEXT
);

CREATE TABLE IF NOT EXISTS enemies (
    name TEXT,
    desc TEXT,
    hp INT,
    atk INT,
    atk_type TEXT,
    p_def INT,
    a_def INT,
    m_def INT,
    r_def INT,
    speed INT,
    sprite_idle_1 TEXT,
    sprite_idle_2 TEXT,
    sprite_atk,
    sprite_damage,
    sprite_dodge,
    sprite_victory_1 TEXT,
    sprite_victory_2 TEXT,
    sprite_defeat_1 TEXT,
    sprite_defeat_2 TEXT
);

CREATE TABLE IF NOT EXISTS player_characters (
    player_id INT,
    character_id INT,
    level INT DEFAULT 1,
    love INT DEFAULT 0,
    FOREIGN KEY (player_id) REFERENCES players(rowid),
    FOREIGN KEY (character_id) REFERENCES characters(rowid)
);

CREATE TABLE IF NOT EXISTS player_items (
    player_id INT,
    item_id INT,
    equipped_by INT DEFAULT NULL,
    FOREIGN KEY (player_id) REFERENCES players(rowid),
    FOREIGN KEY (item_id) REFERENCES items(rowid)
    FOREIGN KEY (equipped_by) REFERENCES player_characters(rowid)
);