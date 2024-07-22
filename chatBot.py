class WeightLossChatbot:
    def __init__(self):
        self.user_data = {}

    def greet_user(self):
        print("Hi! I'm your Weight Loss Chatbot. Let's get started!")

    def get_user_info(self):
        print("Please provide some information about yourself:")
        self.user_data['weight'] = float(input("Enter your weight (in kg): "))
        self.user_data['height'] = float(input("Enter your height (in meters): "))
        self.user_data['age'] = int(input("Enter your age: "))
        self.user_data['activity_level'] = input("Enter your activity level (sedentary/light/moderate/heavy): ").lower()
        self.user_data['exercise_per_week'] = int(input("How many days do you exercise per week? "))

    def calculate_bmi(self):
        bmi = self.user_data['weight'] / (self.user_data['height'] ** 2)
        return bmi

    def recommend_calories(self):
        if self.user_data['activity_level'] == 'sedentary':
            calories = 1.2 * (655 + (9.6 * self.user_data['weight']) + (1.8 * self.user_data['height'] * 100) - (4.7 * self.user_data['age']))
        elif self.user_data['activity_level'] == 'light':
            calories = 1.375 * (655 + (9.6 * self.user_data['weight']) + (1.8 * self.user_data['height'] * 100) - (4.7 * self.user_data['age']))
        elif self.user_data['activity_level'] == 'moderate':
            calories = 1.55 * (655 + (9.6 * self.user_data['weight']) + (1.8 * self.user_data['height'] * 100) - (4.7 * self.user_data['age']))
        elif self.user_data['activity_level'] == 'heavy':
            calories = 1.725 * (655 + (9.6 * self.user_data['weight']) + (1.8 * self.user_data['height'] * 100) - (4.7 * self.user_data['age']))
        else:
            print("Invalid activity level. Please enter sedentary/light/moderate/heavy.")
            return

        return calories - (500 * self.user_data['exercise_per_week'])

    def provide_advice(self):
        bmi = self.calculate_bmi()
        print(f"Your BMI is {bmi:.2f}")

        recommended_calories = self.recommend_calories()
        print(f"To lose weight, you should consume around {recommended_calories:.0f} calories per day.")

        print("Here are some general tips for weight loss:")
        print("- Eat a balanced diet rich in fruits, vegetables, lean proteins, and whole grains.")
        print("- Limit processed foods, sugary drinks, and unhealthy snacks.")
        print("- Stay hydrated by drinking plenty of water throughout the day.")
        print("- Get regular exercise, including both cardio and strength training.")
        print("- Aim for at least 7-9 hours of quality sleep each night.")

    def run(self):
        self.greet_user()
        self.get_user_info()
        self.provide_advice()

if __name__ == "__main__":
    chatbot = WeightLossChatbot()
    chatbot.run()
