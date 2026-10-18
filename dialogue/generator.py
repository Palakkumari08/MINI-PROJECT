
def build_prompt(text, emotion, memories=None):
    """Build a supportive response prompt for Clara."""

    memories = memories or []

    if memories:
        memory_context = "\n".join(
            f"- {memory}" for memory in memories
        )
    else:
        memory_context = "No relevant memories available."

    prompt = f"""
You are Clara, a gentle AI companion for people living with dementia.

User's message: {text}
Detected emotion: {emotion}

Relevant personal memories:
{memory_context}

Instructions:
- Be kind, patient, calm, and reassuring.
- Use simple language and short sentences.
- Respond naturally to the user's message and emotion.
- Never argue with, shame, or frighten the user.
- Never invent personal memories or claim certainty about unknown facts.
- Do not diagnose medical conditions.
- If the user seems distressed, respond gently.
- Write a short, supportive reply.

Clara's reply:
""".strip()

    return prompt


def generate_reply(text, emotion, memories=None):
    """Generate clara's reply using gemini"""
    from google import genai

    try:
        client = genai.Client()

        prompt = build_prompt(text, emotion, memories)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
        )

        if response.text:
            return response.text.strip()

    except Exception:
        pass

    return (
        "I'm here with you. "
        "Let's take a moment and try again."
    )

