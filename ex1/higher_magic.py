from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def wrapped(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return wrapped


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        return [spell(target, power) for spell in spells]
    return sequence










# def fireball(target: str, power: int) -> str:
#     return f"Fireball hits {target} with {power} damage"

# def heal(target: str, power: int) -> str:
#     return f"Heal restores {target} for {power} HP"

# combined = spell_combiner(fireball, heal)
# result = combined("test", 25)
# print(result)

# amp = power_amplifier(fireball, 5)
# res = amp("Amine", 5)
# print(res)