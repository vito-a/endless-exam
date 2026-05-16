# ai900_data_basic.py - AI-900 Fundamentals (Basic Edition - 77 Questions)

EXAM_TAG = "ai900"

EXAM_TITLE = "AI-900: Microsoft Azure AI Fundamentals - BASIC EDITION"

PRACTICE_DATA = {

    "Section 1: AI Workloads & Considerations": [
        {"q": "What is an Artificial Intelligence (AI) workload?", "options": ["A physical server", "A task or process that uses AI techniques to solve problems", "A database query", "A networking protocol"], "answer": 1, "explanation": "AI workloads include tasks like prediction, classification, and natural language processing."},
        {"q": "Which of the following is an example of an AI workload?", "options": ["File storage", "Image classification", "Disk partitioning", "Network routing"], "answer": 1, "explanation": "Image classification is a common AI workload using machine learning."},
        {"q": "What is responsible AI primarily concerned with?", "options": ["Hardware costs", "Ethical and fair use of AI systems", "Programming languages", "Database performance"], "answer": 1, "explanation": "Responsible AI focuses on fairness, reliability, privacy, and transparency."},
        {"q": "Which principle ensures AI systems treat all users fairly?", "options": ["Reliability", "Fairness", "Privacy", "Scalability"], "answer": 1, "explanation": "Fairness ensures no bias or discrimination in AI outcomes."},
        {"q": "What does 'transparency' in AI mean?", "options": ["Encrypting data", "Making AI decisions understandable", "Increasing speed", "Reducing costs"], "answer": 1, "explanation": "Transparency ensures users understand how AI systems make decisions."},
        {"q": "Which AI workload involves understanding spoken language?", "options": ["Computer vision", "Speech recognition", "Regression", "Clustering"], "answer": 1, "explanation": "Speech recognition converts spoken words into text."},
        {"q": "Which workload involves analyzing images?", "options": ["NLP", "Computer vision", "Regression", "Forecasting"], "answer": 1, "explanation": "Computer vision processes and interprets visual data."}
    ],

    "Section 2: Machine Learning Basics": [
        {"q": "What is machine learning?", "options": ["Manual programming", "Systems that learn from data", "Database indexing", "Encryption"], "answer": 1, "explanation": "Machine learning allows systems to learn patterns from data."},
        {"q": "Which type of ML uses labeled data?", "options": ["Unsupervised", "Supervised", "Reinforcement", "Clustering"], "answer": 1, "explanation": "Supervised learning uses labeled datasets."},
        {"q": "Which type of ML finds patterns without labels?", "options": ["Supervised", "Unsupervised", "Regression", "Classification"], "answer": 1, "explanation": "Unsupervised learning identifies hidden patterns."},
        {"q": "What is a model in ML?", "options": ["Database", "Mathematical representation learned from data", "Hardware", "API"], "answer": 1, "explanation": "A model is trained to make predictions."},
        {"q": "What is training data?", "options": ["Final output", "Data used to teach the model", "Logs", "Backups"], "answer": 1, "explanation": "Training data is used to build the model."},
        {"q": "Which task predicts numeric values?", "options": ["Classification", "Regression", "Clustering", "NLP"], "answer": 1, "explanation": "Regression predicts continuous values."},
        {"q": "Which task assigns categories?", "options": ["Regression", "Classification", "Clustering", "Forecasting"], "answer": 1, "explanation": "Classification assigns labels."}
    ],

    "Section 3: Azure Machine Learning": [
        {"q": "What is Azure Machine Learning?", "options": ["Database service", "Cloud ML platform", "Networking tool", "Storage system"], "answer": 1, "explanation": "Azure ML is used to build and deploy ML models."},
        {"q": "What is Azure ML Studio?", "options": ["IDE", "Web-based ML interface", "Database", "Firewall"], "answer": 1, "explanation": "It provides UI for building ML solutions."},
        {"q": "What is AutoML?", "options": ["Manual coding", "Automated model selection", "Data storage", "Monitoring"], "answer": 1, "explanation": "AutoML automates ML pipeline tasks."},
        {"q": "What is a dataset?", "options": ["Code", "Collection of data", "Model", "API"], "answer": 1, "explanation": "Datasets are used for training/testing."},
        {"q": "What is an experiment?", "options": ["Test run of ML workflow", "Database query", "Backup process", "Deployment"], "answer": 0, "explanation": "Experiments track ML runs."},
        {"q": "What is a pipeline?", "options": ["Network route", "ML workflow steps", "Storage unit", "Security rule"], "answer": 1, "explanation": "Pipelines automate ML processes."},
        {"q": "What is model deployment?", "options": ["Deleting model", "Making model available for use", "Training model", "Testing model"], "answer": 1, "explanation": "Deployment exposes model for predictions."}
    ],

    "Section 4: Computer Vision": [
        {"q": "What is computer vision?", "options": ["Audio processing", "Image analysis", "Text processing", "Networking"], "answer": 1, "explanation": "Computer vision extracts insights from images."},
        {"q": "What is image classification?", "options": ["Detect objects", "Assign label to image", "Translate text", "Speech processing"], "answer": 1, "explanation": "Classification labels entire image."},
        {"q": "What is object detection?", "options": ["Label image", "Locate objects", "Translate text", "Cluster data"], "answer": 1, "explanation": "Detects objects and their positions."},
        {"q": "Which Azure service supports vision?", "options": ["Azure AI Vision", "Azure SQL", "Azure VM", "Azure DNS"], "answer": 0, "explanation": "Azure AI Vision provides vision capabilities."},
        {"q": "What is OCR?", "options": ["Audio recognition", "Text extraction from images", "Prediction", "Clustering"], "answer": 1, "explanation": "OCR reads text from images."},
        {"q": "What is face detection?", "options": ["Identify emotions", "Locate faces", "Translate", "Predict values"], "answer": 1, "explanation": "Face detection finds faces."},
        {"q": "What is image tagging?", "options": ["Manual tagging", "Assigning keywords automatically", "Deleting images", "Encrypting images"], "answer": 1, "explanation": "Tagging labels image content."}
    ],

    "Section 5: Natural Language Processing": [
        {"q": "What is NLP?", "options": ["Image processing", "Language understanding", "Networking", "Storage"], "answer": 1, "explanation": "NLP works with human language."},
        {"q": "What is sentiment analysis?", "options": ["Translate text", "Detect emotions in text", "Speech recognition", "Clustering"], "answer": 1, "explanation": "Sentiment detects positive/negative tone."},
        {"q": "What is entity recognition?", "options": ["Find objects", "Extract names/entities", "Translate text", "Predict numbers"], "answer": 1, "explanation": "NER identifies entities like names."},
        {"q": "What is translation?", "options": ["Convert speech", "Convert text between languages", "Detect objects", "Cluster data"], "answer": 1, "explanation": "Translation converts languages."},
        {"q": "Which service supports NLP?", "options": ["Azure AI Language", "Azure VM", "Azure DNS", "Azure Firewall"], "answer": 0, "explanation": "Azure AI Language provides NLP capabilities."},
        {"q": "What is summarization?", "options": ["Expand text", "Shorten text", "Translate text", "Encrypt text"], "answer": 1, "explanation": "Summarization condenses text."},
        {"q": "What is key phrase extraction?", "options": ["Delete text", "Identify important phrases", "Translate", "Predict"], "answer": 1, "explanation": "Extracts key topics from text."}
    ],

    "Section 6: Speech AI": [
        {"q": "What is speech recognition?", "options": ["Text to speech", "Speech to text", "Image detection", "Clustering"], "answer": 1, "explanation": "Converts spoken words to text."},
        {"q": "What is text-to-speech?", "options": ["Speech to text", "Text to audio", "Image analysis", "Prediction"], "answer": 1, "explanation": "Converts text into spoken audio."},
        {"q": "What is speech translation?", "options": ["Text translation", "Speech to speech translation", "Image tagging", "Clustering"], "answer": 1, "explanation": "Translates spoken language."},
        {"q": "Which service provides speech AI?", "options": ["Azure AI Speech", "Azure SQL", "Azure VM", "Azure DNS"], "answer": 0, "explanation": "Azure AI Speech handles speech tasks."},
        {"q": "What is voice recognition?", "options": ["Identify speaker", "Translate speech", "Detect objects", "Cluster data"], "answer": 0, "explanation": "Recognizes speaker identity."},
        {"q": "What is speech synthesis?", "options": ["Speech to text", "Generate speech", "Translate", "Predict"], "answer": 1, "explanation": "Creates human-like audio."},
        {"q": "What is real-time transcription?", "options": ["Batch processing", "Live speech to text", "Image tagging", "Clustering"], "answer": 1, "explanation": "Converts speech instantly."}
    ],

    "Section 7: Generative AI Basics": [
        {"q": "What is generative AI?", "options": ["Data storage", "Creates new content", "Networking", "Security"], "answer": 1, "explanation": "Generative AI creates text, images, etc."},
        {"q": "What is a prompt?", "options": ["Output", "Input to model", "Database", "API"], "answer": 1, "explanation": "Prompt guides AI response."},
        {"q": "What is Azure OpenAI?", "options": ["Database", "AI service for LLMs", "Firewall", "Storage"], "answer": 1, "explanation": "Provides access to advanced models."},
        {"q": "What is a large language model?", "options": ["Small dataset", "Model trained on large text data", "Image model", "Audio model"], "answer": 1, "explanation": "LLMs understand/generate text."},
        {"q": "What is hallucination?", "options": ["Correct answer", "Incorrect AI output", "Fast response", "Encryption"], "answer": 1, "explanation": "AI may generate incorrect info."},
        {"q": "What is prompt engineering?", "options": ["Hardware tuning", "Designing inputs", "Networking", "Security"], "answer": 1, "explanation": "Improves AI responses."},
        {"q": "What is content filtering?", "options": ["Delete data", "Block harmful outputs", "Encrypt data", "Store data"], "answer": 1, "explanation": "Ensures safe AI usage."}
    ],

    "Section 8: Responsible AI": [
        {"q": "What does fairness mean?", "options": ["Fast results", "Equal treatment", "Cheap cost", "High accuracy"], "answer": 1, "explanation": "Fairness avoids bias."},
        {"q": "What does reliability mean?", "options": ["Consistent performance", "Low cost", "Fast speed", "High storage"], "answer": 0, "explanation": "Reliable AI performs consistently."},
        {"q": "What does privacy mean?", "options": ["Open data", "Protect user data", "Delete data", "Share data"], "answer": 1, "explanation": "Privacy safeguards personal info."},
        {"q": "What does inclusiveness mean?", "options": ["Exclude users", "Design for all users", "Reduce cost", "Increase speed"], "answer": 1, "explanation": "Inclusive AI serves everyone."},
        {"q": "What does accountability mean?", "options": ["No responsibility", "Humans responsible for AI", "Automation", "Speed"], "answer": 1, "explanation": "Humans must oversee AI."},
        {"q": "What does transparency mean?", "options": ["Hidden logic", "Explainable AI", "Fast AI", "Cheap AI"], "answer": 1, "explanation": "Transparency explains decisions."},
        {"q": "What does security mean?", "options": ["Open systems", "Protect AI systems", "Delete models", "Reduce cost"], "answer": 1, "explanation": "Security protects AI systems."}
    ],

    "Section 9: AI Services": [
        {"q": "What are Azure AI services?", "options": ["Hardware", "Prebuilt AI APIs", "Databases", "Networks"], "answer": 1, "explanation": "They provide ready-to-use AI capabilities."},
        {"q": "What is REST API?", "options": ["Database", "Web service interface", "Hardware", "Storage"], "answer": 1, "explanation": "REST APIs enable service interaction."},
        {"q": "What is SDK?", "options": ["Hardware", "Development tools", "Database", "Network"], "answer": 1, "explanation": "SDK simplifies development."},
        {"q": "What is endpoint?", "options": ["URL for service", "Database", "Server rack", "Firewall"], "answer": 0, "explanation": "Endpoint is access point."},
        {"q": "What is authentication?", "options": ["Verify identity", "Store data", "Delete data", "Encrypt data"], "answer": 0, "explanation": "Authentication confirms identity."},
        {"q": "What is key-based access?", "options": ["Password", "Access via key", "Database", "Firewall"], "answer": 1, "explanation": "Keys authenticate API usage."},
        {"q": "What is pricing tier?", "options": ["Cost level", "Speed", "Security", "Storage"], "answer": 0, "explanation": "Defines service cost/limits."}
    ],

    "Section 10: Knowledge Mining": [
        {"q": "What is knowledge mining?", "options": ["Delete data", "Extract insights from data", "Store data", "Encrypt data"], "answer": 1, "explanation": "Finds insights from large datasets."},
        {"q": "What is Azure AI Search?", "options": ["Database", "Search service", "Firewall", "Storage"], "answer": 1, "explanation": "Provides indexing/search."},
        {"q": "What is indexing?", "options": ["Delete data", "Organize data", "Encrypt data", "Store data"], "answer": 1, "explanation": "Indexing enables fast search."},
        {"q": "What is enrichment?", "options": ["Delete data", "Add AI insights", "Encrypt data", "Store data"], "answer": 1, "explanation": "Enhances data with AI."},
        {"q": "What is skillset?", "options": ["Hardware", "AI processing steps", "Database", "Network"], "answer": 1, "explanation": "Defines enrichment pipeline."},
        {"q": "What is query?", "options": ["Search request", "Delete request", "Store request", "Encrypt request"], "answer": 0, "explanation": "Query retrieves results."},
        {"q": "What is semantic search?", "options": ["Keyword only", "Meaning-based search", "Delete data", "Encrypt data"], "answer": 1, "explanation": "Uses AI to understand intent."}
    ],

    "Section 11: Conversational AI": [
        {"q": "What is conversational AI?", "options": ["Storage", "Chatbots/virtual agents", "Networking", "Security"], "answer": 1, "explanation": "Conversational AI enables chat experiences."},
        {"q": "What is a bot?", "options": ["Human", "Automated agent", "Database", "Firewall"], "answer": 1, "explanation": "Bots simulate conversation."},
        {"q": "What is Azure Bot Service?", "options": ["Database", "Bot platform", "Storage", "Network"], "answer": 1, "explanation": "Service to build bots."},
        {"q": "What is intent?", "options": ["User goal", "Database", "Model", "API"], "answer": 0, "explanation": "Intent is user purpose."},
        {"q": "What is utterance?", "options": ["User input", "Output", "Database", "API"], "answer": 0, "explanation": "Utterance is what user says."},
        {"q": "What is dialog flow?", "options": ["Conversation structure", "Database", "Storage", "Network"], "answer": 0, "explanation": "Defines conversation steps."},
        {"q": "What is channel?", "options": ["Communication platform", "Database", "Firewall", "Storage"], "answer": 0, "explanation": "Channel is where bot interacts (Teams, web, etc.)."}
    ]
}