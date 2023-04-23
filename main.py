import Do
import Make
import PlayerActions

player_character = Make.Entity_Person(name='Player', race='human', character_class='fighter')
print(player_character.genlog)
print(player_character)

npc_foe = Make.Entity_Person(name='NPC', race='goblin', character_class='rogue')

CombatResult = PlayerActions.Combat(player_character, npc_foe)
print(CombatResult[1])
print(CombatResult[0])
