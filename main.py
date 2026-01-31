import json
from speech import listen_te, speak_te
from memory import Memory
from agent import TeluguAgent
from tools import TOOLS

def main():
    mem = Memory()
    agent = TeluguAgent(mem)

    speak_te("నమస్తే. నేను మీకు ప్రభుత్వ పథకాలు మరియు ఉద్యోగాల గురించి సహాయం చేస్తాను. మీరు ఏమి కోరుకుంటున్నారు?")

    while True:
        user = listen_te()
        if not user:
            speak_te("క్షమించండి, మళ్లీ చెపండి.")
            continue

        result = agent.think(user)
        data = json.loads(result)

        if data["next_action"] == "ask":
            field = data["field"]
            question = data["question"]
            speak_te(question)

        elif data["next_action"] == "tool":
            tool_name = data["tool_name"]
            output = TOOLS[tool_name](mem.get())
            speak_te("మీ అర్హత ఫలితాలు సిద్ధంగా ఉన్నాయి.")
            speak_te(", ".join(output))

        elif data["next_action"] == "final":
            speak_te(data["final_answer"])
            break


if __name__ == "__main__":
    main()
