# Voice-Based Government Services Agent 

##  Project Overview

This project is a **voice-based government services assistant** that helps users discover **government jobs** and **government welfare schemes** based on eligibility.  
The system works **entirely in Telugu**, supporting **voice input and voice output**, and follows a **hybrid agentic architecture** combining **Generative AI (Gemini)** with **rule-based tools** to ensure correctness and reliability.

This approach avoids hallucinations and reflects how **real-world government AI systems** are designed.

---

##  Key Features

-  Telugu **Voice Input** (Speech-to-Text)
-  Telugu **Voice Output** (Text-to-Speech)
-  **Gemini LLM** for intent detection (Job / Scheme)
-  Agentic workflow (Listen → Reason → Act → Respond)
-  Multiple tools for jobs and schemes
-  Intelligent fallback for other locations/departments
-  Conversation memory
-  Speech failure recovery

---

## System Architecture (High Level)
User (Telugu Voice)
        ↓
Speech-to-Text (STT)
        ↓
Intent Detection (Gemini API)
        ↓
Agent Controller (main.py)
        ↓
Tools Layer
  ├─ Job Eligibility Tool
  └─ Scheme Eligibility Tool
        ↓
Response Builder (Telugu)
        ↓
Text-to-Speech (TTS)
        ↓
User (Telugu Voice)

- **LISTEN**: Capture Telugu voice input  
- **REASON**: Identify intent using Gemini  
- **ACT**: Invoke job or scheme tools  
- **RESPOND**: Speak results in Telugu  

---

##  Tools and APIs Used

###  Gemini API
- Used **only for intent detection**
- Identifies whether the user wants:
  - Government jobs
  - Government schemes
- Not used for factual data (prevents hallucination)

###  Speech-to-Text (STT)
- Converts Telugu voice to text
- Retries when speech is unclear

###  Text-to-Speech (TTS)
- Converts Telugu text to Telugu voice
- Used for all responses

###  Rule-Based Tools
- Job eligibility engine
- Scheme eligibility engine
- Operates on mock government datasets

---

##  Project Structure


└── Agent
    ├── main.py        # Agent controller & workflow
    ├── speech.py      # Speech-to-text and text-to-speech
    ├── tools.py       # Job & scheme eligibility logic
    ├── gemini.py      # Gemini intent detection
    ├── memory.py      # Conversation memory
    └── README.md      # Project documentation


---

##  File Descriptions

### `main.py`
- Central agent controller
- Manages conversation flow
- Calls Gemini and tools
- Handles fallback and errors
- Maps Telugu inputs to internal values

### `speech.py`
- Handles Telugu voice input (STT)
- Handles Telugu voice output (TTS)
- Includes retry logic for speech failures

### `gemini.py`
- Integrates Gemini API
- Performs **only intent classification**
- Returns `job` or `scheme`

### `tools.py`
- Contains rule-based eligibility logic
- **Jobs Tool**
  - Filters government jobs by education, department, and location
  - Suggests other locations/departments if needed
- **Schemes Tool**
  - Determines eligibility using age, education, and gender

### `memory.py`
- Stores user information across turns
- Enables multi-step conversations


##  Demo Video
A live demonstration showcasing:
- Voice-based interaction in a native Indian language
- Agent reasoning and planning
- Tool usage for eligibility checking
- Conversation memory across turns
- Error handling and recovery

 **Demo Link:**  
<https://drive.google.com/file/d/1E_rHVWab9QhI9xmBQXQnOZcl40H8y7tP/view?usp=sharing>
