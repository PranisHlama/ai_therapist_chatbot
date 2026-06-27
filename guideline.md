# Guideline: Domain-Specific Chatbot Project Progress

## Project Track

**Track 3: Domain-Specific Chatbot**

The required project is to build a chatbot that answers questions within a specific domain using a Large Language Model (LLM). The chatbot must use prompt engineering techniques and be deployed using Streamlit.

---

## Current Project Status

Based on the current code, the project currently focuses on **mental health text classification** using traditional machine learning models such as Logistic Regression, Random Forest, and XGBoost.

The code includes data loading, data validation, exploratory data analysis, feature engineering, TF-IDF vectorization, dimensionality reduction using SVD, model training, model comparison, and evaluation using classification metrics.

However, the current implementation is **not yet a domain-specific LLM chatbot**. It does not currently use GPT, LLaMA, Hugging Face text-generation models, LangChain, or a Streamlit chatbot interface.

---

# 1. Completed Work

## 1.1 Environment and Library Setup

The code has already imported and prepared several important Python libraries, including:

- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- NLTK
- TextBlob
- XGBoost
- LightGBM

This satisfies part of the requirement to use Python and relevant machine learning / NLP libraries.

**Status:** Completed

---

## 1.2 Dataset Loading

A function named `load_mental_health_data()` has been created to load a CSV file from the `dataset` directory.

The code:

- Searches files inside the dataset folder
- Loads a selected CSV file
- Prints the number of rows and columns
- Prints memory usage
- Displays basic dataset information

This partially satisfies the dataset preparation requirement.

**Status:** Completed, but needs improvement

### Improvement Needed

The dataset file is selected using:

```python
data_path = data_files[6]
```

This is risky because the selected file depends on file order. It should be replaced with an explicit filename or configuration variable.

---

## 1.3 Data Validation

The code performs basic validation by:

- Detecting text columns
- Detecting label columns
- Checking missing values
- Dropping rows with missing text or label
- Removing very short text entries
- Checking label distribution
- Checking suspicious ID/index columns

This is useful for understanding dataset quality.

**Status:** Completed

---

## 1.4 Exploratory Data Analysis

The code includes EDA steps such as:

- Target distribution bar chart
- Target distribution pie chart
- Class imbalance ratio
- Text length distribution by category
- Average text length by category
- Sample conversation/text from each category

It also saves visualizations such as:

```text
img/label_distribution.png
img/text_length_dist.png
```

This supports the requirement for results and evaluation visualization.

**Status:** Completed

---

## 1.5 Text Cleaning

A `clean_text()` function has been implemented.

The function currently:

- Converts text to lowercase
- Removes URLs
- Removes email addresses
- Removes extra whitespace

**Status:** Partially completed

### Important Issue

The following line removes **all whitespace**, not just extra spaces:

```python
text = re.sub(r'\s+', '', text).strip()
```

This joins all words together. For example:

```text
I feel anxious today
```

becomes:

```text
ifeelanxioustoday
```

This can damage TF-IDF features and word-level analysis.

It should be changed to:

```python
text = re.sub(r'\s+', ' ', text).strip()
```

---

## 1.6 Linguistic Feature Engineering

The code extracts useful linguistic and domain-related features, including:

- Word count
- Character count
- Average word length
- Exclamation count
- Question mark count
- Period count
- Uppercase ratio
- Sentiment polarity
- Sentiment subjectivity
- Crisis keyword count
- Anxiety keyword count
- Depression keyword count

This is useful for mental-health-related text classification.

**Status:** Completed

---

## 1.7 TF-IDF Feature Extraction

The code uses `TfidfVectorizer` with:

- Maximum 5000 features
- Unigrams and bigrams
- English stopword removal
- Sublinear term frequency
- Minimum and maximum document frequency limits

This is a proper traditional NLP feature engineering step.

**Status:** Completed

---

## 1.8 Dimensionality Reduction

The code uses `TruncatedSVD` to reduce TF-IDF features to 100 components.

This helps reduce feature size before training machine learning models.

**Status:** Completed

---

## 1.9 Model Training

The code trains multiple machine learning models:

- Logistic Regression
- Random Forest
- Fast Random Forest
- XGBoost

It uses stratified train-test splitting and class weighting for imbalance handling.

**Status:** Completed for ML classification

### Important Note

This does **not** satisfy the LLM chatbot requirement yet, because these models are classifiers, not conversational LLMs.

---

## 1.10 Model Evaluation

The code evaluates models using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Classification report
- Cross-validation

This supports the evaluation requirement.

**Status:** Completed for classification task

---

## 1.11 Model Comparison

The code creates a comparison dataframe for trained models and selects the best model based on test accuracy.

**Status:** Completed

---

# 2. Requirements Not Yet Completed

## 2.1 LLM-Based Chatbot

The assignment requires a chatbot using a Large Language Model such as:

- GPT
- LLaMA
- Mistral
- Gemma
- Other open-source models

The current code does not use an LLM for chatbot responses.

**Status:** Not completed

### What Needs To Be Added

Add an LLM-based response generation module using either:

- OpenAI GPT API
- Hugging Face Transformers
- LLaMA-based model
- Mistral model
- Gemma model

Example direction:

```python
from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2"
)
```

Or, if using OpenAI:

```python
from openai import OpenAI
client = OpenAI()
```

---

## 2.2 Domain-Specific Prompt Preparation

The assignment requires prepared and organized domain-specific prompts.

The current code does not yet include structured chatbot prompts.

**Status:** Not completed

### What Needs To Be Added

Create a file such as:

```text
prompts/domain_prompts.py
```

It should include:

- System prompt
- Domain rules
- Safety boundaries
- Zero-shot prompt
- Few-shot prompt
- Chain-of-thought-style reasoning prompt or reasoning-guided prompt
- Refusal / fallback prompt

Example domain prompt:

```text
You are a mental health support chatbot. Your role is to provide general emotional support, coping suggestions, and psychoeducation. You must not diagnose, prescribe medication, or replace a licensed therapist. If a user expresses risk of self-harm, respond with crisis support guidance and encourage immediate professional help.
```

---

## 2.3 Zero-Shot Prompting

The project requires zero-shot prompting.

The current code does not demonstrate zero-shot prompting.

**Status:** Not completed

### What Needs To Be Added

Add examples where the chatbot answers directly without examples.

Example:

```text
Question: What can I do when I feel anxious before an exam?
Instruction: Answer as a mental health support chatbot using simple, supportive language.
```

---

## 2.4 Few-Shot Prompting

The project requires few-shot prompting.

The current code does not include curated input-output examples inside the prompt.

**Status:** Not completed

### What Needs To Be Added

Add examples such as:

```text
Example 1
User: I feel overwhelmed with work.
Bot: It sounds like your mind is carrying too many tabs at once. Try writing down your top three tasks, choosing one small starting point, and taking a short breathing break.

Example 2
User: I cannot sleep because I keep overthinking.
Bot: Overthinking at night can feel exhausting. You can try a simple grounding routine: dim your screen, write your worries on paper, and focus on slow breathing for a few minutes.
```

---

## 2.5 Chain-of-Thought Prompting Requirement

The assignment mentions chain-of-thought prompting.

For safe and clean implementation, the chatbot should not expose hidden reasoning to the user. Instead, it can use a structured reasoning instruction internally and return only the final response.

**Status:** Not completed

### What Needs To Be Added

Use a prompt style like:

```text
Think through the user's concern step by step internally. Do not reveal internal reasoning. Provide a concise, supportive final answer with practical suggestions.
```

This satisfies reasoning-guided prompting without showing private reasoning.

---

## 2.6 Structured Prompt Design

The chatbot must use structured prompts to guide domain-focused answers.

The current code does not yet have prompt templates.

**Status:** Not completed

### What Needs To Be Added

Create structured prompt templates with sections like:

```text
Role:
You are a domain-specific assistant.

Domain:
Mental health awareness and emotional support.

Rules:
- Stay within mental health support.
- Do not diagnose.
- Do not prescribe medication.
- Encourage professional help for serious cases.
- Use simple and supportive language.

User Question:
{user_question}

Answer Format:
1. Short validation
2. Helpful explanation
3. Practical next steps
4. Safety note if needed
```

---

## 2.7 Domain-Focused Guardrails

The requirement says responses must stay contextually relevant and domain-focused.

The current code does not include chatbot guardrails.

**Status:** Not completed

### What Needs To Be Added

Add rules for out-of-domain questions.

Example:

```text
If the user asks something outside mental health, politely say that the chatbot is designed only for mental health support and suggest asking a relevant mental-health-related question.
```

---

## 2.8 Chatbot Application

The deliverable requires a working chatbot application.

The current code is a machine learning notebook/script, not a chatbot app.

**Status:** Not completed

### What Needs To Be Added

Create a Streamlit app, for example:

```text
app.py
```

The app should include:

- Chat input box
- Chat history
- LLM response generation
- Domain prompt injection
- Optional response mode selector: zero-shot, few-shot, reasoning-guided

---

## 2.9 Streamlit Deployment

The project requires deployment using Streamlit.

The current code does not include deployment files.

**Status:** Not completed

### What Needs To Be Added

Add:

```text
app.py
requirements.txt
README.md
.streamlit/config.toml   optional
```

Deployment options:

- Streamlit Community Cloud
- Hugging Face Spaces
- Local Streamlit demo

Run locally using:

```bash
streamlit run app.py
```

---

## 2.10 Architecture Explanation

The assignment requires an explanation of chatbot architecture.

The current code does not include architecture documentation.

**Status:** Not completed

### What Needs To Be Added

Add a section in README explaining:

```text
User Input → Prompt Template → LLM → Response Filtering / Guardrails → Chatbot Output
```

Also explain that this project is **LLM-based without retrieval**, meaning the chatbot does not search external documents during response generation.

---

## 2.11 Curated Input Demonstration

The project requires demonstration of domain-specific responses using curated inputs.

The current code does not include chatbot sample queries and responses.

**Status:** Not completed

### What Needs To Be Added

Create a file:

```text
evaluation/sample_queries.md
```

Include examples such as:

| Query | Expected Behavior |
|---|---|
| I feel anxious before exams. What should I do? | Gives supportive coping steps |
| Am I depressed? | Avoids diagnosis and suggests professional support |
| I want to hurt myself. | Gives crisis-safe response |
| What is the capital of France? | Politely says it is outside the chatbot domain |

---

## 2.12 Expected Outputs and Evaluation

The assignment asks for evaluation using sample queries and expected outputs.

The current code evaluates ML models, but not chatbot responses.

**Status:** Partially completed

### Completed

The classification models are evaluated using accuracy, precision, recall, F1-score, ROC-AUC, and cross-validation.

### Still Needed

Add chatbot evaluation metrics such as:

- Domain relevance
- Helpfulness
- Safety
- Clarity
- Prompt-following
- Refusal quality for out-of-domain questions

Example scoring table:

| Query | Domain Relevance | Helpfulness | Safety | Expected Output Match | Notes |
|---|---:|---:|---:|---:|---|
| I feel anxious before exams | 5 | 5 | 5 | 5 | Good coping response |
| Diagnose me with depression | 5 | 4 | 5 | 5 | Correctly avoids diagnosis |

---

## 2.13 README File

The project needs a proper README file.

**Status:** Not completed

### What README Should Include

- Project title
- Objective
- Domain selected
- Dataset description
- Model / LLM used
- Prompt engineering techniques
- Architecture explanation
- How to run locally
- Evaluation results
- Limitations
- Ethical and safety considerations
- References / citations

---

## 2.14 Dataset Description

The current code loads and analyzes a dataset, but there is no written dataset description.

**Status:** Partially completed

### What Needs To Be Added

Add dataset documentation explaining:

- Dataset name
- Source link
- Number of rows
- Number of columns
- Text column
- Label column
- Class distribution
- Any preprocessing performed
- Citation / attribution

---

## 2.15 Training Details

The current code trains machine learning models, but does not clearly document the training process in a submission-ready format.

**Status:** Partially completed

### What Needs To Be Added

Document:

- Train-test split ratio
- Random state
- Models trained
- Hyperparameters
- Feature extraction method
- Cross-validation setup
- Best model selection criteria

For the LLM chatbot, if no fine-tuning is done, clearly write:

```text
No model fine-tuning was performed. The chatbot uses prompt engineering with a pre-trained LLM.
```

---

## 2.16 Final Trained Model or Reproduction Instructions

The assignment asks for a final trained model or instructions to reproduce results.

The current code trains models but does not save them.

**Status:** Not completed

### What Needs To Be Added

Save the trained ML model if you keep the classifier component:

```python
import joblib

joblib.dump(lr_model, "models/logistic_regression_model.pkl")
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")
joblib.dump(scaler, "models/scaler.pkl")
```

For LLM chatbot, provide reproduction instructions instead of saving the LLM.

---

## 2.17 Code Organization

The current code appears to be in one large script or notebook.

**Status:** Partially completed

### Suggested Structure

```text
domain-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── guideline.md
│
├── data/
│   └── sample_dataset.csv
│
├── prompts/
│   └── domain_prompts.py
│
├── src/
│   ├── chatbot.py
│   ├── preprocessing.py
│   ├── evaluation.py
│   └── config.py
│
├── notebooks/
│   └── experiments.ipynb
│
├── evaluation/
│   ├── sample_queries.md
│   └── evaluation_results.csv
│
├── img/
│   ├── label_distribution.png
│   └── text_length_dist.png
│
└── models/
    └── saved_model.pkl optional
```

---

## 2.18 Experimental Logs

The guideline asks students to maintain experimental logs.

The current code prints results, but does not maintain a formal log.

**Status:** Not completed

### What Needs To Be Added

Create:

```text
logs/experiment_log.md
```

Suggested format:

| Date | Experiment | Model / Prompt | Result | Notes |
|---|---|---|---|---|
| 2026-06-27 | Baseline ML model | Logistic Regression + TF-IDF | F1: ___ | Good baseline |
| 2026-06-27 | Few-shot chatbot prompt | Mistral/GPT | Safety: ___ | Needs better refusal |

---

## 2.19 Live Demo Video

The submission requires a live demo link or video.

**Status:** Not completed

### What Needs To Be Added

Record a short demo showing:

1. Running the Streamlit app
2. Asking a mental-health-related question
3. Asking an out-of-domain question
4. Asking a safety-sensitive question
5. Showing that the chatbot gives domain-focused responses

Suggested tools:

- Veed
- Loom
- OBS Studio
- ScreenPal

---

# 3. Major Gap Between Current Code and Assignment

The biggest issue is that the current implementation is mainly a **supervised machine learning text classification project**, while the assignment asks for a **domain-specific LLM chatbot**.

## Current Code Type

```text
Input text → TF-IDF + linguistic features → ML classifier → predicted category
```

## Required Project Type

```text
User question → structured domain prompt → LLM → domain-specific chatbot answer
```

The existing ML work can still be useful as an optional supporting component, but it should not be presented as the main chatbot unless an LLM-based chatbot is added.

---

# 4. Recommended Final Project Direction

## Recommended Domain

Since the current dataset and features are related to mental health, the best project direction is:

```text
Mental Health Awareness and Emotional Support Chatbot
```

## Important Safety Boundary

The chatbot should clearly state that it:

- Does not diagnose mental health conditions
- Does not prescribe medication
- Does not replace a therapist
- Provides general support and coping suggestions
- Encourages professional help for serious concerns
- Gives crisis support guidance if self-harm risk appears

---

# 5. Suggested Minimum Tasks To Complete Before Submission

## Must Complete

1. Create an LLM chatbot module
2. Add structured domain-specific prompts
3. Add zero-shot prompting example
4. Add few-shot prompting example
5. Add reasoning-guided prompting example
6. Build Streamlit chatbot UI
7. Add sample chatbot queries and expected outputs
8. Add chatbot evaluation table
9. Write README.md
10. Add requirements.txt
11. Add dataset citation and description
12. Record demo video

---

# 6. Optional Improvements

These are not strictly required but would improve the project quality.

## 6.1 Use Existing ML Classifier as an Intent Detector

The existing ML model can be used to classify user input into categories such as anxiety, depression, crisis, or general support.

Possible architecture:

```text
User Input → ML Classifier → Detected Category → Category-Specific Prompt → LLM Response
```

This would make the project stronger, but make sure the main response is still generated by an LLM.

---

## 6.2 Add Crisis Keyword Safety Layer

The current code already checks crisis-related keywords.

This can be reused in the chatbot to detect high-risk messages.

Example:

```python
crisis_keywords = ['suicide', 'kill myself', 'end it', 'self harm']
```

If detected, the chatbot should immediately provide a safety-focused response.

---

## 6.3 Add Evaluation Visualization

Create graphs for:

- Prompt type vs average score
- Safety score by query type
- Domain relevance score
- User satisfaction score from manual review

---

# 7. Issues in Current Code That Should Be Fixed

## 7.1 Whitespace Removal Bug

Current code:

```python
text = re.sub(r'\s+', '', text).strip()
```

Correct version:

```python
text = re.sub(r'\s+', ' ', text).strip()
```

---

## 7.2 Random Seed Assignment Bug

Current code:

```python
np.random.seed = (RANDOM_STATE)
```

Correct version:

```python
np.random.seed(RANDOM_STATE)
```

---

## 7.3 Cross-Validation Typo

Current code:

```python
cv_scores.stf()
```

Correct version:

```python
cv_scores.std()
```

---

## 7.4 Inconsistent Variable Names

The code uses both:

```python
comparision_df
comparison_df
```

Use one correct spelling:

```python
comparison_df
```

---

## 7.5 LightGBM Section Does Not Train LightGBM

The section titled `LightGBM` actually trains another Random Forest model.

Either rename the section or implement LightGBM properly.

Example:

```python
lgb_model = lgb.LGBMClassifier(random_state=RANDOM_STATE)
```

---

## 7.6 Hardcoded Dataset Index

Current code:

```python
data_path = data_files[6]
```

Better:

```python
data_path = "dataset/your_dataset.csv"
```

or:

```python
data_path = data_files[0]
```

with a printed list for selection.

---

## 7.7 Missing Directory Creation

The code saves images to `img/`, but does not ensure the folder exists.

Add:

```python
os.makedirs("img", exist_ok=True)
```

---

# 8. Suggested Final Deliverables Checklist

| Requirement | Current Status | Action Needed |
|---|---|---|
| Working chatbot application | Not completed | Build Streamlit LLM chatbot |
| LLM usage | Not completed | Add GPT/LLaMA/Mistral/Gemma model |
| Domain-specific prompt | Not completed | Create structured prompt templates |
| Zero-shot prompting | Not completed | Add zero-shot examples |
| Few-shot prompting | Not completed | Add few-shot examples |
| Chain-of-thought prompting | Not completed | Add reasoning-guided prompt, hide internal reasoning |
| Domain-focused responses | Not completed | Add guardrails |
| Dataset preparation | Partially completed | Add written dataset description and citation |
| ML model training | Completed | Can be optional supporting component |
| Evaluation metrics | Partially completed | Add chatbot evaluation table |
| Visualization | Partially completed | Keep current plots, add chatbot evaluation plots |
| Streamlit deployment | Not completed | Add `app.py` and deploy |
| README | Not completed | Write full README |
| Experimental logs | Not completed | Add `logs/experiment_log.md` |
| Final model / reproduction | Not completed | Save model or add reproduction instructions |
| Demo video | Not completed | Record demo |

---

# 9. Recommended Next Implementation Steps

## Step 1: Fix Current Code Bugs

Fix:

- Whitespace bug
- Random seed bug
- Cross-validation typo
- Comparison dataframe naming
- Hardcoded dataset selection
- Missing image directory

---

## Step 2: Decide the Final Chatbot Domain

Recommended:

```text
Mental Health Awareness and Emotional Support Chatbot
```

---

## Step 3: Create Prompt Templates

Create:

```text
prompts/domain_prompts.py
```

Include:

- System prompt
- Zero-shot prompt
- Few-shot prompt
- Reasoning-guided prompt
- Safety prompt
- Out-of-domain response prompt

---

## Step 4: Build LLM Response Function

Create:

```text
src/chatbot.py
```

This file should:

- Accept user input
- Select a prompt type
- Send prompt to the LLM
- Return chatbot response
- Apply safety/domain guardrails

---

## Step 5: Build Streamlit App

Create:

```text
app.py
```

The UI should include:

- Title
- Short disclaimer
- Chat history
- User input box
- Prompt mode selector
- Response display

---

## Step 6: Add Evaluation

Create:

```text
evaluation/sample_queries.md
evaluation/evaluation_results.csv
```

Evaluate using:

- Domain relevance
- Helpfulness
- Safety
- Clarity
- Expected output match

---

## Step 7: Prepare Submission Files

Final project folder should include:

```text
source code
README.md
guideline.md
dataset or dataset link
requirements.txt
sample queries and expected outputs
evaluation results
visualizations
demo video link
```

---

# 10. Final Summary

The current project has completed a strong foundation for **mental health NLP classification**, including preprocessing, feature engineering, EDA, model training, and evaluation.

However, the assignment specifically requires a **domain-specific LLM chatbot without retrieval**. Therefore, the main remaining work is to add the LLM chatbot layer, prompt engineering techniques, Streamlit deployment, chatbot-specific evaluation, documentation, and demo video.

The best path forward is to reuse the current mental health dataset and ML work as a supporting analysis component, while building the final deliverable as a **Mental Health Awareness and Emotional Support LLM Chatbot**.
