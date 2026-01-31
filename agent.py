from google import genai
from config import API_KEY, MODEL_NAME

class TeluguAgent:
    def __init__(self, memory):
        self.memory = memory

        # ✅ NEW WAY: Create client
        self.client = genai.Client(api_key=API_KEY)

        # Tool definitions
        self.tools = [
            {
                "function_declarations": [
                    {
                        "name": "check_jobs",
                        "description": "Check job eligibility",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "age": {"type": "integer"},
                                "education": {"type": "string"},
                                "gender": {"type": "string"},
                            },
                            "required": ["age", "education", "gender"]
                        }
                    },
                    {
                        "name": "check_schemes",
                        "description": "Check scheme eligibility",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "age": {"type": "integer"},
                                "education": {"type": "string"},
                                "gender": {"type": "string"},
                            },
                            "required": ["age", "education", "gender"]
                        }
                    }
                ]
            }
        ]

    def think(self, user_message):
        prompt = f"""
మీరు ఒక తెలుగు మాట్లాడే ప్రభుత్వ సేవా ఏజెంట్.

మీ పని:
- వినియోగదారుడి తెలుగు వాక్యాన్ని అర్థం చేసుకోవాలి
- అవసరమైన వివరాలు మెమరీలో నింపాలి
- విరుద్ధ సమాచారాన్ని గుర్తించాలి
- తదుపరి చర్య నిర్ణయించాలి

ప్రస్తుత మెమరీ: {self.memory.get()}
వినియోగదారు చెప్పింది: {user_message}

కేవలం ఈ JSON మాత్రమే ఇవ్వాలి:
{{
  "next_action": "ask" | "tool" | "final",
  "field": "",
  "question": "",
  "tool_name": "",
  "final_answer": ""
}}
"""

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            tools=self.tools
        )

        return response.text
