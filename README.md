# Voice-Based Native Language Welfare Scheme Agent

##  Overview
This project implements a **voice-first, agentic AI system** that helps users identify and apply for **government/public welfare schemes** based on their eligibility.  
The agent operates **end-to-end in a native Indian language** (non-English) and demonstrates **reasoning, planning, tool usage, memory, and failure handling**, going beyond a simple chatbot.

The system supports:
- Voice input (Speech-to-Text)
- Agentic decision-making
- Eligibility checking using tools
- Conversation memory across turns
- Voice output (Text-to-Speech)
- Graceful handling of incomplete or incorrect inputs

---

##  Objective
To build a **native-language service agent** that can:
- Understand user requests via voice
- Determine eligibility for welfare schemes
- Ask follow-up questions when information is missing
- Maintain context across multiple interactions
- Respond back using voice output

---

##  Agent Architecture
The system follows an **agentic workflow**:

1. **Input Layer**  
   - User speaks in a native Indian language
   - Speech converted to text (STT)

2. **Agent Reasoning Layer**
   - Planner: decides next action
   - Executor: calls tools (eligibility checks, retrieval)
   - Evaluator: verifies responses and handles failures

3. **Tools Layer**
   - Eligibility Engine
   - External / mock APIs
   - Utility tools

4. **Memory Layer**
   - Stores conversation history
   - Handles contradictions and follow-ups

5. **Output Layer**
   - Generates native-language response
   - Converts text back to speech (TTS)



## Project Structure

├── README.md               # Project documentation
├── main.py                 # Entry point for the application
├── agent.py                # Core agent logic (planning, execution)
├── config.py               # Configuration and constants
├── eligibility.py          # Eligibility checking logic for schemes
├── memory.py               # Conversation memory management
├── speech.py               # Speech-to-Text and Text-to-Speech pipeline
├── tools.py                # Tools used by the agent
└── test_google_stt.py      # Test file for Google STT integration


##  Demo Video
A live demonstration showcasing:
- Voice-based interaction in a native Indian language
- Agent reasoning and planning
- Tool usage for eligibility checking
- Conversation memory across turns
- Error handling and recovery

 **Demo Link:**  
<https://drive.google.com/file/d/1E_rHVWab9QhI9xmBQXQnOZcl40H8y7tP/view?usp=sharing>
