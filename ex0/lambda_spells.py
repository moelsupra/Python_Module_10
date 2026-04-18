def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact : artifact['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage.get('power', 0) >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))

def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage.get('power', 0), mages))

    return {
        'max_power' : max(powers),
        'min_power' : min(powers),
        'avg_power' : round(sum(powers) / len(powers), 2),
    }
