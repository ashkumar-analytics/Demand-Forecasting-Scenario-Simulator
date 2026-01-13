def simulate_scenarios(base_forecast, shock_percentage):
    scenarios = {
        "base": base_forecast,
        "high_demand": base_forecast * (1 + shock_percentage),
        "low_demand": base_forecast * (1 - shock_percentage)
    }
    return scenarios
