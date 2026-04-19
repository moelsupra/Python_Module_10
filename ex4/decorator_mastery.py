from collections.abc import Callable
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.8f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = next((arg for arg in args if isinstance(arg, int)), 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying..."
                          f" (attempt {attempt + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c == ' ' for c in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(0.1)
        return f"Fireball cast on {target} -> {power}!"

    result = fireball("Dragon", 10)
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise Exception("Spell unstable!")
    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def lucky_spell() -> str:
        return "Waaaaaaagh spelled !"
    print(lucky_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()

    try:
        print(MageGuild.validate_mage_name("Amine"))
        print(MageGuild.validate_mage_name("A1"))
        print(guild.cast_spell("Lightning", 15))
        print(guild.cast_spell("Fire", 5))
    except Exception as e:
        print(f"Error: {e}")
