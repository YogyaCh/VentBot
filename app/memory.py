
session_memory = {}

def update_memory(session_id, user_input):
    session_memory.setdefault(session_id, []).append(user_input)
    session_memory[session_id] = session_memory[session_id][-3:]

def get_context(session_id):
    return " | ".join(session_memory.get(session_id, []))
