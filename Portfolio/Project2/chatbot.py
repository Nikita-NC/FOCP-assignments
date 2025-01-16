import random
import json

def load_config(file):  #loads congigure file from the json file
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Configuration file not found. Exiting.")
        exit()
    except json.JSONDecodeError:
        print("Error decoding the configuration file. Exiting.")
        exit()

def log_session(user_name, log_data):  #save chat log
    try:
        with open(f"{user_name}_chat_log.txt", "w") as f:
            f.write("\n".join(log_data))
    except Exception as e:
        print(f"Error saving the log: {e}")

def generate_agent_name():  #generate random agent names
    return random.choice(["Alex", "Hunter", "Flash", "Xavier", "Jack"])

def random_disconnect():
    return random.random() < 0.05  #return true if the number is less tha 0.05

def main():
    config = load_config("chat_config.json")
    keywords = config.get("keywords", {})
    random_responses = config.get("random_responses", [])

    user_name = input("Welcome! What's your name? ")
    print(f"Hi {user_name}! Nice to meet you.")

    agent_name = generate_agent_name()
    print(f"You're now chatting with Agent {agent_name}. Type 'bye' to exit.")

    conversation_log = [f"User: {user_name}", f"Agent: {agent_name}"]

    while True:
        user_input = input(f"{user_name}: ").strip().lower()
        conversation_log.append(f"{user_name}: {user_input}")

        if user_input in ["bye", "quit", "exit"]:
            farewell = f"Goodbye, {user_name}! Have a great day!"
            print(f"Agent {agent_name}: {farewell}")
            conversation_log.append(f"Agent {agent_name}: {farewell}")
            break

        if random_disconnect():
            print(f"Agent {agent_name}: Oh no, I got disconnected. Please try again later!")
            conversation_log.append(f"Agent {agent_name}: Disconnected.")
            break

        response = None
        for keyword, replies in keywords.items():
            if keyword in user_input:
                response = random.choice(replies).replace("{user_name}", user_name)
                break

        if not response:
            response = random.choice(random_responses).replace("{user_name}", user_name)

        print(f"Agent {agent_name}: {response}")
        conversation_log.append(f"Agent {agent_name}: {response}")

    log_session(user_name, conversation_log)

if __name__ == "__main__":
    main()
        