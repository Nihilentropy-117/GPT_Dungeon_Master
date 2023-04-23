import Do


class Character:
    def __init__(self, name, race, character_class, hp, ac, stats, level, weapons=None, inventory=None, genlog=None):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.hp = hp
        self.ac = ac
        self.stats = stats
        self.level = level
        self.genlog = genlog
        self.weapons = weapons if weapons else []
        self.inventory = inventory if inventory else []


    def __str__(self):
        output = f"{self.name} ({self.race} {self.character_class})\n"
        output += f"Level: {self.level}\n"
        output += f"Hit Points: {self.hp}\n"
        output += "Ability Scores:\n"
        for ability, score in self.stats.items():
            output += f"    {ability.capitalize()}: {score}\n"
        return output


def Entity_Person(name, race, character_class):
    _genLog = "DEBUG: Data used to Generate\n"

    # Generate ability scores using 4d6 drop lowest method
    ability_scores = {}

    for ability in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
        rolls = [Do.rollD(6) for i in range(4)]
        _genLog += (f"For {ability}: Rolled {rolls}. ")
        drop = min(rolls)
        rolls.remove(drop)
        _genLog += (f"Dropped {drop}: Sum=")
        ability_scores[ability] = sum(rolls)
        _genLog += f"{sum(rolls)}\n"

    # Assign ability scores based on class
    if character_class == 'barbarian':
        ability_scores['strength'] += 4
        ability_scores['dexterity'] += 2
        ability_scores['constitution'] += 2
    elif character_class == 'bard':
        ability_scores['dexterity'] += 2
        ability_scores['charisma'] += 4
    elif character_class == 'cleric':
        ability_scores['wisdom'] += 4
        ability_scores['constitution'] += 2
    elif character_class == 'druid':
        ability_scores['wisdom'] += 4
        ability_scores['constitution'] += 2
    elif character_class == 'fighter':
        ability_scores['strength'] += 4
        ability_scores['constitution'] += 2
    elif character_class == 'monk':
        ability_scores['strength'] += 2
        ability_scores['dexterity'] += 2
        ability_scores['wisdom'] += 2
    elif character_class == 'paladin':
        ability_scores['strength'] += 4
        ability_scores['charisma'] += 2
    elif character_class == 'ranger':
        ability_scores['dexterity'] += 4
        ability_scores['wisdom'] += 2
    elif character_class == 'rogue':
        ability_scores['dexterity'] += 4
        ability_scores['intelligence'] += 2
    elif character_class == 'sorcerer':
        ability_scores['constitution'] += 2
        ability_scores['charisma'] += 4
    elif character_class == 'wizard':
        ability_scores['intelligence'] += 4
        ability_scores['constitution'] += 2

    # Calculate hit points based on character class and constitution modifier
    hp = 0
    if character_class == 'barbarian':
        hp = 12 + ((ability_scores['constitution'] - 10) // 2) * 3
    elif character_class == 'fighter' or character_class == 'paladin' or character_class == 'ranger':
        hp = 10 + ((ability_scores['constitution'] - 10) // 2) * 3
    elif character_class == 'cleric' or character_class == 'druid' or character_class == 'monk' or character_class == 'rogue' or character_class == 'wizard':
        hp = 8 + ((ability_scores['constitution'] - 10) // 2) * 3

    # Set starting skills and number of skill ranks per level
    class_skills = dict(
        barbarian=['Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Knowledge (nature)', 'Perception', 'Ride',
                   'Survival', 'Swim'],
        bard=['Acrobatics', 'Appraise', 'Bluff', 'Climb', 'Diplomacy', 'Disguise', 'Escape Artist', 'Intimidate',
              'Knowledge (arcana)', 'Knowledge (dungeoneering)', 'Knowledge (engineering)', 'Knowledge (geography)',
              'Knowledge (history)', 'Knowledge (local)', 'Knowledge (nature)', 'Knowledge (nobility)',
              'Knowledge (planes)', 'Knowledge (religion)', 'Linguistics', 'Perception', 'Perform', 'Profession',
              'Sense Motive', 'Sleight of Hand', 'Spellcraft', 'Stealth', 'Use Magic Device'],
        cleric=['Appraise', 'Craft', 'Diplomacy', 'Heal', 'Knowledge (arcana)', 'Knowledge (history)',
                'Knowledge (nobility)', 'Knowledge (planes)', 'Knowledge (religion)', 'Linguistics', 'Profession',
                'Sense Motive', 'Spellcraft'],
        druid=['Climb', 'Craft', 'Fly', 'Handle Animal', 'Heal', 'Knowledge (geography)', 'Knowledge (nature)',
               'Perception', 'Profession', 'Ride', 'Spellcraft', 'Survival', 'Swim'])

    class_skills['fighter'] = class_skills['barbarian'] + ['Craft', 'Handle Animal', 'Intimidate',
                                                           'Knowledge (dungeoneering)', 'Knowledge (engineering)',
                                                           'Profession', 'Ride', 'Survival']

    class_skills['monk'] = ['Acrobatics', 'Climb', 'Craft', 'Escape Artist', 'Intimidate', 'Knowledge (history)',
                            'Knowledge (religion)', 'Perception', 'Perform', 'Profession', 'Ride', 'Sense Motive',
                            'Stealth', 'Swim']

    class_skills['paladin'] = class_skills['cleric'] + ['Handle Animal', 'Intimidate', 'Ride', 'Sense Motive'],

    class_skills['ranger'] = class_skills['druid'] + ['Climb', 'Craft', 'Handle Animal', 'Heal',
                                                      'Knowledge (dungeoneering)', 'Knowledge (geography)',
                                                      'Knowledge (nature)', 'Perception',
                                                      'Profession', 'Ride', 'Spellcraft', 'Stealth', 'Survival',
                                                      'Swim'],

    class_skills['rogue'] = ['Acrobatics', 'Appraise', 'Bluff', 'Climb', 'Craft', 'Diplomacy', 'Disable Device',
                             'Disguise', 'Escape Artist', 'Intimidate', 'Knowledge (dungeoneering)',
                             'Knowledge (local)', 'Linguistics', 'Perception', 'Perform', 'Profession', 'Sense Motive',
                             'Sleight of Hand', 'Stealth', 'Swim', 'Use Magic Device'],

    class_skills['wizard'] = ['Appraise', 'Craft', 'Fly', 'Knowledge (arcana)', 'Knowledge (dungeoneering)',
                              'Knowledge (engineering)', 'Knowledge (geography)', 'Knowledge (history)',
                              'Knowledge (local)', 'Knowledge (nature)', 'Knowledge (nobility)', 'Knowledge (planes)',
                              'Knowledge (religion)', 'Linguistics', 'Profession', 'Spellcraft']

    starting_skills = []
    for skill in class_skills[character_class]:
        starting_skills.append({'name': skill, 'ranks': 0, 'class_skill': True})

    starting_weapons = []
    if character_class == 'barbarian' or character_class == 'fighter' or character_class == 'paladin' or character_class == 'ranger':
        starting_weapons.append({'name': 'longsword', 'damage': '1d8'})
    elif character_class == 'bard' or character_class == 'cleric' or character_class == 'druid' or character_class == 'monk' or character_class == 'rogue':
        starting_weapons.append({'name': 'dagger', 'damage': '1d4'})
    elif character_class == 'sorcerer' or character_class == 'wizard':
        starting_weapons.append({'name': 'quarterstaff', 'damage': '1d6'})

    class_ac_values = {
        'barbarian': 15,
        'bard': 13,
        'cleric': 14,
        'druid': 13,
        'fighter': 16,
        'monk': 13,
        'paladin': 16,
        'ranger': 14,
        'rogue': 15,
        'sorcerer': 12,
        'wizard': 12
    }
    # Create the PathfinderCharacter object and return it
    person = Character(
        name=name,
        race=race,
        character_class=character_class,
        hp=hp,
        ac=class_ac_values[character_class],
        genlog=_genLog,
        stats=ability_scores,
        level=3,
        weapons=starting_weapons,
        inventory=['backpack', 'torch', 'rope']
    )
    return person



