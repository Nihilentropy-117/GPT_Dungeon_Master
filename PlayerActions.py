import Do
import GPT


def Combat(Attacker, Defender):
    _combat = Do.Combat(Attacker, Defender)
    CombatData = _combat.fight()
    CombatPrompt = f"You are a Dungeons and Dragons Dungeon Master, running a game. Describe the following battle in " \
                   f"epic narrative. {CombatData[0]} Make sure to include all numbers, and do not leave out any actions."

    # CombatPrompt = [Narrative, Log]
    CombatNarrative = GPT.call(CombatPrompt, 500)
    CombatLog = CombatData[1]
    ret = [CombatNarrative, CombatLog]
    return ret
