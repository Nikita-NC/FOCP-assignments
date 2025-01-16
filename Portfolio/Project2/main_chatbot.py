import json
import re
import random

def load_json(file):
    try:
        with open(file, "r") as bot_responses:
            print(f"Loaded '{file}' successfully!")
            return json.load(bot_responses)
    except FileNotFoundError:
        print(f"Configuration file '{file}' not found. Exiting.")
        exit() 
    except json.JSONDecodeError:
        print(f"Error decoding the configuration file '{file}'. Exiting.")
        exit()

def log_session(user_name, log_data):
    try:
        with open(f"{user_name}_chat_log.txt", "w") as f:
            f.write("\n".join(log_data))
    except Exception as e:
        print(f"Error saving the log: {e}")

def generate_agent_name():
    return random.choice(["Alex", "Hunter", "Flash", "Xavier", "Jack"])

def random_disconnect():
    return random.random() < 0.05

def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet.",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]

    return random.choice(random_list)

def get_response(input_string, response_data):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if input_string.strip() == "":
        return "Please type something so we can chat :("

    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_string()

def main():
    response_data = load_json("bot.json")
    user_name = input("Welcome! What's your name? ").strip()
    if not user_name:
        print("Name cannot be empty! Restarting...")
        return

    print(f"Hi {user_name}! Nice to meet you.")

    agent_name = generate_agent_name()
    print(f"You're now chatting with Agent {agent_name}. Type 'bye' to exit.")
    conversation_log = [f"User: {user_name}", f"Agent: {agent_name}"]

    while True:
        user_input = input(f"{user_name}: ").strip()
        conversation_log.append(f"{user_name}: {user_input}")

        if user_input.lower() in ["bye", "quit", "exit"]:
            farewell = f"Goodbye, {user_name}! Have a great day!"
            print(f"Agent {agent_name}: {farewell}")
            conversation_log.append(f"Agent {agent_name}: {farewell}")
            break

        if random_disconnect():
            print(f"Agent {agent_name}: Oh no, I got disconnected. Please try again later!")
            conversation_log.append(f"Agent {agent_name}: Disconnected.")
            break

        response = get_response(user_input, response_data)
        print(f"Agent {agent_name}: {response}")
        conversation_log.append(f"Agent {agent_name}: {response}")

    log_session(user_name, conversation_log)

if __name__ == "__main__":
    main()