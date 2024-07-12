total_jacks = 100
completed_jacks = 0

while completed_jacks < total_jacks:
    print(f"Perform 10 jumping jacks!")
    input("Press Enter when done...")
    completed_jacks += 10
    print(f"Are you tired? (yes/no)")
    response = input().lower()
    if response in ["yes", "y"]:
        print("Do you want to skip the remaining sets? (yes/no)")
        response = input().lower()
        if response in ["yes", "y"]:
            print(f"You completed a total of {completed_jacks} jumping jacks.")
            break
        remaining_jacks = total_jacks - completed_jacks
        print(f"{remaining_jacks} jumping jacks remaining.")
    else:
        print("Congratulations! You completed the workout!")
