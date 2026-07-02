# AI Therapist Chatbot Workflow

This document explains the working flow of the `ai_therapist_chatbot` project from user input to final chatbot response.

## 1. Project Purpose

The project is a mental-health awareness and emotional-support chatbot. It helps users with general concerns such as stress, anxiety, sleep issues, loneliness, relationships, burnout, self-care, and emotional well-being.

The chatbot is not a therapist, doctor, emergency service, or diagnostic tool. It does not diagnose conditions, prescribe medication, or replace professional care.

## 2. High-Level Runtime Flow

```text
User opens Streamlit app
        |
        v
User selects prompt style and response source
        |
        v
User enters a mental-health-related question
        |
        v
app.py receives the question
        |
        +----------------------------+
        |                            |
        v                            v
Response source: ollama       Response source: dataset
        |                            |
        v                            v
Safety checks                 TF-IDF similarity search
        |                            |
        v                            v
Prompt construction           Best matching dataset answer
        |
        v
Local Ollama model generation
        |
        v
Assistant response is shown in Streamlit chat
```

## 3. Streamlit App Flow

The main application starts in `app.py`.

1. Streamlit configures the page title, layout, and chat interface.
2. The sidebar lets the user choose:
   - Prompt style: `zero_shot`, `few_shot`, or `reasoning_guided`
   - Response source: `ollama` or `dataset`
3. The app stores chat history in `st.session_state.messages`.
4. When the user submits a question, the question is added to the chat history.
5. The app decides which response path to use:
   - `ollama`: generate a response through the local LLM.
   - `dataset`: retrieve the closest answer from the training dataset.
6. The final answer is displayed in the assistant chat bubble and saved to session history.

## 4. Ollama Response Workflow

The Ollama-based response flow is handled by `src/chatbot.py`.

```text
User question
     |
     v
get_bot_reply()
     |
     v
Check empty input
     |
     v
Check crisis keywords
     |
     v
Check domain keywords
     |
     v
Build selected prompt template
     |
     v
Send prompt to Ollama API
     |
     v
Return model response
```

### Step Details

1. `get_bot_reply()` receives the user question, selected prompt mode, and model name.
2. Empty input returns a simple message asking the user to enter a question.
3. Crisis detection runs before model generation.
4. Out-of-domain detection runs before prompt creation.
5. If the message is safe and in-domain, `build_prompt()` creates the final prompt.
6. `ask_ollama()` sends the prompt to `http://localhost:11434/api/generate`.
7. Ollama returns the generated answer, which is shown in the Streamlit app.

## 5. Safety Workflow

Safety logic is defined in `src/safety.py`.

### Crisis Detection

The chatbot checks for crisis-related keywords such as suicide, self-harm, or wanting to die. If a crisis phrase is detected, the chatbot does not call Ollama. It immediately returns a predefined crisis-safe response with emergency guidance.

```text
Crisis message detected
        |
        v
Return CRISIS_RESPONSE
        |
        v
Skip LLM generation
```

### Domain Filtering

The chatbot checks whether the message is related to mental health or emotional support. If the question is outside the domain, it returns a polite refusal.

```text
Out-of-domain message detected
        |
        v
Return OUT_OF_DOMAIN_RESPONSE
        |
        v
Skip LLM generation
```

This prevents the app from behaving like a general-purpose chatbot.

## 6. Prompt Engineering Workflow

Prompt templates are stored in `src/prompts.py`.

The project supports three prompt styles:

| Prompt Mode | Purpose |
|---|---|
| `zero_shot` | Gives the model rules and the user question without examples. |
| `few_shot` | Provides sample user-assistant examples before the current question. |
| `reasoning_guided` | Asks the model to reason internally and return only a structured final answer. |

The selected prompt mode is passed from the Streamlit sidebar to `get_bot_reply()`, then to `build_prompt()`. The final prompt is sent to the local Ollama model.

## 7. Dataset Response Workflow

The dataset-based response path is handled by `src/dataset_retriever.py`.

```text
Load conversations_training.json
        |
        v
Create DataFrame from input/output pairs
        |
        v
Convert dataset questions to TF-IDF vectors
        |
        v
Convert user question to TF-IDF vector
        |
        v
Calculate cosine similarity
        |
        v
Return output from best matching question
```

If the best similarity score is lower than the minimum threshold, the app returns a fallback message asking the user to rephrase.

This path does not generate a new LLM answer. It retrieves the closest existing answer from the dataset.

## 8. Supporting ML Workflow

The project also includes supporting machine learning work in `src/train_model.py`.

That workflow is separate from the live Streamlit chat response. It supports experimentation and analysis through:

1. Loading mental-health text datasets.
2. Cleaning and validating text data.
3. Creating TF-IDF and extra linguistic features.
4. Training traditional ML classifiers.
5. Evaluating models with metrics such as accuracy, precision, recall, F1-score, ROC-AUC, and cross-validation.
6. Recording experiment observations in `logs/experiment_log.md`.

## 9. Evaluation Workflow

Evaluation cases are listed in `evaluation/sample_queries.md`.

The manual evaluation process is:

1. Start the Streamlit app.
2. Run sample queries through each prompt mode.
3. Check whether responses are:
   - Relevant to the mental-health domain
   - Supportive and clear
   - Practical and concise
   - Safe for crisis, diagnosis, and medication-related questions
   - Correctly refusing unrelated questions
4. Record experiment results in `logs/experiment_log.md`.

## 10. Complete End-to-End Flow

```text
Start Ollama
    |
    v
Run streamlit run app.py
    |
    v
Open chatbot UI
    |
    v
Choose prompt style and response source
    |
    v
Ask a question
    |
    v
If source is dataset:
    Find closest dataset answer with TF-IDF and cosine similarity
    Return matching output or fallback message
    |
    v
If source is ollama:
    Check crisis safety
    Check domain relevance
    Build selected prompt
    Send prompt to local Ollama model
    Return generated answer
    |
    v
Display response in Streamlit chat
    |
    v
Use sample queries and logs to evaluate behavior
```

## 11. Main Files Involved

| File | Role in Workflow |
|---|---|
| `app.py` | Runs the Streamlit chat UI and routes each question to Ollama or dataset mode. |
| `src/chatbot.py` | Applies safety checks, builds prompts, calls Ollama, and returns LLM replies. |
| `src/safety.py` | Detects crisis messages and out-of-domain questions. |
| `src/prompts.py` | Defines prompt templates and builds the selected prompt. |
| `src/dataset_retriever.py` | Finds the closest dataset answer using TF-IDF and cosine similarity. |
| `src/train_model.py` | Runs supporting ML classification experiments. |
| `evaluation/sample_queries.md` | Provides manual test questions and expected behavior. |
| `logs/experiment_log.md` | Records experiments, observations, and next actions. |

