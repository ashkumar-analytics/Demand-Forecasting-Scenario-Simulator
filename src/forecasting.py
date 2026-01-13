from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_demand(df, periods=6):
    model = ExponentialSmoothing(
        df["demand_units"],
        trend="additive",
        seasonal=None
    )
    fitted_model = model.fit()
    forecast = fitted_model.forecast(periods)
    return forecast
