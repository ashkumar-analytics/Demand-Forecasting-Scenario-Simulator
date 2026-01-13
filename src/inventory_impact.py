def inventory_gap(scenarios, planned_inventory):
    gaps = {}
    for scenario, demand in scenarios.items():
        gaps[scenario] = planned_inventory - demand.sum()
    return gaps
