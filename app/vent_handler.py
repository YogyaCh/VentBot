
from app.sentiment import analyze_sentiment
from app.memory import update_memory, get_context
from app.llm import get_llm_response

async def handle_vent(user_input, session_id):
    update_memory(session_id, user_input)
    context = get_context(session_id)
    emotion = analyze_sentiment(user_input)

    prompt = f"You are VentBot. Be warm, empathetic, and reflective.\n\nContext: {context}\nUser: {user_input}\nEmotion: {emotion}\nReply empathetically."
    reply = get_llm_response(prompt)
    return reply
