import os, json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url="https://api.meta.ai/v1", api_key=os.environ["MODEL_API_KEY"])

schema = {
    "type": "object",
    "properties": {
        "abstract_function": {"type": "string"},
        "mechanism": {"type": "string"},
        "constraints": {"type": "array", "items": {"type": "string"}},
        "limitations": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["abstract_function", "mechanism", "constraints", "limitations"],
    "additionalProperties": False,
}

resp = client.chat.completions.create(
    model="muse-spark-1.3",
    messages=[{"role": "user", "content":
        "Abstract this problem into a function, mechanism, constraints and limitations: "
        "Stray dogs on highways are hit by vehicles at night because drivers cannot see them."}],
    response_format={"type": "json_schema",
                     "json_schema": {"name": "abstraction", "strict": True, "schema": schema}},
)
print(json.loads(resp.choices[0].message.content))