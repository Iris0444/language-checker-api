from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/check-language")
async def check_language(input: TextInput):
    text = input.text
    violations = []

    if "不是" in text and "而是" in text:
        violations.append({
            "type": "structure",
            "message": "出現『先否定再肯定』句型，請避免使用。"
        })

    if any(word in text for word in ["極度", "無比", "又", "還", "並且"]):
        violations.append({
            "type": "style",
            "message": "出現誇飾或堆疊詞，建議簡化語氣。"
        })

    suggestion = "語言風格檢查完畢。"
    if violations:
        suggestion = "建議根據提示調整語句風格。"

    return {
        "violations": violations,
        "suggestion": suggestion
    }
