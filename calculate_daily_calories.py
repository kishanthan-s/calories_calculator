def calculate_daily_calories(bmr, activity_level):
    if activity_level == "1":
        calories = bmr * 1.2
    elif activity_level == "2":
        calories = bmr * 1.375
    elif activity_level == "3":
        calories = bmr * 1.55
    elif activity_level== "4":
        calories = bmr * 1.725
    else:
        raise ValueError("Choose a given active level")
    return calories