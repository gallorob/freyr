from typing import List, Any

from dungeon_despair.domain.configs import config
from dungeon_despair.domain.encounter import Encounter
from dungeon_despair.domain.entities.enemy import Enemy
from dungeon_despair.domain.entities.trap import Trap
from dungeon_despair.domain.entities.treasure import Treasure
from dungeon_despair.domain.level import Level
from dungeon_despair.domain.utils import get_encounter


def all_elements_same_by_value(l: List[Any],
                               v: Any) -> bool:
	return all(x == v for x in l)


def get_enemies_in_encounter(enc: Encounter) -> List[Enemy]:
	return enc.entities['enemy']

def get_traps_in_encounter(enc: Encounter) -> List[Trap]:
	return enc.entities['trap']

def get_treasures_in_encounter(enc: Encounter) -> List[Treasure]:
	return enc.entities['treasure']

def is_room(name: str,
            level: Level) -> bool:
	return name in level.rooms.keys()

def is_corridor(name: str,
                level: Level) -> bool:
	return name in level.corridors.keys()


def validate_intents(use_case: int, step: int, intents: List[str]) -> bool:
	if use_case == 1:
		if step == 0:  # Make a room in a swamp
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 1:  # Add a couple of enemies
			return len(intents) > 1 and all_elements_same_by_value(intents, 'add_enemy')
		elif step == 2:  # Add a new room set in the middle ages
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 3:  # Add an enemy and a treasure
			return len(intents) == 2 and 'add_enemy' in intents and 'add_treasure' in intents
		elif step == 4:  # Add multiple traps in the corridor
			return len(intents) > 1 and all_elements_same_by_value(intents, 'add_trap')
		elif step == 5:  # Change the first enemy in the swamp to half its health and give it a sword
			return len(intents) == 1 and intents[0] == 'update_enemy_properties'
		elif step == 6:  # Add a trap in the first room
			return len(intents) == 1 and intents[0] == 'add_trap'
		else:
			raise ValueError('Invalid step')
	if use_case == 2:
		if step == 0:  # Create a starting room with a torch-lit atmosphere
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 1:  # Introduce an enemy in the starting room, described as a menacing shadow with 50 health points
			return len(intents) == 1 and intents[0] == 'add_enemy'
		elif step == 2:  # Make a new room filled with ancient runes on the floor
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 3:  # Place a treasure chest at the end of the corridor
			return len(intents) == 1 and intents[0] == 'add_treasure'
		elif step == 4:  # Add a hidden trap in the corridor
			return len(intents) == 1 and intents[0] == 'add_trap'
		elif step == 5:  # Insert a small chamber with a mystical pool
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 6:  # Add a humanoid cat guarding a chest filled with wool
			return len(intents) == 2 and 'add_enemy' in intents and 'add_treasure' in intents
		elif step == 7:  # Connect the mystical pool chamber to a larger cavernous room filled with glowing mushrooms
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 8:  # Add a giant spider with 80 health points in the cavernous room
			return len(intents) == 1 and intents[0] == 'add_enemy'
		else:
			raise ValueError('Invalid step')
	if use_case == 3:
		if step == 0:  # Create a starting room with dim lighting and a stone entrance
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 1:  # Create a room with a collapsed bridge spanning a dark chasm
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 2:  # Place a treasure chest
			return len(intents) == 1 and intents[0] == 'add_treasure'
		elif step == 3:  # Introduce an enemy in the collapsed bridge room: a ghostly apparition with 60 health points
			return len(intents) == 1 and intents[0] == 'add_enemy'
		elif step == 4:  #Add an underground chamber with phosphorescent crystals connected to the starting room
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 5:  # Place a swarm of bats in the underground chamber with 40 health points collectively
			return len(intents) == 1 and intents[0] == 'add_enemy'
		elif step == 6:  # Create a room with a magical mirror that reflects the future actions of anyone who gazes into it
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 7:  # Introduce an enemy in the magical mirror room: a spectral guardian with 70 health points
			return len(intents) == 1 and intents[0] == 'add_enemy'
		elif step == 8:  # Connect the magical mirror room to a circular arena with a locked gate
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 9:  # Add a ferocious minotaur with 100 health points in the circular arena
			return len(intents) == 1 and intents[0] == 'add_enemy'
		else:
			raise ValueError('Invalid step')
	elif use_case == 4:
		if step == 0:  # Create a room with a gravity-defying effect where everything floats
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 1:  # Place a treasure chest in the starting room
			return len(intents) == 1 and intents[0] == 'add_treasure'
		elif step == 2:  # Create a room where nothing exists, yet everything does
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 3:  # Add a treasure chest that is also an enemy
			return len(intents) == 1 and intents[0] == 'add_enemy' or intents[0] == 'add_treasure'
		elif step == 4:  # Place a trap in the room
			return len(intents) == 1 and intents[0] == 'add_trap'
		elif step == 5:  # Place five unique enemies
			return len(intents) == 5 and all_elements_same_by_value(intents, 'add_enemy')
		elif step == 6:  # Add a room next to the current one
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 7:  # Add a room next to the current one
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 8:  # Add a room next to the current one
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 9:  # Add a room next to the current one
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 10:  # Add a room next to the current one
			return len(intents) == 1 and intents[0] == 'create_room'
		else:
			raise ValueError('Invalid step')
	elif use_case == 5:
		if step == 0:  # Create 3 rooms, each connected to the next one, all set in a different European city
			return len(intents) == 5 and all_elements_same_by_value(intents, 'create_room')
		elif step == 1:  # Add a goblin archer in the first room
			return len(intents) == 1 and intents[0] == 'add_enemy'
		elif step == 2:  # Also add two zombies
			return len(intents) == 2 and all_elements_same_by_value(intents, 'add_enemy')
		elif step == 3:  # Now generate a room connected to the first one, set in underground Atlantis
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 4:  # Put a couple of evil mermaids in Atlantis
			return len(intents) > 1 and all_elements_same_by_value(intents, 'add_enemy')
		elif step == 5:  # Place multiple ocean-themed traps in the corridor to Atlantis
			return len(intents) > 1 and all_elements_same_by_value(intents, 'add_trap')
		elif step == 6:  # Place a single treasure chest in all rooms, each containing a piece of a treasure map
			return len(intents) > 1 and all_elements_same_by_value(intents, 'add_treasure')
		elif step == 7:  # Remove the chest containing the second piece of the treasure map
			return len(intents) == 1 and intents[0] == 'remove_entity'
		elif step == 8:  # Add another room connected to Atlantis, set in Hell
			return len(intents) == 1 and intents[0] == 'create_room'
		elif step == 9:  # Place two fallen angels armed with flaming swords
			return len(intents) > 1 and all_elements_same_by_value(intents, 'add_enemy')
		elif step == 10:  # Change one of the angels to a capybara monster
			return len(intents) == 1 and intents[0] == 'update_enemy_properties'
		elif step == 11:  # Set the health of the capybara to 1000
			return len(intents) == 1 and intents[0] == 'update_enemy_properties'
		elif step == 12:  # Make the capybara a punker, with pink spiky hair
			return len(intents) == 1 and intents[0] == 'update_enemy_properties'
		else:
			raise ValueError('Invalid step')
	else:
		raise ValueError("Invalid use case")

def validate_level_domain(use_case: int, step: int, old_level: Level, new_level: Level) -> bool:
	if use_case == 1:
		if step == 0:  # Make a room in a swamp
			return len(new_level.rooms) == 1 and new_level.current_room != old_level.current_room
		elif step == 1:  # Add a couple of enemies
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) > 1
		elif step == 2:  # Add a new room set in the middle ages
			return len(new_level.rooms) == 2 and len(new_level.corridors) == 1 and new_level.current_room != old_level.current_room
		elif step == 3:  # Add an enemy and a treasure
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies, new_treasures = get_enemies_in_encounter(new_enc), get_treasures_in_encounter(new_enc)
			old_enemies, old_treasures = get_enemies_in_encounter(old_enc), get_treasures_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) > 0 and len(new_treasures) - len(old_treasures) > 0
		elif step == 4:  # Add multiple traps in the corridor
			if new_level.current_room not in new_level.corridors: return False
			new_corridor = new_level.corridors[new_level.current_room]
			old_corridor = old_level.corridors[new_level.current_room]
			new_traps, old_traps = 0, 0
			for enc in new_corridor.encounters:
				new_traps += len(get_traps_in_encounter(enc))
			for enc in old_corridor.encounters:
				old_traps += len(get_traps_in_encounter(enc))
			return new_traps - old_traps > 0
		elif step == 5:  # Change the first enemy in the swamp to half its health and give it a sword
			return True
		elif step == 6:  # Add a trap in the first room
			# should not work, so level remains unchanged
			return new_level.model_dump_json() == old_level.model_dump_json()
		else:
			raise ValueError("Invalid step")
	elif use_case == 2:
		if step == 0:  # Create a starting room with a torch-lit atmosphere
			return len(new_level.rooms) == 1 and new_level.current_room != old_level.current_room
		elif step == 1:  # Introduce an enemy in the starting room, described as a menacing shadow with 50 health points
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 1
		elif step == 2:  # Make a new room filled with ancient runes on the floor
			return len(new_level.rooms) == 2 and len(new_level.corridors) == 1 and new_level.current_room != old_level.current_room
		elif step == 3:  # Place a treasure chest at the end of the corridor
			if new_level.current_room not in new_level.corridors: return False
			new_corridor = new_level.corridors[new_level.current_room]
			old_corridor = old_level.corridors[new_level.current_room]
			new_treasures = get_treasures_in_encounter(new_corridor.encounters[new_corridor.length - 1])
			old_treasures = get_treasures_in_encounter(old_corridor.encounters[new_corridor.length - 1])
			return len(new_treasures) - len(old_treasures) == 1
		elif step == 4:  # Add a hidden trap in the corridor
			if new_level.current_room not in new_level.corridors: return False
			new_corridor = new_level.corridors[new_level.current_room]
			old_corridor = old_level.corridors[new_level.current_room]
			new_traps, old_traps = 0, 0
			for enc in new_corridor.encounters:
				new_traps += len(get_traps_in_encounter(enc))
			for enc in old_corridor.encounters:
				old_traps += len(get_traps_in_encounter(enc))
			return new_traps - old_traps == 1
		elif step == 5:  # Insert a small chamber with a mystical pool
			return len(new_level.rooms) == 3 and len(new_level.corridors) == 2
		elif step == 6:  # Add a humanoid cat guarding a chest filled with wool
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			new_treasures = get_treasures_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			old_treasures = get_treasures_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 1 and len(new_treasures) - len(old_treasures) == 1
		elif step == 7:  # Connect the mystical pool chamber to a larger cavernous room filled with glowing mushrooms
			return len(new_level.rooms) == 4 and len(new_level.corridors) == 3
		elif step == 8:  # Add a giant spider with 80 health points in the cavernous room
			if new_level.current_room not in new_level.rooms: return False
			enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			return len(get_enemies_in_encounter(enc)) == 1
		else:
			raise ValueError("Invalid step")
	elif use_case == 3:
		if step == 0:  # Create a starting room with dim lighting and a stone entrance
			return len(new_level.rooms) == 1 and new_level.current_room != old_level.current_room
		if step == 1:  # Create a room with a collapsed bridge spanning a dark chasm
			return len(new_level.rooms) == 2 and len(new_level.corridors) == 1 and new_level.current_room != old_level.current_room
		if step == 2:  # Place a treasure chest
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_treasures = get_treasures_in_encounter(new_enc)
			old_treasures = get_treasures_in_encounter(old_enc)
			return len(new_treasures) - len(old_treasures) == 1
		if step == 3:  # Introduce an enemy in the collapsed bridge room: a ghostly apparition with 60 health points
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 1
		elif step == 4:  # Add an underground chamber with phosphorescent crystals connected to the starting room
			return len(new_level.rooms) == 3 and len(new_level.corridors) == 2  and new_level.current_room != old_level.current_room
		elif step == 5:  # Place a swarm of bats in the underground chamber with 40 health points collectively
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) > 0
		elif step == 6:  # Create a room with a magical mirror that reflects the future actions of anyone who gazes into it
			return len(new_level.rooms) == 4 and len(new_level.corridors) == 3 and new_level.current_room != old_level.current_room
		elif step == 7:  # Introduce an enemy in the magical mirror room: a spectral guardian with 70 health points
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 1
		elif step == 8:  # Connect the magical mirror room to a circular arena with a locked gate
			return len(new_level.rooms) == 5 and len(new_level.corridors) == 4 and new_level.current_room != old_level.current_room
		elif step == 9:  # Add a ferocious minotaur with 100 health points in the circular arena
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 1
		else:
			raise ValueError('Invalid step')
	elif use_case == 4:
		if step == 0:  # Create a room with a gravity-defying effect where everything floats
			return len(new_level.rooms) == 1 and new_level.current_room != old_level.current_room
		elif step == 1:  # Place a treasure chest in the starting room
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_treasures = get_treasures_in_encounter(new_enc)
			old_treasures = get_treasures_in_encounter(old_enc)
			return len(new_treasures) - len(old_treasures) == 1
		elif step == 2:  # Create a room where nothing exists, yet everything does
			return len(new_level.rooms) == 2 and len(new_level.corridors) == 1 and new_level.current_room != old_level.current_room
		elif step == 3:  # Add a treasure chest that is also an enemy
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			new_treasures = get_treasures_in_encounter(new_enc)
			old_treasures = get_treasures_in_encounter(old_enc)
			return len(new_treasures) - len(old_treasures) == 1 or len(new_enemies) - len(old_enemies) == 1
		elif step == 4:  # Place a trap in the room
			# should not work, so level remains unchanged
			return old_level.model_dump_json() == new_level.model_dump_json()
		elif step == 5:  # Place five unique enemies
			# should not work, so only add up to 4 enemies
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == min(5, config.max_enemies_per_encounter)
		elif step == 6:  # Add a room next to the current one
			return len(new_level.rooms) == 3 and len(new_level.corridors) == 2 and new_level.current_room != old_level.current_room
		elif step == 7:  # Add a room next to the current one
			return len(new_level.rooms) == 4 and len(new_level.corridors) == 3 and new_level.current_room != old_level.current_room
		elif step == 8:  # Add a room next to the current one
			return len(new_level.rooms) == 5 and len(new_level.corridors) == 4 and new_level.current_room != old_level.current_room
		elif step == 9:  # Add a room next to the current one
			return len(new_level.rooms) == 6 and len(new_level.corridors) == 5 and new_level.current_room != old_level.current_room
		elif step == 10:  # Add a room next to the current one
			return len(new_level.rooms) == 7 and len(new_level.corridors) == 6 and new_level.current_room != old_level.current_room
		else:
			raise ValueError('Invalid step')
	elif use_case == 5:
		if step == 0:  # Create 3 rooms, each connected to the next one, all set in a different European city
			return len(new_level.rooms) == 3 and len(new_level.corridors) == 2 and new_level.current_room != old_level.current_room
		elif step == 1:  # Add a goblin archer in the first room
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 1
		elif step == 2:  # Also add two zombies
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 2
		elif step == 3:  # Now generate a room connected to the first one, set in underground Atlantis
			return len(new_level.rooms) == 4 and len(new_level.corridors) == 3 and new_level.current_room != old_level.current_room
		elif step == 4:  # Put a couple of evil mermaids in Atlantis
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) > 1
		elif step == 5:  # Place multiple ocean-themed traps in the corridor to Atlantis
			if new_level.current_room not in new_level.corridors: return False
			new_corridor = new_level.corridors[new_level.current_room]
			old_corridor = old_level.corridors[new_level.current_room]
			new_traps, old_traps = 0, 0
			for enc in new_corridor.encounters:
				new_traps += len(get_traps_in_encounter(enc))
			for enc in old_corridor.encounters:
				old_traps += len(get_traps_in_encounter(enc))
			return new_traps - old_traps > 1
		elif step == 6:  # Place a single treasure chest in all rooms, each containing a piece of a treasure map
			has_treasure = True
			for room_name in new_level.rooms.keys():
				old_treasures = get_treasures_in_encounter(old_level.rooms[room_name].encounter)
				new_treasures = get_treasures_in_encounter(new_level.rooms[room_name].encounter)
				has_treasure &= len(new_treasures) - len(old_treasures) == 1
			return has_treasure
		elif step == 7:  # Remove the chest containing the second piece of the treasure map
			one_less_treasure = True
			for room_name in new_level.rooms.keys():
				old_treasures = get_treasures_in_encounter(old_level.rooms[room_name].encounter)
				new_treasures = get_treasures_in_encounter(new_level.rooms[room_name].encounter)
				one_less_treasure &= len(new_treasures) - len(old_treasures) == 0
			return one_less_treasure
		elif step == 8:  # Add another room connected to Atlantis, set in Hell
			return len(new_level.rooms) == 5 and len(new_level.corridors) == 4 and new_level.current_room != old_level.current_room
		elif step == 9:  # Place two fallen angels armed with flaming swords
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			return len(new_enemies) - len(old_enemies) == 2
		elif step == 10:  # Change one of the angels to a capybara monster
			return True
		elif step == 11:  # Set the health of the capybara to 1000
			return True
		elif step == 12:  # Make the capybara a punker, with pink spiky hair
			return True
		else:
			raise ValueError('Invalid step')
	else:
		raise ValueError("Invalid use case")


def validate_level_design(use_case: int, step: int, old_level: Level, new_level: Level) -> bool:
	if use_case == 1:
		if step == 0:  # Make a room in a swamp
			return True
		elif step == 1:  # Add a couple of enemies
			return True
		elif step == 2:  # Add a new room set in the middle ages
			return True
		elif step == 3:  # Add an enemy and a treasure
			return True
		elif step == 4:  # Add traps in the corridor
			return True
		elif step == 5:  # Change the first enemy in the swamp to half its health and give it a sword
			room_before = list(old_level.rooms.values())[0]
			room_after = list(new_level.rooms.values())[0]
			return room_before.encounter.entities['enemy'][0].hp == 2 * room_after.encounter.entities['enemy'][0].hp
		elif step == 6:  # Add a trap in the first room
			# should not work, so level remains unchanged
			return True
		else:
			raise ValueError("Invalid step")
	elif use_case == 2:
		if step == 0:  # Create a starting room with a torch-lit atmosphere
			return True
		elif step == 1:  # Introduce an enemy in the starting room, described as a menacing shadow with 50 health points
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			new_enemy = [enemy for enemy in new_enemies if enemy.name not in [x.name for x in old_enemies]][0]
			return new_enemy.hp == 50.0
		elif step == 2:  # Make a new room filled with ancient runes on the floor
			return True
		elif step == 3:  # Place a treasure chest at the end of the corridor
			return True
		elif step == 4:  # Add a hidden trap in the corridor
			return True
		elif step == 5:  # Insert a small chamber with a mystical pool
			return True
		elif step == 6:  # Add a humanoid cat guarding a chest filled with wool
			return True
		elif step == 7:  # Connect the mystical pool chamber to a larger cavernous room filled with glowing mushrooms
			return True
		elif step == 8:  # Add a giant spider with 80 health points in the cavernous room
			enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			enemies = get_enemies_in_encounter(enc)
			return enemies[0].hp == 80.0
		else:
			raise ValueError("Invalid step")
	elif use_case == 3:
		if step == 0:  # Create a starting room with dim lighting and a stone entrance
			return True
		if step == 1:  # Create a room with a collapsed bridge spanning a dark chasm
			return True
		if step == 2:  # Place a treasure chest
			return True
		if step == 3:  # Introduce an enemy in the collapsed bridge room: a ghostly apparition with 60 health points
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			new_enemy = [enemy for enemy in new_enemies if enemy.name not in [x.name for x in old_enemies]][0]
			return new_enemy.hp == 60.0
		elif step == 4:  # Add an underground chamber with phosphorescent crystals connected to the starting room
			return True
		elif step == 5:  # Place a swarm of bats in the underground chamber with 40 health points collectively
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			diff_enemies = [enemy for enemy in new_enemies if enemy.name not in [x.name for x in old_enemies]]
			sum_hp = sum([x.hp for x in diff_enemies])
			return sum_hp == 40.0
		elif step == 6:  # Create a room with a magical mirror that reflects the future actions of anyone who gazes into it
			return True
		elif step == 7:  # Introduce an enemy in the magical mirror room: a spectral guardian with 70 health points
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			new_enemy = [enemy for enemy in new_enemies if enemy.name not in [x.name for x in old_enemies]][0]
			return new_enemy.hp == 70.0
		elif step == 8:  # Connect the magical mirror room to a circular arena with a locked gate
			return True
		elif step == 9:  # Add a ferocious minotaur with 100 health points in the circular arena
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			new_enemy = [enemy for enemy in new_enemies if enemy.name not in [x.name for x in old_enemies]][0]
			return new_enemy.hp == 100.0
		else:
			raise ValueError('Invalid step')
	elif use_case == 4:
		if step == 0:  # Create a room with a gravity-defying effect where everything floats
			return True
		elif step == 1:  # Place a treasure chest in the starting room
			return False
		elif step == 2:  # Create a room where nothing exists, yet everything does
			return True
		elif step == 3:  # Add a treasure chest that is also an enemy
			return True
		elif step == 4:  # Place a trap in the room
			return True
		elif step == 5:  # Place five unique enemies
			return True
		elif step == 6:  # Add a room next to the current one
			return True
		elif step == 7:  # Add a room next to the current one
			return True
		elif step == 8:  # Add a room next to the current one
			return True
		elif step == 9:  # Add a room next to the current one
			return True
		elif step == 10:  # Add a room next to the current one
			return True
		else:
			raise ValueError('Invalid step')
	elif use_case == 5:
		if step == 0:  # Create 3 rooms, each connected to the next one, all set in a different European city
			return True
		elif step == 1:  # Add a goblin archer in the first room
			return True
		elif step == 2:  # Also add two zombies
			return True
		elif step == 3:  # Now generate a room connected to the first one, set in underground Atlantis
			return True
		elif step == 4:  # Put a couple of evil mermaids in Atlantis
			return True
		elif step == 5:  # Place multiple ocean-themed traps in the corridor to Atlantis
			return True
		elif step == 6:  # Place a single treasure chest in all rooms, each containing a piece of a treasure map
			return True
		elif step == 7:  # Remove the chest containing the second piece of the treasure map
			return True
		elif step == 8:  # Add another room connected to Atlantis, set in Hell
			return True
		elif step == 9:  # Place two fallen angels armed with flaming swords
			return True
		elif step == 10:  # Change one of the angels to a capybara monster
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			diff_enemies = [enemy for enemy in new_enemies if enemy.name not in [x.name for x in old_enemies]]
			return len(diff_enemies) == 1
		elif step == 11:  # Set the health of the capybara to 1000
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			diff_enemies = [enemy for enemy in new_enemies if enemy.hp not in [x.hp for x in old_enemies]]
			if diff_enemies:
				return diff_enemies[0].hp == 1000
			else:
				return False
		elif step == 12:  # Make the capybara a punker, with pink spiky hair
			if new_level.current_room not in new_level.rooms: return False
			new_enc = get_encounter(level=new_level, room_name=new_level.current_room, cell_index=-1)
			old_enc = get_encounter(level=old_level, room_name=old_level.current_room, cell_index=-1)
			new_enemies = get_enemies_in_encounter(new_enc)
			old_enemies = get_enemies_in_encounter(old_enc)
			diff_enemies = [enemy for enemy in new_enemies if enemy.description not in [x.description for x in old_enemies]]
			return len(diff_enemies) == 1
		else:
			raise ValueError('Invalid step')
	else:
		raise ValueError("Invalid use case")