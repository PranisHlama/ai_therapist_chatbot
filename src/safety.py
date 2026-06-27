CRISIS_KEYWORDS = (
    "suicide",
    "kill myself",
    "end my life",
    "hurt myself",
    "self harm",
    "self-harm",
    "i want to die",
    "i don't want to live",
)

DOMAIN_KEYWORDS = (
    "mental",
    "stress",
    "anxiety",
    "anxious",
    "depression",
    "depressed",
    "sad",
    "lonely",
    "loneliness",
    "panic",
    "worry",
    "worried",
    "sleep",
    "overthinking",
    "emotion",
    "feel",
    "therapy",
    "therapist",
    "relationship",
    "burnout",
    "self care",
    "self-care",
)

CRISIS_RESPONSE = """
I'm really sorry you're feeling this way. If you might hurt yourself or feel in
immediate danger, please contact emergency services now or go to the nearest
emergency room.

If you are in the U.S. or Canada, call or text 988 for the Suicide & Crisis
Lifeline. If you are elsewhere, contact your local emergency number or a trusted
person nearby right now.

You do not have to handle this alone. If possible, move away from anything you
could use to hurt yourself and reach out to someone who can stay with you.
""".strip()

OUT_OF_DOMAIN_RESPONSE = (
    "I can only help with mental-health-related support, such as stress, "
    "anxiety, mood, sleep, relationships, and emotional well-being. Please ask "
    "a question in that area."
)


def is_crisis_message(text):
    normalized = text.lower()
    return any(keyword in normalized for keyword in CRISIS_KEYWORDS)


def is_domain_message(text):
    normalized = text.lower()
    return any(keyword in normalized for keyword in DOMAIN_KEYWORDS)
