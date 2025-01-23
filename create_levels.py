import copy
import os

from dungeon_despair.domain.configs import config
from dungeon_despair.functions import DungeonCrawlerFunctions
from dungeon_despair.domain.level import Level

os.makedirs(f'./{config.temp_dir}', exist_ok=True)
os.makedirs('./resources/levels', exist_ok=True)

dcf = DungeonCrawlerFunctions()

empty_level = Level()
empty_level.save_to_file('./resources/levels/empty.bin', '')

# Test case #1
print('Generating levels for T1...')
os.makedirs('./resources/levels/1', exist_ok=True)
t1_level = copy.deepcopy(empty_level)

dcf.create_room(level=t1_level,
                name='Swamp Room',
                description='A room set in a swamp',
                room_from='', direction='')
t1_level.save_to_file('./resources/levels/1/2.bin', '')

dcf.add_enemy(level=t1_level,
              room_name='Swamp Room',
              name='Bog Monster', description='A monster covered in algae',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_enemy(level=t1_level,
              room_name='Swamp Room',
              name='Banshee', description='A screaming banshee',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t1_level.save_to_file('./resources/levels/1/3.bin', '')

dcf.create_room(level=t1_level,
                name='Medieval Room',
                description='A room set in the middle ages',
                room_from='Swamp Room', direction='east')
t1_level.save_to_file('./resources/levels/1/4.bin', '')

dcf.add_enemy(level=t1_level,
              room_name='Medieval Room',
              name='Undead Knight', description='A skeleton wearing an armor',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_treasure(level=t1_level,
                 room_name='Medieval Room',
                 name='Ornate Chest',
                 description='A chest made out of wood',
                 loot='5x gold pieces',
                 cell_index=-1)
t1_level.save_to_file('./resources/levels/1/5.bin', '')

dcf.add_trap(level=t1_level,
             corridor_name='Swamp Room-Medieval Room',
             name='Spike Pit', description='A pit with spikes',
             effect='Causes bleeding',
             cell_index=1)
dcf.add_trap(level=t1_level,
             corridor_name='Swamp Room-Medieval Room',
             name='Sand Pit', description='A pit with sand',
             effect='Causes bleeding',
             cell_index=2)
t1_level.save_to_file('./resources/levels/1/6.bin', '')

dcf.update_enemy_properties(level=t1_level,
                            room_name='Swamp Room',
                            reference_name='Bog Monster',
                            name='Bog Monster', description='A monster covered in algae',
                            species='Unknown', hp=2.5, dodge=0.5, prot=0.5, spd=0.5,
                            cell_index=-1)
t1_level.save_to_file('./resources/levels/1/7.bin', '')

del t1_level

# Test case 2
print('Generating levels for T2...')
os.makedirs('./resources/levels/2', exist_ok=True)
t2_level = copy.deepcopy(empty_level)

dcf.create_room(level=t2_level,
                name='Starting Room',
                description='A starting room with a torch-lit atmosphere',
                room_from='', direction='')
t2_level.save_to_file('./resources/levels/2/2.bin', '')

dcf.add_enemy(level=t2_level,
              room_name='Starting Room',
              name='Menacing Shadow', description='A menacing shadow',
              species='Unknown', hp=50.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t2_level.save_to_file('./resources/levels/2/3.bin', '')

dcf.create_room(level=t2_level,
                name='Ancient Room',
                description='A room filled with ancient runes on the floor',
                room_from='Starting Room', direction='east')
t2_level.save_to_file('./resources/levels/2/4.bin', '')


dcf.add_treasure(level=t2_level,
                 room_name='Starting Room-Ancient Room',
                 name='Ornate Chest',
                 description='A chest made out of wood',
                 loot='5x gold pieces',
                 cell_index=2)
t2_level.save_to_file('./resources/levels/2/5.bin', '')
                      
dcf.add_trap(level=t2_level,
             corridor_name='Starting Room-Ancient Room',
             name='Spike Pit', description='A pit with spikes',
             effect='Causes bleeding',
             cell_index=1)
t2_level.save_to_file('./resources/levels/2/6.bin', '')

dcf.create_room(level=t2_level,
                name='Small Room',
                description='A small chamber with a mystical pool',
                room_from='Ancient Room', direction='south')
t2_level.save_to_file('./resources/levels/2/7.bin', '')

dcf.add_enemy(level=t2_level,
              room_name='Small Room',
              name='Humanoid Cat', description='A humanoid cat',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_treasure(level=t2_level,
                 room_name='Small Room',
                 name='Simple Chest',
                 description='A chest made out of wood',
                 loot='10x wool balls',
                 cell_index=-1)
t2_level.save_to_file('./resources/levels/2/8.bin', '')

dcf.create_room(level=t2_level,
                name='Cavern Room',
                description='A larger cavernous room filled with glowing mushrooms',
                room_from='Small Room', direction='east')
t2_level.save_to_file('./resources/levels/2/9.bin', '')

del t2_level

# Test case 3
print('Generating levels for T3...')
os.makedirs('./resources/levels/3', exist_ok=True)
t3_level = copy.deepcopy(empty_level)

dcf.create_room(level=t3_level,
                name='Starting Room',
                description='A starting room with dim lighting and a stone entrance',
                room_from='', direction='')
t3_level.save_to_file('./resources/levels/3/2.bin', '')

dcf.create_room(level=t3_level,
                name='Bridge Room',
                description='A room with a collapsed bridge spanning a dark chasm',
                room_from='Starting Room', direction='east')
t3_level.save_to_file('./resources/levels/3/3.bin', '')

dcf.add_treasure(level=t3_level,
                 room_name='Bridge Room',
                 name='Simple Chest',
                 description='A chest made out of wood',
                 loot='10x gold pieces',
                 cell_index=-1)
t3_level.save_to_file('./resources/levels/3/4.bin', '')

dcf.add_enemy(level=t3_level,
              room_name='Bridge Room',
              name='Ghost', description='A ghostly apparition',
              species='Unknown', hp=60.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t3_level.save_to_file('./resources/levels/3/5.bin', '')

dcf.create_room(level=t3_level,
                name='Underground Room',
                description='An underground chamber with phosphorescent crystals',
                room_from='Starting Room', direction='north')
t3_level.save_to_file('./resources/levels/3/6.bin', '')

dcf.add_enemy(level=t3_level,
              room_name='Underground Room',
              name='Bat 1', description='A bat',
              species='Unknown', hp=20.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_enemy(level=t3_level,
              room_name='Underground Room',
              name='Bat 2', description='A bat',
              species='Unknown', hp=20.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t3_level.save_to_file('./resources/levels/3/7.bin', '')

dcf.create_room(level=t3_level,
                name='Mirror Room',
                description='A room with a magical mirror that reflects the future actions of anyone who gazes into it',
                room_from='Underground Room', direction='north')
t3_level.save_to_file('./resources/levels/3/8.bin', '')

dcf.add_enemy(level=t3_level,
              room_name='Mirror Room',
              name='Spectral Guardian', description='A spectral guardian',
              species='Unknown', hp=70.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t3_level.save_to_file('./resources/levels/3/9.bin', '')

dcf.create_room(level=t3_level,
                name='Arena Room',
                description='A circular arena with a locked gate',
                room_from='Mirror Room', direction='east')
t3_level.save_to_file('./resources/levels/3/10.bin', '')

del t3_level

# Test case 4
print('Generating levels for T4...')
os.makedirs('./resources/levels/4', exist_ok=True)
t4_level = copy.deepcopy(empty_level)

dcf.create_room(level=t4_level,
                name='Gravity Room',
                description='A room with a gravity-defying effect where everything floats',
                room_from='', direction='')
t4_level.save_to_file('./resources/levels/4/2.bin', '')

dcf.add_treasure(level=t4_level,
                 room_name='Gravity Room',
                 name='Simple Chest',
                 description='A chest made out of wood',
                 loot='10x gold pieces',
                 cell_index=-1)
t4_level.save_to_file('./resources/levels/4/3.bin', '')

dcf.create_room(level=t4_level,
                name='Omega Room',
                description='A room where nothing exists, yet everything does',
                room_from='Gravity Room', direction='east')
t4_level.save_to_file('./resources/levels/4/4.bin', '')

dcf.add_enemy(level=t4_level,
              room_name='Omega Room',
              name='Treasure Chest', description='A treasure chest that is also an enemy',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t4_level.save_to_file('./resources/levels/4/5.bin', '')

t4_level.save_to_file('./resources/levels/4/6.bin', '')

dcf.add_enemy(level=t4_level,
              room_name='Omega Room',
              name='Enemy 1', description='An enemy',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_enemy(level=t4_level,
              room_name='Omega Room',
              name='Enemy 2', description='An enemy',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_enemy(level=t4_level,
              room_name='Omega Room',
              name='Enemy 3', description='An enemy',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t4_level.save_to_file('./resources/levels/4/7.bin', '')

dcf.create_room(level=t4_level,
                name='Room 1',
                description='A room',
                room_from='Omega Room', direction='north')
t4_level.save_to_file('./resources/levels/4/8.bin', '')

dcf.create_room(level=t4_level,
                name='Room 2',
                description='A room',
                room_from='Room 1', direction='north')
t4_level.save_to_file('./resources/levels/4/9.bin', '')

dcf.create_room(level=t4_level,
                name='Room 3',
                description='A room',
                room_from='Room 2', direction='north')
t4_level.save_to_file('./resources/levels/4/10.bin', '')

dcf.create_room(level=t4_level,
                name='Room 4',
                description='A room',
                room_from='Room 3', direction='north')
t4_level.save_to_file('./resources/levels/4/11.bin', '')

del t4_level

# Test case 5
print('Generating levels for T5...')
os.makedirs('./resources/levels/5', exist_ok=True)
t5_level = copy.deepcopy(empty_level)

dcf.create_room(level=t5_level,
                name='Paris Room',
                description='A room set in Paris',
                room_from='', direction='')
dcf.create_room(level=t5_level,
                name='Rome Room',
                description='A room set in Rome',
                room_from='Paris Room', direction='east')
dcf.create_room(level=t5_level,
                name='Amsterdam Room',
                description='A room set in Amsterdam',
                room_from='Rome Room', direction='east')
t5_level.save_to_file('./resources/levels/5/2.bin', '')

dcf.add_enemy(level=t5_level,
              room_name='Paris Room',
              name='Goblin Archer', description='A goblin archer',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t5_level.save_to_file('./resources/levels/5/3.bin', '')

dcf.add_enemy(level=t5_level,
              room_name='Paris Room',
              name='Zombie 1', description='A zombie',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_enemy(level=t5_level,
              room_name='Paris Room',
              name='Zombie 2', description='A zombie',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t5_level.save_to_file('./resources/levels/5/4.bin', '')

dcf.create_room(level=t5_level,
                name='Atlantis Room',
                description='A room set in underground Atlantis',
                room_from='Paris Room', direction='north')
t5_level.save_to_file('./resources/levels/5/5.bin', '')

dcf.add_enemy(level=t5_level,
              room_name='Atlantis Room',
              name='Evil Mermaid 1', description='An evil mermaid',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_enemy(level=t5_level,
              room_name='Atlantis Room',
              name='Evil Mermaid 2', description='An evil mermaid',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t5_level.save_to_file('./resources/levels/5/6.bin', '')

dcf.add_trap(level=t5_level,
             corridor_name='Paris Room-Atlantis Room',
             name='Whirlpool', description='A whirlpool',
             effect='Causes bleeding',
             cell_index=1)
dcf.add_trap(level=t5_level,
             corridor_name='Paris Room-Atlantis Room',
             name='Shark Pit', description='A pit with sharks',
             effect='Causes bleeding',
             cell_index=2)
t5_level.save_to_file('./resources/levels/5/7.bin', '')

dcf.add_treasure(level=t5_level,
                 room_name='Paris Room',
                 name='Simple Chest',
                 description='A chest containing a piece of a treasure map',
                 loot='Treasure Map piece 1',
                 cell_index=-1)
dcf.add_treasure(level=t5_level,
                 room_name='Rome Room',
                 name='Simple Chest',
                 description='A chest containing a piece of a treasure map',
                 loot='Treasure Map piece 2',
                 cell_index=-1)
dcf.add_treasure(level=t5_level,
                 room_name='Amsterdam Room',
                 name='Simple Chest',
                 description='A chest containing a piece of a treasure map',
                 loot='Treasure Map piece 3',
                 cell_index=-1)
dcf.add_treasure(level=t5_level,
                 room_name='Atlantis Room',
                 name='Simple Chest',
                 description='A chest containing a piece of a treasure map',
                 loot='Treasure Map piece 4',
                 cell_index=-1)
t5_level.save_to_file('./resources/levels/5/8.bin', '')

dcf.remove_entity(level=t5_level,
                  room_name='Rome Room',
                  entity_name='Simple Chest',
                  entity_type='treasure',
                  cell_index=-1)
t5_level.save_to_file('./resources/levels/5/9.bin', '')

dcf.create_room(level=t5_level,
                name='Hell Room',
                description='A room set in Hell',
                room_from='Atlantis Room', direction='west')
t5_level.save_to_file('./resources/levels/5/10.bin', '')

dcf.add_enemy(level=t5_level,
              room_name='Hell Room',
              name='Fallen Angel 1', description='A fallen angel',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
dcf.add_enemy(level=t5_level,
              room_name='Hell Room',
              name='Fallen Angel 2', description='A fallen angel',
              species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
              cell_index=-1)
t5_level.save_to_file('./resources/levels/5/11.bin', '')

dcf.update_enemy_properties(level=t5_level,
                            room_name='Hell Room',
                            reference_name='Fallen Angel 1',
                            name='Capybara Monster',
                            description='A monster capybara',
                            species='Unknown', hp=5.0, dodge=0.5, prot=0.5, spd=0.5,
                            cell_index=-1)
t5_level.save_to_file('./resources/levels/5/12.bin', '')

dcf.update_enemy_properties(level=t5_level,
                            room_name='Hell Room',
                            reference_name='Capybara Monster',
                            name='Capybara Monster',
                            description='A monster capybara',
                            species='Unknown', hp=1000.0, dodge=0.5, prot=0.5, spd=0.5,
                            cell_index=-1)
t5_level.save_to_file('./resources/levels/5/13.bin', '')

print('All levels created and saved')
