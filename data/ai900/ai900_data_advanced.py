# ai900_data_advanced.py - AI-900 Fundamentals (Advanced Edition - 77 Questions)

EXAM_TAG = "ai900"

EXAM_TITLE = "AI-900: Microsoft Azure AI Fundamentals - ADVANCED EDITION"

PRACTICE_DATA = {

    "Section 1: AI Workloads & Responsible AI": [
        {"q": "A retail company wants to automatically categorize product images. Which AI workload should they use?", "options": ["Regression", "Computer vision", "Clustering", "Forecasting"], "answer": 1, "explanation": "Image categorization is a computer vision task."},
        {"q": "A bank uses AI to approve loans but notices bias against certain groups. Which Responsible AI principle is violated?", "options": ["Transparency", "Fairness", "Reliability", "Scalability"], "answer": 1, "explanation": "Bias indicates a fairness issue."},
        {"q": "An AI model provides predictions but cannot explain how it reached them. Which principle is lacking?", "options": ["Privacy", "Transparency", "Inclusiveness", "Security"], "answer": 1, "explanation": "Transparency requires explainability."},
        {"q": "Which workload is best for predicting house prices?", "options": ["Classification", "Regression", "Clustering", "NLP"], "answer": 1, "explanation": "Regression predicts continuous values."},
        {"q": "A chatbot answers customer queries in real time. Which workload is this?", "options": ["Computer vision", "Conversational AI", "Regression", "Clustering"], "answer": 1, "explanation": "Chatbots are conversational AI."},
        {"q": "Which Responsible AI principle ensures systems perform consistently under different conditions?", "options": ["Reliability", "Fairness", "Privacy", "Inclusiveness"], "answer": 0, "explanation": "Reliability ensures consistent performance."},
        {"q": "Which workload identifies unusual patterns in credit card transactions?", "options": ["Classification", "Anomaly detection", "Regression", "Translation"], "answer": 1, "explanation": "Anomaly detection finds unusual behavior."}
    ],

    "Section 2: Machine Learning Concepts": [
        {"q": "A dataset contains labeled images of cats and dogs. Which type of learning is this?", "options": ["Unsupervised", "Supervised", "Reinforcement", "Clustering"], "answer": 1, "explanation": "Labeled data indicates supervised learning."},
        {"q": "Which algorithm groups customers based on purchasing behavior without predefined labels?", "options": ["Regression", "Classification", "Clustering", "Forecasting"], "answer": 2, "explanation": "Clustering is unsupervised grouping."},
        {"q": "What is overfitting?", "options": ["Model performs well on new data", "Model memorizes training data", "Model ignores data", "Model deletes data"], "answer": 1, "explanation": "Overfitting reduces generalization."},
        {"q": "What is a feature in ML?", "options": ["Prediction result", "Input variable", "Model output", "Database field"], "answer": 1, "explanation": "Features are inputs to the model."},
        {"q": "What is training vs inference?", "options": ["Same process", "Training builds model, inference uses it", "Inference builds model", "Training deletes model"], "answer": 1, "explanation": "Training creates model, inference applies it."},
        {"q": "Which metric evaluates classification accuracy?", "options": ["RMSE", "Accuracy", "Mean", "Variance"], "answer": 1, "explanation": "Accuracy measures correct predictions."},
        {"q": "Which scenario uses reinforcement learning?", "options": ["Spam detection", "Game playing agent", "Sales prediction", "Image tagging"], "answer": 1, "explanation": "Reinforcement learning uses rewards/penalties."}
    ],

    "Section 3: Azure Machine Learning": [
        {"q": "A data scientist wants to automate model selection and tuning. Which Azure ML feature should they use?", "options": ["Designer", "AutoML", "Pipelines", "Notebooks"], "answer": 1, "explanation": "AutoML automates model selection."},
        {"q": "Which Azure ML component tracks experiments and metrics?", "options": ["Workspace", "Compute", "Dataset", "Endpoint"], "answer": 0, "explanation": "Workspace manages experiments."},
        {"q": "What is the purpose of compute targets?", "options": ["Store data", "Run training jobs", "Deploy APIs", "Monitor logs"], "answer": 1, "explanation": "Compute executes ML workloads."},
        {"q": "Which tool allows drag-and-drop ML model creation?", "options": ["Azure ML Designer", "CLI", "SDK", "PowerShell"], "answer": 0, "explanation": "Designer is visual tool."},
        {"q": "What is a real-time endpoint?", "options": ["Batch job", "API for predictions", "Database", "Model storage"], "answer": 1, "explanation": "Endpoints serve predictions."},
        {"q": "What is batch inference used for?", "options": ["Real-time predictions", "Large dataset predictions", "Training", "Monitoring"], "answer": 1, "explanation": "Batch processes large data sets."},
        {"q": "Which format is commonly used for model deployment?", "options": ["CSV", "REST API", "PDF", "XML"], "answer": 1, "explanation": "Models are exposed via APIs."}
    ],

    "Section 4: Computer Vision": [
        {"q": "A company wants to detect defective products on a production line. Which task is appropriate?", "options": ["OCR", "Object detection", "Translation", "Clustering"], "answer": 1, "explanation": "Object detection identifies defects."},
        {"q": "Which service extracts printed text from scanned documents?", "options": ["Face API", "OCR", "Speech API", "Translator"], "answer": 1, "explanation": "OCR extracts text."},
        {"q": "What is image segmentation?", "options": ["Label whole image", "Divide image into regions", "Translate image", "Delete image"], "answer": 1, "explanation": "Segmentation identifies regions."},
        {"q": "Which scenario uses face recognition?", "options": ["Detect objects", "Verify identity", "Translate text", "Predict sales"], "answer": 1, "explanation": "Face recognition verifies identity."},
        {"q": "Which Azure service analyzes images?", "options": ["Azure AI Vision", "Azure SQL", "Azure DNS", "Azure Firewall"], "answer": 0, "explanation": "Vision service handles images."},
        {"q": "What is caption generation?", "options": ["Translate speech", "Describe image", "Cluster data", "Encrypt data"], "answer": 1, "explanation": "Captions describe images."},
        {"q": "What is a bounding box?", "options": ["Database", "Rectangle around object", "Encryption", "API"], "answer": 1, "explanation": "Bounding boxes locate objects."}
    ],

    "Section 5: Natural Language Processing": [
        {"q": "A company wants to detect customer sentiment in reviews. Which service should they use?", "options": ["Vision", "Speech", "Language", "Bot"], "answer": 2, "explanation": "Language service handles sentiment."},
        {"q": "What is named entity recognition used for?", "options": ["Translate text", "Extract entities", "Detect images", "Predict values"], "answer": 1, "explanation": "NER extracts entities."},
        {"q": "Which task identifies key topics in text?", "options": ["Translation", "Key phrase extraction", "OCR", "Regression"], "answer": 1, "explanation": "Key phrases highlight topics."},
        {"q": "What is language detection?", "options": ["Translate text", "Identify language", "Summarize text", "Cluster data"], "answer": 1, "explanation": "Detects language automatically."},
        {"q": "What is abstractive summarization?", "options": ["Copy text", "Generate summary", "Translate text", "Delete text"], "answer": 1, "explanation": "Generates new summary text."},
        {"q": "Which API translates text?", "options": ["Translator", "Vision", "Speech", "Search"], "answer": 0, "explanation": "Translator API converts languages."},
        {"q": "What is intent detection?", "options": ["Detect language", "Understand user goal", "Translate text", "Cluster"], "answer": 1, "explanation": "Intent identifies user goal."}
    ],

    "Section 6: Speech AI": [
        {"q": "A call center transcribes calls in real time. Which service is used?", "options": ["Vision", "Speech-to-text", "Translator", "Search"], "answer": 1, "explanation": "Speech-to-text transcribes calls."},
        {"q": "Which feature converts written text into spoken words?", "options": ["Speech recognition", "Text-to-speech", "OCR", "Clustering"], "answer": 1, "explanation": "TTS generates audio."},
        {"q": "Which scenario uses speech translation?", "options": ["Translate text", "Translate spoken language", "Detect objects", "Predict values"], "answer": 1, "explanation": "Speech translation handles spoken input."},
        {"q": "What is speaker recognition?", "options": ["Translate speech", "Identify speaker", "Detect objects", "Cluster"], "answer": 1, "explanation": "Identifies speaker identity."},
        {"q": "Which Azure service supports speech?", "options": ["Speech", "Vision", "SQL", "VM"], "answer": 0, "explanation": "Speech service handles audio tasks."},
        {"q": "What is batch transcription?", "options": ["Real-time", "Process recorded audio", "Translate text", "Cluster"], "answer": 1, "explanation": "Batch processes recordings."},
        {"q": "What is neural voice?", "options": ["Basic audio", "Human-like speech", "Translation", "Prediction"], "answer": 1, "explanation": "Neural voices sound natural."}
    ],

    "Section 7: Generative AI": [
        {"q": "A developer uses prompts to generate code. Which AI type is this?", "options": ["Regression", "Generative AI", "Clustering", "Vision"], "answer": 1, "explanation": "Generative AI creates content."},
        {"q": "What is prompt engineering?", "options": ["Model training", "Designing inputs", "Deploying APIs", "Monitoring"], "answer": 1, "explanation": "Improves outputs via prompts."},
        {"q": "Which issue occurs when AI generates incorrect facts?", "options": ["Latency", "Hallucination", "Overfitting", "Bias"], "answer": 1, "explanation": "Hallucination = incorrect output."},
        {"q": "What is temperature parameter?", "options": ["Speed", "Randomness", "Cost", "Security"], "answer": 1, "explanation": "Controls creativity."},
        {"q": "Which service provides LLM access?", "options": ["Azure OpenAI", "Azure SQL", "Azure DNS", "Azure VM"], "answer": 0, "explanation": "Azure OpenAI provides models."},
        {"q": "What is token?", "options": ["Word unit", "Database", "API", "Model"], "answer": 0, "explanation": "Tokens are text units."},
        {"q": "What is grounding?", "options": ["Ignore data", "Use external data", "Encrypt data", "Delete data"], "answer": 1, "explanation": "Grounding improves accuracy."}
    ],

    "Section 8: Responsible AI Governance": [
        {"q": "Which tool evaluates model fairness?", "options": ["Fairlearn", "SQL", "VM", "DNS"], "answer": 0, "explanation": "Fairlearn assesses fairness."},
        {"q": "Which principle ensures user data is protected?", "options": ["Privacy", "Fairness", "Transparency", "Inclusiveness"], "answer": 0, "explanation": "Privacy protects data."},
        {"q": "Which principle ensures AI works for diverse users?", "options": ["Inclusiveness", "Security", "Reliability", "Speed"], "answer": 0, "explanation": "Inclusiveness supports all users."},
        {"q": "Which principle ensures accountability?", "options": ["Human oversight", "Automation", "Speed", "Cost"], "answer": 0, "explanation": "Humans remain responsible."},
        {"q": "Which risk involves exposing sensitive data?", "options": ["Bias", "Privacy breach", "Latency", "Cost"], "answer": 1, "explanation": "Privacy breach exposes data."},
        {"q": "Which tool explains model predictions?", "options": ["InterpretML", "SQL", "VM", "DNS"], "answer": 0, "explanation": "InterpretML explains models."},
        {"q": "Which principle ensures system safety?", "options": ["Security", "Fairness", "Transparency", "Inclusiveness"], "answer": 0, "explanation": "Security protects systems."}
    ],

    "Section 9: Azure AI Services Integration": [
        {"q": "Which method allows apps to call AI services?", "options": ["REST API", "FTP", "SSH", "RDP"], "answer": 0, "explanation": "REST APIs enable integration."},
        {"q": "What is API key used for?", "options": ["Storage", "Authentication", "Encryption", "Monitoring"], "answer": 1, "explanation": "API keys authenticate access."},
        {"q": "What is SDK advantage?", "options": ["Manual calls", "Simplifies development", "Deletes data", "Encrypts data"], "answer": 1, "explanation": "SDK simplifies coding."},
        {"q": "What is endpoint URL?", "options": ["Database", "Access point", "Firewall", "Storage"], "answer": 1, "explanation": "Endpoint is service URL."},
        {"q": "What is throttling?", "options": ["Speed up", "Limit requests", "Delete data", "Encrypt"], "answer": 1, "explanation": "Limits API usage."},
        {"q": "What is latency?", "options": ["Delay", "Storage", "Cost", "Security"], "answer": 0, "explanation": "Latency is response delay."},
        {"q": "What is scaling?", "options": ["Reduce usage", "Handle load", "Delete data", "Encrypt"], "answer": 1, "explanation": "Scaling handles demand."}
    ],

    "Section 10: Knowledge Mining & Search": [
        {"q": "A company wants to search documents with AI enrichment. Which service?", "options": ["Azure AI Search", "SQL", "VM", "DNS"], "answer": 0, "explanation": "AI Search enables enrichment."},
        {"q": "What is a skillset?", "options": ["Database", "Enrichment pipeline", "Storage", "Firewall"], "answer": 1, "explanation": "Skillset defines AI processing."},
        {"q": "What is indexer?", "options": ["Search engine", "Data ingestion tool", "API", "Database"], "answer": 1, "explanation": "Indexer loads data."},
        {"q": "What is semantic ranking?", "options": ["Keyword match", "Meaning-based ranking", "Delete data", "Encrypt"], "answer": 1, "explanation": "Uses AI understanding."},
        {"q": "What is cognitive skill?", "options": ["Hardware", "AI function", "Database", "Network"], "answer": 1, "explanation": "Skills enrich data."},
        {"q": "What is full-text search?", "options": ["Exact match", "Search all text", "Delete data", "Encrypt"], "answer": 1, "explanation": "Searches entire content."},
        {"q": "What is enrichment pipeline?", "options": ["Storage", "Processing workflow", "Network", "Firewall"], "answer": 1, "explanation": "Pipeline processes data."}
    ],

    "Section 11: Conversational AI": [
        {"q": "A company builds a chatbot for customer support. Which service?", "options": ["Bot Service", "SQL", "VM", "DNS"], "answer": 0, "explanation": "Bot Service enables chatbots."},
        {"q": "What is intent?", "options": ["User goal", "Database", "API", "Model"], "answer": 0, "explanation": "Intent defines purpose."},
        {"q": "What is utterance?", "options": ["User input", "Output", "Database", "API"], "answer": 0, "explanation": "Utterance is user text."},
        {"q": "What is dialog management?", "options": ["Conversation flow", "Database", "Storage", "Network"], "answer": 0, "explanation": "Controls conversation."},
        {"q": "What is channel integration?", "options": ["Storage", "Connect platforms", "Delete data", "Encrypt"], "answer": 1, "explanation": "Bots connect to platforms."},
        {"q": "What is QnA bot?", "options": ["Predict values", "Answer FAQs", "Detect images", "Cluster"], "answer": 1, "explanation": "QnA bots answer questions."},
        {"q": "What is adaptive dialog?", "options": ["Static flow", "Dynamic conversation", "Database", "API"], "answer": 1, "explanation": "Adaptive dialogs adjust dynamically."}
    ]
}
