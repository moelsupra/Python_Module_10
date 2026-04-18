def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(
        filter(lambda mage: mage.get('power', 0) >= min_power, mages)
        )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    powers = list(map(lambda mage: mage.get('power', 0), mages))

    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Shadow Cloak', 'power': 60, 'type': 'armor'},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")

    print("Before sorting:")
    for artifact in artifacts:
        print(f"  {artifact['name']} - power: {artifact['power']}")

    sorted_artifacts = artifact_sorter(artifacts)

    print("After sorting:")
    for artifact in sorted_artifacts:
        print(f"  {artifact['name']} - power: {artifact['power']}")

    print("\nTesting power filter...")
    filtered = power_filter(artifacts, 70)
    for mage in filtered:
        print(f"{mage['name']} passed with power {mage['power']}")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    for spell in transformed:
        print(spell)

    print("\nTesting mage stats...")
    stats = mage_stats(artifacts)
    print(stats)
