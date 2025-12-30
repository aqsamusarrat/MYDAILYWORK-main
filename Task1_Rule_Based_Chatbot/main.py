class RuleBot:
    """
    This class defines a simple rule-based chatbot.
    It responds based on predefined rules and keywords. 
    """

    negative_responses = (
        "no",
        "nope",
        "nah",
        "not a chance",
        "never",
    )

    exit_commands = (
        "quit",
        "pause",
        "exit",
        "goodbye",
        "bye",
    )

    def __init__(self):
        """
        Constructor method.
        This runs automatically when the object is created.
        """
        self.bot_name = "RuleBot"

    def greet_user(self):
        """
        Displays a welcome message.
        """
        print("=" * 40)
        print(f"Hello! I am {self.bot_name}.")
        print("I am a simple rule-based chatbot.")
        print("Type 'exit' anytime to leave the chat.")
        print("=" * 40)

    def get_user_input(self):
        """
        Takes input from the user and convert it to lowercase.
        """
        user_input = input("You: ")
        return user_input.lower()

    def check_exit(self, user_input):
        """
        Checks if the user wants to exit the chat.
        """
        return user_input in self.exit_commands

    def generate_response(self, user_input):
        """
        Generates a response based on user input.
        """
        if user_input in self.negative_responses:
            return "Alright, let me know if you change your mind."
        elif "hello" in user_input or "hi" in user_input:
            return "Hello there! How can I help you today?"
        elif "who are you" in user_input:
            return "I am a rule-based chatbot created using Python."
        elif "learn" in user_input or "study" in user_input:
            return "Learning step by step every day is the key to success."
        else:
            return "Interesting! Tell me more."

    def start_chat(self):
        """
        Starts the chatbot conversation loop.
        """
        self.greet_user()

        while True:
            user_input = self.get_user_input()

            if self.check_exit(user_input):
                print(f"{self.bot_name}: Goodbye! Have a great day.")
                break
            response = self.generate_response(user_input)
            print(f"{self.bot_name}: {response}")


if __name__ == "__main__":
    bot = RuleBot()
    bot.start_chat()













































































