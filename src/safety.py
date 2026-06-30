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
    "pressure",
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
immediate danger, please call Nepal Police at 100 now, contact a nearby hospital
emergency department, or ask someone close to take you there immediately.

In Nepal, you can also call the Suicide Prevention Helpline at 1166 for
crisis support.

You do not have to handle this alone. If possible, move away from anything you
could use to hurt yourself, and call or sit with a trusted person nearby right
now.
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
