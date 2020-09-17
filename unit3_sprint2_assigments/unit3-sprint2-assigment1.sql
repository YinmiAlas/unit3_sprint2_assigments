-- How many total Characters are there?
SELECT COUNT("character_id")
FROM charactercreator_character;-- Total 302

-- How many of each specific subclass?
SELECT COUNT("character_ptr_id")
FROM charactercreator_cleric;-- Total 75

SELECT COUNT("character_ptr_id") 
FROM charactercreator_fighter;-- Total 68

SELECT COUNT("mage_ptr_id") 
FROM charactercreator_mage;-- Total 108

SELECT COUNT("character_ptr_id")
FROM charactercreator_necromancer;-- Total 11

SELECT COUNT("character_ptr_id")
FROM charactercreator_thief;-- Total 51

--How many total Items?
SELECT COUNT("item_id")
FROM charactercreator_character_inventory;-- Total Items 898

-- How many of the Items are weapons? How many are not?
SELECT COUNT("item_ptr_id")
FROM armory_weapon;-- 37 weapons and 861 are not weapons

-- How many Items does each character have? (Return first 20 rows) 
SELECT
  COUNT(item_id),
  COUNT(DISTINCT item_id)
FROM charactercreator_character_inventory
LIMIT 20;

-- How many Weapons does each character have?(Return first 20 rows)

SELECT 
  COUNT(item_ptr_id),
  COUNT(DISTINCT item_ptr_id)
FROM armory_weapon
LIMIT 20;

-- On average, how many Items does each Character have?
SELECT 
  COUNT(item_id),
  AVG(item_id)
FROM charactercreator_character_inventory
GROUP BY item_id;

-- On average, how many Weapons does each character have?
SELECT
  COUNT(item_ptr_id),
  AVG(item_ptr_id)
FROM armory_weapon
GROUP BY item_ptr_id;