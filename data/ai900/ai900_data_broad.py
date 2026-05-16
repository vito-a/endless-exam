# ai900_data_broad.py - AI-900 Fundamentals (Broad Edition - 77 Questions)

EXAM_TAG = "ai900"

EXAM_TITLE = "AI-900: Microsoft Azure AI Fundamentals - BROAD EDITION"

PRACTICE_DATA = {

    "Section 1: Fundamental AI Concepts": [
        {"q": "Which statement BEST describes Artificial Intelligence (AI)?", "options": ["A replacement for all human decision making", "Software that imitates human cognitive abilities", "A type of database technology", "A networking protocol"], "answer": 1, "explanation": "AI systems imitate human capabilities such as learning, reasoning, and perception."},
        {"q": "Which AI workload is used to predict future sales amounts?", "options": ["Classification", "Regression", "Computer vision", "OCR"], "answer": 1, "explanation": "Regression predicts continuous numeric values."},
        {"q": "Which workload is MOST appropriate for identifying spam emails?", "options": ["Classification", "Clustering", "Segmentation", "OCR"], "answer": 0, "explanation": "Spam filtering is a classification problem."},
        {"q": "What is the primary purpose of Responsible AI?", "options": ["Reduce storage costs", "Ensure ethical and trustworthy AI systems", "Increase internet speed", "Replace software developers"], "answer": 1, "explanation": "Responsible AI ensures systems are fair, transparent, and reliable."},
        {"q": "Which Responsible AI principle focuses on protecting user information?", "options": ["Inclusiveness", "Privacy and security", "Transparency", "Fairness"], "answer": 1, "explanation": "Privacy and security protect sensitive user data."},
        {"q": "A chatbot that answers employee HR questions is an example of which AI workload?", "options": ["Computer vision", "Conversational AI", "Forecasting", "Object detection"], "answer": 1, "explanation": "Chatbots are conversational AI solutions."},
        {"q": "Which AI workload is designed to detect unusual patterns in data?", "options": ["Translation", "Anomaly detection", "OCR", "Regression"], "answer": 1, "explanation": "Anomaly detection identifies abnormal behavior or outliers."}
    ],

    "Section 2: Machine Learning Foundations": [
        {"q": "What is machine learning?", "options": ["Manual database tuning", "Systems learning patterns from data", "A networking technology", "An encryption method"], "answer": 1, "explanation": "Machine learning enables systems to learn from data."},
        {"q": "Which type of machine learning requires labeled training data?", "options": ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Clustering"], "answer": 0, "explanation": "Supervised learning uses labeled examples."},
        {"q": "Which machine learning approach groups similar items together?", "options": ["Classification", "Regression", "Clustering", "Forecasting"], "answer": 2, "explanation": "Clustering groups similar data without labels."},
        {"q": "What is overfitting?", "options": ["A model generalizes well", "A model memorizes training data", "A model encrypts data", "A model reduces latency"], "answer": 1, "explanation": "Overfitting reduces performance on new data."},
        {"q": "Which metric is commonly used to evaluate classification models?", "options": ["Accuracy", "RMSE", "Variance", "Latency"], "answer": 0, "explanation": "Accuracy measures correct predictions."},
        {"q": "Which scenario BEST fits reinforcement learning?", "options": ["Predicting sales revenue", "Training a game-playing AI agent", "Extracting text from invoices", "Detecting sentiment"], "answer": 1, "explanation": "Reinforcement learning uses rewards and penalties."},
        {"q": "What is a feature in a machine learning model?", "options": ["The predicted output", "An input variable", "A deployment endpoint", "A data backup"], "answer": 1, "explanation": "Features are the input attributes used for prediction."}
    ],

    "Section 3: Azure Machine Learning Services": [
        {"q": "What is Azure Machine Learning primarily used for?", "options": ["Managing databases", "Building and deploying ML models", "Hosting websites", "Configuring networks"], "answer": 1, "explanation": "Azure ML is Microsoft's cloud platform for machine learning."},
        {"q": "Which Azure ML capability automatically tests multiple algorithms?", "options": ["Pipelines", "AutoML", "Designer", "Azure Monitor"], "answer": 1, "explanation": "AutoML automates model selection and tuning."},
        {"q": "Which Azure ML feature provides a drag-and-drop interface?", "options": ["Designer", "CLI", "PowerShell", "REST"], "answer": 0, "explanation": "Designer provides low-code model development."},
        {"q": "What is the purpose of a compute cluster in Azure ML?", "options": ["Store images", "Run scalable training jobs", "Provide DNS resolution", "Manage APIs"], "answer": 1, "explanation": "Compute clusters execute machine learning workloads."},
        {"q": "Which deployment type is optimized for low-latency predictions?", "options": ["Batch endpoint", "Real-time endpoint", "Offline endpoint", "Static dataset"], "answer": 1, "explanation": "Real-time endpoints serve immediate predictions."},
        {"q": "What is the role of a pipeline in Azure ML?", "options": ["Encrypt data", "Automate ML workflows", "Manage firewalls", "Host virtual machines"], "answer": 1, "explanation": "Pipelines automate repeatable ML processes."},
        {"q": "What is the purpose of model inference?", "options": ["Train a model", "Generate predictions using a model", "Delete training data", "Create databases"], "answer": 1, "explanation": "Inference uses trained models for predictions."}
    ],

    "Section 4: Computer Vision Solutions": [
        {"q": "Which Azure AI capability extracts text from scanned documents?", "options": ["OCR", "Speech synthesis", "Regression", "Clustering"], "answer": 0, "explanation": "OCR extracts text from images."},
        {"q": "What is object detection?", "options": ["Predicting numbers", "Identifying and locating objects in images", "Translating speech", "Grouping customers"], "answer": 1, "explanation": "Object detection identifies object types and positions."},
        {"q": "Which Azure service provides image analysis features?", "options": ["Azure AI Vision", "Azure SQL Database", "Azure Functions", "Azure Firewall"], "answer": 0, "explanation": "Azure AI Vision supports computer vision tasks."},
        {"q": "What is image classification?", "options": ["Locating objects", "Assigning labels to images", "Converting speech to text", "Summarizing text"], "answer": 1, "explanation": "Classification assigns categories to images."},
        {"q": "What is face detection used for?", "options": ["Finding faces in images", "Forecasting sales", "Detecting sentiment", "Clustering customers"], "answer": 0, "explanation": "Face detection locates faces within images."},
        {"q": "What is image captioning?", "options": ["Encrypting images", "Generating text descriptions for images", "Deleting images", "Scaling databases"], "answer": 1, "explanation": "Captioning creates natural language descriptions."},
        {"q": "What is a bounding box in computer vision?", "options": ["A storage account", "A rectangle identifying object location", "A database index", "A network gateway"], "answer": 1, "explanation": "Bounding boxes identify detected object positions."}
    ],

    "Section 5: Natural Language Processing": [
        {"q": "Which Azure AI service supports sentiment analysis?", "options": ["Azure AI Language", "Azure AI Vision", "Azure DNS", "Azure Firewall"], "answer": 0, "explanation": "Azure AI Language provides NLP features."},
        {"q": "What is sentiment analysis used for?", "options": ["Identifying emotions in text", "Extracting images", "Generating predictions", "Managing networks"], "answer": 0, "explanation": "Sentiment analysis detects positive, neutral, or negative tone."},
        {"q": "Which NLP capability extracts names of people and organizations?", "options": ["Translation", "Entity recognition", "Regression", "OCR"], "answer": 1, "explanation": "NER identifies entities in text."},
        {"q": "What is language detection?", "options": ["Summarizing text", "Identifying the language of text", "Translating speech", "Detecting objects"], "answer": 1, "explanation": "Language detection determines the source language."},
        {"q": "Which service translates text between languages?", "options": ["Translator", "Speech", "Vision", "Bot"], "answer": 0, "explanation": "Translator converts text across languages."},
        {"q": "What is key phrase extraction?", "options": ["Encrypting text", "Identifying important terms", "Deleting text", "Creating databases"], "answer": 1, "explanation": "Key phrase extraction identifies important topics."},
        {"q": "What is summarization?", "options": ["Expanding text", "Condensing text into shorter form", "Converting speech", "Clustering"], "answer": 1, "explanation": "Summarization shortens content while preserving meaning."}
    ],

    "Section 6: Speech & Audio AI": [
        {"q": "Which capability converts spoken words into text?", "options": ["Text-to-speech", "Speech-to-text", "OCR", "Segmentation"], "answer": 1, "explanation": "Speech recognition converts audio into text."},
        {"q": "What does text-to-speech accomplish?", "options": ["Generates spoken audio", "Detects emotions", "Classifies images", "Clusters data"], "answer": 0, "explanation": "Text-to-speech synthesizes audio from text."},
        {"q": "Which Azure service supports speech recognition and synthesis?", "options": ["Azure AI Speech", "Azure AI Vision", "Azure AI Search", "Azure Backup"], "answer": 0, "explanation": "Azure AI Speech supports speech workloads."},
        {"q": "What is speaker recognition?", "options": ["Extracting text", "Identifying who is speaking", "Detecting objects", "Generating summaries"], "answer": 1, "explanation": "Speaker recognition verifies or identifies speakers."},
        {"q": "Which capability translates spoken language in real time?", "options": ["Speech translation", "OCR", "Regression", "Clustering"], "answer": 0, "explanation": "Speech translation converts speech between languages."},
        {"q": "What is a neural voice?", "options": ["A physical microphone", "Human-like synthesized speech", "A networking protocol", "A database engine"], "answer": 1, "explanation": "Neural voices sound natural and expressive."},
        {"q": "Which scenario BEST fits batch transcription?", "options": ["Live captions during a meeting", "Processing recorded audio files overnight", "Real-time chatbot interaction", "Detecting fraud"], "answer": 1, "explanation": "Batch transcription processes prerecorded audio."}
    ],

    "Section 7: Generative AI & Azure OpenAI": [
        {"q": "What is generative AI primarily designed to do?", "options": ["Delete databases", "Create new content", "Manage firewalls", "Configure networks"], "answer": 1, "explanation": "Generative AI creates text, images, code, and more."},
        {"q": "Which Azure service provides access to GPT models?", "options": ["Azure OpenAI Service", "Azure Monitor", "Azure Firewall", "Azure SQL"], "answer": 0, "explanation": "Azure OpenAI provides managed access to large language models."},
        {"q": "What is a prompt in generative AI?", "options": ["The AI output", "The input instruction provided to the model", "A storage account", "A firewall rule"], "answer": 1, "explanation": "Prompts guide model behavior and responses."},
        {"q": "What is prompt engineering?", "options": ["Deploying APIs", "Designing prompts to improve results", "Managing databases", "Scaling compute clusters"], "answer": 1, "explanation": "Prompt engineering optimizes AI outputs."},
        {"q": "What is hallucination in generative AI?", "options": ["Correct predictions", "Plausible but incorrect information", "Improved latency", "Faster training"], "answer": 1, "explanation": "Hallucinations are inaccurate generated responses."},
        {"q": "What does the temperature parameter affect?", "options": ["Encryption level", "Response creativity and randomness", "Database storage", "Image resolution"], "answer": 1, "explanation": "Higher temperature increases randomness."},
        {"q": "Why are content filters important in generative AI systems?", "options": ["Reduce storage costs", "Block harmful or unsafe outputs", "Increase GPU speed", "Improve OCR"], "answer": 1, "explanation": "Content filters promote safe AI usage."}
    ],

    "Section 8: Responsible AI & Governance": [
        {"q": "Which Responsible AI principle focuses on explaining AI decisions?", "options": ["Transparency", "Fairness", "Inclusiveness", "Scalability"], "answer": 0, "explanation": "Transparency improves explainability."},
        {"q": "Which principle ensures AI systems work for diverse populations?", "options": ["Inclusiveness", "Latency", "Storage", "Networking"], "answer": 0, "explanation": "Inclusiveness supports accessibility and diversity."},
        {"q": "Which Microsoft tool helps evaluate fairness in ML models?", "options": ["Fairlearn", "Power BI", "Azure DNS", "Azure Backup"], "answer": 0, "explanation": "Fairlearn helps analyze fairness issues."},
        {"q": "What is model interpretability?", "options": ["Encrypting models", "Understanding how models make decisions", "Scaling databases", "Deleting datasets"], "answer": 1, "explanation": "Interpretability explains model predictions."},
        {"q": "Which principle emphasizes human responsibility for AI outcomes?", "options": ["Accountability", "Latency", "Regression", "OCR"], "answer": 0, "explanation": "Humans remain responsible for AI systems."},
        {"q": "Which issue occurs when AI performs differently across demographic groups?", "options": ["Fairness issue", "Storage issue", "Networking issue", "Compression issue"], "answer": 0, "explanation": "Unequal performance may indicate bias."},
        {"q": "Why is human oversight important in AI systems?", "options": ["Reduce storage", "Monitor and correct harmful outcomes", "Increase token limits", "Improve OCR"], "answer": 1, "explanation": "Human oversight helps reduce harmful decisions."}
    ],

    "Section 9: Azure AI Services & APIs": [
        {"q": "Which interface is commonly used to access Azure AI services?", "options": ["REST API", "FTP", "SMB", "Telnet"], "answer": 0, "explanation": "REST APIs are standard interfaces for AI services."},
        {"q": "What is the purpose of an API key?", "options": ["Translate text", "Authenticate requests", "Train models", "Delete datasets"], "answer": 1, "explanation": "API keys authenticate access to services."},
        {"q": "What is an SDK?", "options": ["A networking device", "A software development toolkit", "A database engine", "A firewall"], "answer": 1, "explanation": "SDKs simplify application development."},
        {"q": "What does an endpoint URL represent?", "options": ["A storage account", "The address of a service", "A training dataset", "A network cable"], "answer": 1, "explanation": "Endpoints specify where requests are sent."},
        {"q": "What is throttling?", "options": ["Increasing storage", "Limiting API requests", "Compressing images", "Translating text"], "answer": 1, "explanation": "Throttling prevents excessive usage."},
        {"q": "What is latency?", "options": ["Response delay", "Encryption strength", "Storage capacity", "GPU size"], "answer": 0, "explanation": "Latency measures delay in responses."},
        {"q": "What cloud characteristic allows AI services to handle increased demand?", "options": ["Scalability", "OCR", "Translation", "Segmentation"], "answer": 0, "explanation": "Scalability adjusts resources dynamically."}
    ],

    "Section 10: Knowledge Mining & AI Search": [
        {"q": "What is knowledge mining?", "options": ["Deleting files", "Extracting insights from large datasets", "Replacing databases", "Compressing backups"], "answer": 1, "explanation": "Knowledge mining uncovers valuable information from data."},
        {"q": "Which Azure service enables AI-powered search experiences?", "options": ["Azure AI Search", "Azure DNS", "Azure Firewall", "Azure Backup"], "answer": 0, "explanation": "Azure AI Search provides indexing and search capabilities."},
        {"q": "What is the role of an indexer in Azure AI Search?", "options": ["Train ML models", "Import and process data", "Encrypt databases", "Scale virtual machines"], "answer": 1, "explanation": "Indexers load data into search indexes."},
        {"q": "What is a skillset in Azure AI Search?", "options": ["A firewall rule", "A collection of AI enrichment steps", "A compute cluster", "A network gateway"], "answer": 1, "explanation": "Skillsets define enrichment workflows."},
        {"q": "What does semantic search improve?", "options": ["GPU performance", "Meaning-based search relevance", "Storage replication", "Network bandwidth"], "answer": 1, "explanation": "Semantic search understands context and intent."},
        {"q": "Which cognitive skill extracts printed text from images?", "options": ["OCR skill", "Regression skill", "Forecasting skill", "Clustering skill"], "answer": 0, "explanation": "OCR extracts text during enrichment."},
        {"q": "Which scenario BEST demonstrates knowledge mining?", "options": ["Analyzing millions of legal documents for insights", "Hosting websites", "Creating virtual networks", "Managing storage accounts"], "answer": 0, "explanation": "Knowledge mining extracts insights from large unstructured data collections."}
    ],

    "Section 11: Conversational AI & Bots": [
        {"q": "Which Azure service helps developers build conversational bots?", "options": ["Azure Bot Service", "Azure Kubernetes Service", "Azure Firewall", "Azure Backup"], "answer": 0, "explanation": "Azure Bot Service supports chatbot development."},
        {"q": "What is an utterance in conversational AI?", "options": ["A user input", "A model deployment", "A storage container", "A firewall rule"], "answer": 0, "explanation": "An utterance is what the user says or types."},
        {"q": "What is intent detection?", "options": ["Understanding user goals", "Detecting objects", "Predicting revenue", "Managing APIs"], "answer": 0, "explanation": "Intent detection identifies the user's purpose."},
        {"q": "What is dialog management responsible for?", "options": ["Controlling conversation flow", "Encrypting databases", "Scaling GPUs", "Training OCR models"], "answer": 0, "explanation": "Dialog management controls interactions."},
        {"q": "What is a Q&A bot?", "options": ["A forecasting system", "A chatbot answering FAQs", "An image classifier", "A fraud detector"], "answer": 1, "explanation": "Q&A bots provide answers from knowledge bases."},
        {"q": "Which feature allows bots to connect to Microsoft Teams and web apps?", "options": ["Channel integration", "Object detection", "OCR", "Segmentation"], "answer": 0, "explanation": "Channels connect bots to communication platforms."},
        {"q": "What are adaptive dialogs used for?", "options": ["Static workflows", "Dynamic conversation handling", "Database tuning", "Image processing"], "answer": 1, "explanation": "Adaptive dialogs allow flexible conversations."}
    ]
}