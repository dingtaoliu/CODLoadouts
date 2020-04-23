DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS loadout;
DROP TABLE IF EXISTS weapon;
DROP TABLE IF EXISTS perk;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS attachment;
DROP TABLE IF EXISTS weapon_loadout;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE loadout (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  loadout_name TEXT NOT NULL,
  primary_weapon_id INTEGER NOT NULL,
  secondary_weapon_id INTEGER NOT NULL,
  perk_1_id INTEGER NOT NULL,
  perk_2_id INTEGER NOT NULL,
  perk_3_id INTEGER NOT NULL,
  primary_equipment_id INTEGER NOT NULL,
  secondary_equipment_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (primary_weapon_id) REFERENCES weapon (id),
  FOREIGN KEY (secondary_weapon_id) REFERENCES weapon (id),
  FOREIGN KEY (perk_1_id) REFERENCES perk (id),
  FOREIGN KEY (perk_2_id) REFERENCES perk (id),
  FOREIGN KEY (perk_3_id) REFERENCES perk (id),
  FOREIGN KEY (primary_equipment_id) REFERENCES equipment (id),
  FOREIGN KEY (secondary_equipment_id) REFERENCES equipment (id)
);

CREATE TABLE weapon (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  weapon_name TEXT NOT NULL 
);

CREATE TABLE perk (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  perk_name TEXT NOT NULL 
);

CREATE TABLE equipment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  equipment_name TEXT NOT NULL 
);

CREATE TABLE attachment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  attachment_type TEXT NOT NULL,
  attachment_name TEXT NOT NULL 
);

CREATE TABLE weapon_loadout (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  weapon_id INTEGER NOT NULL,
  attachment_1_id INTEGER DEFAULT NULL,
  attachment_2_id INTEGER DEFAULT NULL,
  attachment_3_id INTEGER DEFAULT NULL,
  attachment_4_id INTEGER DEFAULT NULL,
  attachment_5_id INTEGER DEFAULT NULL,
  attachment_6_id INTEGER DEFAULT NULL,
  attachment_7_id INTEGER DEFAULT NULL,
  attachment_8_id INTEGER DEFAULT NULL,
  attachment_9_id INTEGER DEFAULT NULL,
  FOREIGN KEY (weapon_id) REFERENCES weapon (id),
  FOREIGN KEY (attachment_1_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_2_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_3_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_4_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_5_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_6_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_7_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_8_id) REFERENCES attachment (id),
  FOREIGN KEY (attachment_9_id) REFERENCES attachment (id)
);