# Simple Fitness Recommendation Script

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        status = "Normal weight"
    elif 25 <= bmi <= 29.9:
        status = "Overweight"
    else:
        status = "Obese"
    return bmi, status


def suggest_workout(goal, bmi_status):
    workouts_by_bmi = {
        "Underweight": {
            "1": ["Light Cardio", "Yoga", "Walking"],
            "2": ["Strength Training (Bodyweight)", "Resistance Bands", "Pilates"],
            "3": ["Gentle Yoga", "Mobility Work", "Stretching"],
            "4": ["Walking", "Light Cardio", "Swimming"]
        },
        "Normal weight": {
            "1": ["Running", "HIIT", "Cycling"],
            "2": ["Weight Lifting", "Bodyweight Exercises", "Split Training"],
            "3": ["Yoga", "Pilates", "Stretch Routines"],
            "4": ["Swimming", "Moderate Cardio", "Functional Training"]
        },
        "Overweight": {
            "1": ["Low-Impact Cardio (Elliptical, Walking)", "Water Aerobics", "Light HIIT"],
            "2": ["Bodyweight Strength", "Resistance Bands", "Low-impact Lifting"],
            "3": ["Stretching", "Chair Yoga", "Tai Chi"],
            "4": ["Swimming", "Stationary Bike", "Rowing"]
        },
        "Obese": {
            "1": ["Walking", "Water Walking", "Chair Exercises"],
            "2": ["Resistance Bands", "Seated Strength Training", "Beginner Weights"],
            "3": ["Chair Yoga", "Stretching", "Breathing Exercises"],
            "4": ["Light Swimming", "Recumbent Bike", "Slow-paced Walks"]
        }
    }

    return workouts_by_bmi.get(bmi_status, {}).get(goal, ["No workout suggestions available"])


def suggest_diet(goal, bmi_status):
    diet_by_bmi = {
        "Underweight": {
            "1": ["More frequent meals", "Healthy fats", "Smoothies with protein"],
            "2": ["High-calorie healthy foods", "Protein shakes", "Nut butters"],
            "3": ["Balanced, anti-inflammatory foods", "Omega-3 rich foods", "Nutrient-dense veggies"],
            "4": ["Whole grains", "Avocados", "Lean protein"]
        },
        "Normal weight": {
            "1": ["Slight calorie deficit", "Lean protein", "Lots of vegetables"],
            "2": ["High protein meals", "Complex carbs", "Healthy fats"],
            "3": ["Balanced diet", "Anti-inflammatory foods", "Plenty of water"],
            "4": ["Whole foods", "Hydration", "Moderate portion sizes"]
        },
        "Overweight": {
            "1": ["Low-carb diet", "High fiber", "Intermittent fasting (if suitable)"],
            "2": ["Moderate protein", "Vegetables with every meal", "Smaller portions"],
            "3": ["Anti-inflammatory foods", "Green tea", "Whole grains"],
            "4": ["Balanced diet", "Low sugar intake", "Mindful eating"]
        },
        "Obese": {
            "1": ["Very low-carb", "High fiber", "Avoid sugary drinks"],
            "2": ["Protein-rich but portion-controlled", "Low-calorie, nutrient-dense foods"],
            "3": ["Anti-inflammatory foods", "Small, frequent meals", "Limit sodium"],
            "4": ["Fruits and vegetables", "Light meals", "Hydration focus"]
        }
    }

    return diet_by_bmi.get(bmi_status, {}).get(goal, ["No diet suggestions available"])


def main():
    print("🏋️ Welcome to the Fitness Recommendation System")

    # Input: Weight & Height
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        if weight <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        print("⚠️ Please enter valid positive numbers for weight and height.")
        return

    # BMI Calculation
    bmi, status = calculate_bmi(weight, height)
    print(f"\n📊 Your BMI is {bmi:.2f} ({status})")

    # Input: Fitness Goal
    print("\n🎯 Choose your fitness goal:")
    print("1. Weight Loss")
    print("2. Muscle Gain")
    print("3. Flexibility")
    print("4. General Fitness")
    goal = input("Enter the number of your goal: ")

    if goal not in ["1", "2", "3", "4"]:
        print("⚠️ Invalid goal selected. Please choose a number between 1 and 4.")
        return

    # Workouts
    print("\n🏋️ Recommended Workouts:")
    for workout in suggest_workout(goal, status):
        print(f"- {workout}")

    # Diet
    print("\n🥗 Recommended Diet:")
    for item in suggest_diet(goal, status):
        print(f"- {item}")


if __name__ == "__main__":
    main()
