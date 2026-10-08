from app.core.guardrails import validate_question


def test_validate_question():
    assert validate_question("What is this document about?") == "What is this document about?"
