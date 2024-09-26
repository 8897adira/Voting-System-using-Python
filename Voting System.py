# Initialize nominees
nominee1 = "Candidate 1"
nominee2 = "Candidate 2"

# Initialize vote counts
nm1_votes = 0
nm2_votes = 0

# List of voter IDs
voter_id = [1001, 1002, 1003, 1004, 1005]  # You can add as many voter IDs as needed
total_voters = len(voter_id)  # To track how many voters are there initially

def display_results():
    # Display the vote count and percentages for each candidate
    print("\n--- Voting Results ---")
    print(f"Total votes for {nominee1}: {nm1_votes}")
    print(f"Total votes for {nominee2}: {nm2_votes}")
    total_votes = nm1_votes + nm2_votes
    if total_votes > 0:
        percent_nm1 = (nm1_votes / total_votes) * 100
        percent_nm2 = (nm2_votes / total_votes) * 100
        print(f"{nominee1} received {percent_nm1:.2f}% of the vote.")
        print(f"{nominee2} received {percent_nm2:.2f}% of the vote.")
    else:
        print("No votes have been cast.")

def reset_voting():
    global nm1_votes, nm2_votes, voter_id
    nm1_votes = 0
    nm2_votes = 0
    voter_id = [1001, 1002, 1003, 1004, 1005]  # Reset to original voter list
    print("\nVoting system reset successfully!")

while True:
    mode = input("Enter 'voter' to vote or 'admin' to manage: ").lower()
    
    if mode == 'voter':
        if len(voter_id) == 0:
            print("Voting is complete! No more voters available.")
            break

        try:
            voter = int(input("Enter your voter ID: "))
        except ValueError:
            print("Invalid input. Please enter a valid voter ID.")
            continue

        if voter in voter_id:
            print("You are a valid voter")
            voter_id.remove(voter)  # Remove voter to prevent duplicate voting
            print("------------------------------------------")
            print(f"To give vote to {nominee1}, Press 1")
            print(f"To give vote to {nominee2}, Press 2")
            print("------------------------------------------")

            try:
                vote = int(input("Enter your precious vote (1 or 2): "))
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
                continue

            if vote == 1:
                nm1_votes += 1
                print(f"{nominee1} thanks you for your important vote!")
            elif vote == 2:
                nm2_votes += 1
                print(f"{nominee2} thanks you for your important vote!")
            else:
                print("Invalid vote. Please enter either 1 or 2.")
        else:
            print("Invalid voter ID or you have already voted.")

    elif mode == 'admin':
        admin_choice = input("Enter 'results' to see results, 'reset' to reset voting, or 'end' to stop voting: ").lower()
        if admin_choice == 'results':
            display_results()
        elif admin_choice == 'reset':
            reset_voting()
        elif admin_choice == 'end':
            print("Voting is now closed.")
            display_results()
            break
        else:
            print("Invalid input. Please try again.")
    
    else:
        print("Invalid mode. Please enter 'voter' or 'admin'.")
    
    # Automatically stop voting when all voters have cast their votes
    if len(voter_id) == 0:
        print("\nAll voters have cast their votes. Voting is now closed.")
        display_results()
        break
