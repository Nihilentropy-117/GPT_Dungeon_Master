import random


class Combat:

    def __init__(self, player_character, npc_foe):
        self.player_character = player_character
        self.npc_foe = npc_foe
        self.output = ""
        self.log = ""

    def attack(self, attacker, defender):q
        attack_roll = random.randint(1, 20) + ((attacker.stats['strength'] - 10) / 2)
        self.output += f"{attacker.name} rolled a {attack_roll} to hit {defender.name}: AC of {defender.ac}\n"
        if attack_roll >= defender.ac:
            damage_roll = random.randint(1, 6) + ((attacker.stats['strength'] - 10) / 2)
            defender.hp -= damage_roll

            self.output += f"{attacker.name} hits {defender.name} for {damage_roll} damage!\n"
            self.log += f"{attacker.name}:{attack_roll} vs {defender.name}:{defender.ac} | Hit:{damage_roll}\n"
        else:
            self.output += f"{attacker.name} misses {defender.name}!\n"
            self.log += f"{attacker.name}:{attack_roll} vs {defender.name}:{defender.ac} | Miss\n"

    def fight(self):
        self.output += f"{self.player_character.name} ({self.player_character.character_class}) vs {self.npc_foe.name} ({self.npc_foe.character_class})!\n"
        while self.player_character.hp > 0 and self.npc_foe.hp > 0:
            self.output += f"{self.player_character.name} ({self.player_character.hp} hp) attacks {self.npc_foe.name} ({self.npc_foe.hp} hp)!\n"
            self.attack(self.player_character, self.npc_foe)
            if self.npc_foe.hp <= 0:
                self.output += f"{self.npc_foe.name} is defeated!\n"
                break
            self.output += f"{self.npc_foe.name} ({self.npc_foe.hp} hp) attacks {self.player_character.name} ({self.player_character.hp} hp)!\n"
            self.attack(self.npc_foe, self.player_character)
            if self.player_character.hp <= 0:
                self.output += f"{self.player_character.name} is defeated!\n"
                break
        self.output += "Combat over!\n"
        ret = [self.output, self.log]
        return ret


def rollD(x):
    roll = random.randrange(1, x + 1)
    return roll
