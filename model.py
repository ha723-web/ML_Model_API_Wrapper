# model.py

def predict_price(labor_cost, material_cost):
    """
    Simple pricing logic: cost + 20% markup
    """
    return round(labor_cost + material_cost + 0.2 * (labor_cost + material_cost), 2)
