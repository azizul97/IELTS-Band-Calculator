def validate_score(score):
    """
    Validate that the input score is a valid IELTS band score (0 to 9, in 0.5 increments).
    """
    try:
        score = float(score)
        if 0 <= score <= 9 and (score * 2).is_integer():
            return score
        else:
            raise ValueError
    except ValueError:
        print("Invalid score. Please enter a number between 0 and 9 in increments of 0.5.")
        return None

def calculate_overall_band(listening, reading, writing, speaking):
    """
    Calculate the overall IELTS band score based on the four module scores.
    """
    average_score = (listening + reading + writing + speaking) / 4
    # Round to the nearest 0.5 band
    overall_band = round(average_score * 2) / 2
    return overall_band

def main():
    print("Welcome to the IELTS Band Score Calculator***")

    # Collect scores for each module
    modules = ["Listening", "Reading", "Writing", "Speaking"]
    scores = {}

    for module in modules:
        while True:
            score = input(f"Enter your {module} score (0-9, increments of 0.5): ")
            validated_score = validate_score(score)
            if validated_score is not None:
                scores[module] = validated_score
                break

    # Calculate overall band score
    overall_band = calculate_overall_band(
        scores["Listening"], scores["Reading"], scores["Writing"], scores["Speaking"]
    )

    # Display results
    print("\nYour IELTS Scores:")
    for module, score in scores.items():
        print(f"{module}: {score}")

    print(f"Overall Band Score: {overall_band}")

if __name__ == "__main__":
    main()