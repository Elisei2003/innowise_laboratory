
def generate_profile(age):
    """
    Determines the life stage based on age.
    Args:
        age (int): The calculated age of the user.
    Returns:
        str: The corresponding life stage ("Child", "Teenager", or "Adult").
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:  # 20 or older
        return "Adult"

def run_mini_profile_generator():
    """
    Gathers user data, calculates age, collects hobbies, and displays the final profile.
    """
    CURRENT_YEAR = 2025

    print("--- Welcome to the Mini-Profile Generator ---")

    # 2. Get User Input

    # Name
    user_name = input("Please enter your full name: ")

    # Birth Year (with basic validation)
    while True:
        try:
            birth_year_str = input("Please enter your birth year (e.g., 1990): ")
            birth_year = int(birth_year_str)
            if birth_year > CURRENT_YEAR or birth_year < 1900:
                print(f"Warning: Year {birth_year} seems unusual. Please enter a valid year.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for the birth year.")

    # Calculate Age
    current_age = CURRENT_YEAR - birth_year

    # Gather Hobbies
    hobbies = []
    print("\n--- Hobby Collection ---")
    while True:
        hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ").strip()

        # Check for stop condition (case-insensitive)
        if hobby_input.lower() == "stop":
            break

        # Add hobby if input is not empty
        if hobby_input:
            hobbies.append(hobby_input)
        else:
            print("Hobby cannot be empty. Try again.")

    # 3. Process and Generate the Profile

    # Call the function to get the life stage
    life_stage = generate_profile(current_age)

    # Create the profile dictionary
    user_profile = {
        "name": user_name,
        "age": current_age,
        "birth_year": birth_year,
        "life_stage": life_stage,
        "hobbies": hobbies
    }

    # 4. Display the Output
    print("\n========================================")
    print("          FINAL USER PROFILE")
    print("========================================")
    print(f"Name: {user_profile['name']}")
    print(f"Current Age (based on {CURRENT_YEAR}): {user_profile['age']} years old")
    print(f"Life Stage: {user_profile['life_stage']}")
    print("----------------------------------------")

    # Display Hobbies section
    if not user_profile['hobbies']:
        print("You didn't mention any hobbies.")
    else:
        num_hobbies = len(user_profile['hobbies'])
        print(f"Favorite Hobbies ({num_hobbies}):")
        for hobby in user_profile['hobbies']:
            print(f"- {hobby}")

    print("========================================")


if __name__ == "__main__":
    run_mini_profile_generator()
