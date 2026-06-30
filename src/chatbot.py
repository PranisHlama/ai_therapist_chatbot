import requests

from src.prompts import build_prompt
from src.safety import CRISIS_RESPONSE, OUT_OF_DOMAIN_RESPONSE, is_crisis_message, is_domain_message


OLLAMA_URL = "http://localhost:11434/api/generate"


class ChatbotError(Exception):
    """Raised when the chatbot cannot return a model response."""


def ask_ollama(prompt, model_name="mistral"):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": False,
            },
            timeout=100,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise ChatbotError(
            "Could not connect to Ollama. Make sure Ollama is running and the "
            f"'{model_name}' model is installed."
        ) from exc

    data = response.json()
    answer = data.get("response")
    if not answer:
        raise ChatbotError("Ollama returned an empty response.")

    return answer.strip()


def get_bot_reply(user_question, prompt_mode="zero_shot", model_name="mistral"):
    if not user_question.strip():
        return "Please enter a question."

    if is_crisis_message(user_question):
        return CRISIS_RESPONSE

    if not is_domain_message(user_question):
        return OUT_OF_DOMAIN_RESPONSE

    prompt = build_prompt(user_question, prompt_mode)
    return ask_ollama(prompt, model_name=model_name)
