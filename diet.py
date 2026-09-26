def bmi_calculator(Weight,Height):
    bmi = Weight/((Height/100)**2) 
    return round(bmi,2)

def bmr_calculator(Gender,Age,Weight,Height):
    if Gender == "Male":
        bmr = (10 * Weight) + (6.25 * Height) - (5 * Age) + 5
        return bmr
    elif Gender == "Female":
        bmr = (10 * Weight) + (6.25 * Height) - (5 * Age) - 161
        return bmr 

def tdee_calculator(bmr,Activity):
    activity_factor = {"Sedentary":1.20,
                       "Lightly Active":1.375,
                       "Moderately Active":1.55,
                       "Very Active":1.725,
                       "Extra Active":1.90}
    tdee = bmr * activity_factor[Activity]
    return round(tdee,2) 

def calorie_target(tdee,Aim):
    if Aim == "weight maintain":
        calorie = tdee
    elif Aim == "weight loss":
        calorie = tdee - 400
    elif Aim == "weight gain":
        calorie = tdee + 300
    return round(calorie,2) 

# print(bmi_calculator(65,150))
# bmr = bmr_calculator("female",20,60,165)
# tdee = tdee_calculator(bmr,"Very Active")
# print(calorie_target(tdee,"weight loss"))

