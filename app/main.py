
from fastapi import FastAPI, Request
from app.vent_handler import handle_vent

app = FastAPI()

@app.post("/respond")
async def respond(request: Request):
    data = await request.json()
    user_text = data.get("transcript", "")
    session_id = data.get("session_id", "default")

    reply = await handle_vent(user_text, session_id)
    return {"response": reply}
