# Define the vote dictionary outside the function
vote = {}

def check_voting(name: str):
    if vote.get(name):
        print("Kick him out")
    else:
        print("Vote for this person")
        vote[name] = True
    
    return vote

# Example usage
print(check_voting("Alice"))  # Output: Vote for this person {'Alice': True}
print(check_voting("Bob"))    # Output: Vote for this person {'Alice': True, 'Bob': True}
print(check_voting("Alice"))  # Output: Kick him out {'Alice': True, 'Bob': True}
