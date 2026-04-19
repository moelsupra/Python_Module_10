from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def wrapped(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return wrapped


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {mega('Dragon', 10)}")
    giga = power_amplifier(fireball, 8)
    print(f"Original: 5, Amplified: {giga('Ghost', 5)}")
    double = power_amplifier(fireball, 2)
    print(f"Double amplified: {double('Dragon', 10)}")

    print("\nTesting conditional caster...")
    strong_enough = conditional_caster(
        lambda target, power: power >= 20, fireball
    )
    print(strong_enough("Dragon", 25))
    print(strong_enough("Dragon", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))
