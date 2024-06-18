def count_words(text):
    """Function to count the number of words in a given text."""
    if not text.strip():  # Check if the text is empty or consists only of whitespace
        return 0
    words = text.split()  # Split the text by whitespace to get a list of words
    return len(words)  # Return the number of words in the list

def main():
    """Main function to interact with the user and display word count."""
    print("Welcome to the Word Count Tool!")
    print("Please enter a sentence or paragraph:")
    user_input = input()  # Prompt the user to enter text

    # Calculate the word count using the function
    num_words = count_words(user_input)

    # Display the result
    if num_words == 0:
        print("You have entered an empty sentence or paragraph.")
    else:
        print(f"The total number of words entered is: {num_words}")

if __name__ == "__main__":
    main()
