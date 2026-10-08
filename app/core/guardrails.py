def validate_question(question: str) -> str:
    if question is None or not str(question).strip():
        raise ValueError("Question cannot be empty")

    cleaned = str(question).strip()

    if len(cleaned) > 5000:
        raise ValueError("Question is too long")

    blocked_phrases = [
        "ignore previous instructions",
        "pretend you are",
        "bypass the system",
    ]

    lowered = cleaned.lower()
    for phrase in blocked_phrases:
        if phrase in lowered:
            raise ValueError("Input contains blocked instructions")

    return cleaned
