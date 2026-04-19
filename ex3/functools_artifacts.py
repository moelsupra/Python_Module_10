from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        'add': add,
        'multiply': mul,
        'max': lambda a, b: max(a, b),
        'min': lambda a, b: min(a, b),
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment, 50, 'lightning'),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return cast


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    try:
        print(f"Sum: {spell_reducer(spells, 'add')}")
        print(f"Product: {spell_reducer(spells, 'multiply')}")
        print(f"Max: {spell_reducer(spells, 'max')}")
        print(f"Min: {spell_reducer(spells, 'min')}")
    except Exception as e:
        print(f"  Error: {e}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} enchantment on {target} with {power} power"
    try:
        enchanters = partial_enchanter(base_enchantment)
        for enchant in enchanters.values():
            print(f"{enchant('Sword')}")
    except Exception as e:
        print(f"  Error: {e}")

    print("\nTesting memoized fibonacci...")
    try:
        for n in [0, 1, 10, 15]:
            print(f"Fib({n}): {memoized_fibonacci(n)}")
        print(f"  Cache info: {memoized_fibonacci.cache_info()}")
    except ValueError as e:
        print(f"  Error: {e}")

    print("\nTesting spell dispatcher...")
    try:
        cast = spell_dispatcher()
        print(f"{cast(42)}")
        print(f"{cast('fireball')}")
        print(f"{cast(['fire', 'ice', 'lightning'])}")
        print(f"{cast(3.14)}")
    except Exception as e:
        print(f"  Error: {e}")
