# Name Card Generator (Console App)

def generate_card():
    print("Name Card Generator")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    contact = input("Enter your contact number: ")

    card = f"""
    ---------------------------
    | Name   : {name}
    | Email  : {email}
    | Contact: {contact}
    ---------------------------
    """

    print(card)

    save = input("Do you want to save this as a .txt file? (yes/no): ").strip().lower()
    if save == 'yes':
        with open("name_card.txt", "w") as file:
            file.write(card)
        print("Card saved as 'name_card.txt'.")

if __name__ == "__main__":
    generate_card()
