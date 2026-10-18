
from dialogue.generator import build_prompt, generate_reply


def test_prompt_contains_user_message_and_emotion():
    prompt = build_prompt("I feel lonely", "sad")

    assert "I feel lonely" in prompt
    assert "sad" in prompt
    assert "Clara's reply:" in prompt


def test_prompt_includes_memories():
    prompt = build_prompt(
        "Who is my friend?",
        "confused",
        memories=["My friend is named Ravi."]
    )

    assert "My friend is named Ravi." in prompt



def test_generate_reply_returns_ai_response(monkeypatch):
    from dialogue import generator

    class FakeResponse:
        text = "Hello! I am Clara."

    class FakeModels:
        def generate_content(self, **kwargs):
            return FakeResponse()

    class FakeClient:
        models = FakeModels()

    class FakeGenAI:
        @staticmethod
        def Client():
            return FakeClient()

    monkeypatch.setattr("google.genai.Client", FakeGenAI.Client)

    result = generator.generate_reply("Hello Clara", "happy")

    assert result == "Hello! I am Clara."

