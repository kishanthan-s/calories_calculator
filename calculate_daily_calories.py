def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    elif activity_level== "very active":
        calories = bmr * 1.725
    else:
        raise ValueError("Choose a given active level")
    return calories