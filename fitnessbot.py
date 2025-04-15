# Simple Fitness Recommendation Script

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"
    return bmi, status

def suggest_workout(goal):
    workouts = {
        "1": ["Cardio (Running, Cycling)", "HIIT Workouts", "Jump Rope"],
        "2": ["Weight Lifting", "Bodyweight Exercises", "Progressive Overload"],
        "3": ["Yoga", "Stretching", "Pilates"],
        "4": ["Walking", "Swimming", "Light Cardio"]
    }
    return workouts.get(goal, ["No workout suggestions available"])

def suggest_diet(goal):
    diets = {
        "1": ["Lean protein", "Vegetables", "Low-carb diet"],
        "2": ["High protein diet", "Healthy fats", "Complex carbs"],
        "3": ["Balanced diet", "Hydration", "Anti-inflammatory foods"],
        "4": ["Fruits", "Nuts", "Whole grains"]
    }
    return diets.get(goal, ["No diet suggestions available"])

def main():
    print("🏋️ Welcome to the Fitness Recommendation System")

    # BMI
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi, status = calculate_bmi(weight, height)
    print(f"\nYour BMI is {bmi:.2f} ({status})")

    # Goals
    print("\nChoose your fitness goal:")
    print("1. Weight Loss")
    print("2. Muscle Gain")
    print("3. Flexibility")
    print("4. General Fitness")
    goal = input("Enter the number of your goal: ")

    # Recommendations
    print("\n🏋️ Recommended Workouts:")
    for workout in suggest_workout(goal):
        print(f"- {workout}")

    print("\n🥗 Recommended Diet:")
    for item in suggest_diet(goal):
        print(f"- {item}")

if __name__ == "__main__":
    main()
