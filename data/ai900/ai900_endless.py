# ai900_endless.py - AI Generated Questions

EXAM_TAG = "ai900"

EXAM_TITLE = "AI900: Endless AI Exam"

PRACTICE_DATA = {
    "AI Generated Section 1778869524": [
        {
            "q": "Which of the following principles of Microsoft’s Responsible AI framework specifically requires that the creators and operators of an AI system be able to explain and take responsibility for its impacts?",
            "options": ["Fairness", "Transparency", "Accountability", "Privacy"],
            "answer": 2,
            "explanation": "Accountability in the Responsible AI framework obliges developers and operators to be answerable for the outcomes and impacts of their AI systems, including providing justification for decisions."
        },
        {
            "q": "In the context of model interpretability, what does a SHAP (SHapley Additive exPlanations) value represent for a specific feature in a prediction?",
            "options": [
                "The contribution of the feature to the model's overall loss function",
                "The importance of the feature as measured by tree depth",
                "The marginal effect of that feature on the predicted outcome",
                "The correlation between the feature and the target variable"
            ],
            "answer": 2,
            "explanation": "A SHAP value quantifies how much each feature contributes to the predicted output relative to the expected value, representing its marginal effect on the model's prediction."
        },
        {
            "q": "Which Azure AI service provides a managed, scalable feature store to facilitate the creation, storage, and serving of machine learning features?",
            "options": ["Azure Cognitive Services", "Azure Machine Learning", "Azure Databricks", "Azure Synapse Analytics"],
            "answer": 1,
            "explanation": "Azure Machine Learning includes a managed Feature Store service that enables users to create, version, and serve features at scale for training and inference pipelines."
        },
        {
            "q": "During an automated MLOps pipeline, which stage is primarily responsible for validating the schema and statistical distribution of incoming training data before model training begins?",
            "options": ["Model deployment", "Data validation", "Hyperparameter tuning", "Model interpretability"],
            "answer": 1,
            "explanation": "Data validation is the MLOps stage where schemas, missing values, and statistical distributions are checked to ensure data quality before model training begins."
        },
        {
            "q": "Which metric quantifies the difference in true positive rates between two protected groups, making it useful for assessing fairness in classification models?",
            "options": ["Accuracy", "ROC‑AUC", "Equal Opportunity Difference", "Precision@K"],
            "answer": 2,
            "explanation": "Equal Opportunity Difference measures disparity in true positive rates across demographic groups, highlighting fairness concerns in classification tasks."
        },
        {
            "q": "In a federated learning system, what is the main function of the central aggregation server?",
            "options": [
                "Persistently store the final model weights after each round",
                "Aggregate locally computed model updates from edge devices",
                "Extract and transform features on client machines",
                "Label training examples for each participating device"
            ],
            "answer": 1,
            "explanation": "The central server in federated learning does not train locally but aggregates the model updates (e.g., weight deltas) sent from edge devices to produce a new global model."
        },
        {
            "q": "When dealing with an imbalanced dataset, which technique modifies the training data distribution by synthetically generating samples for the minority class without collecting additional real-world data?",
            "options": ["Random undersampling", "SMOTE oversampling", "Feature scaling", "Principal component analysis"],
            "answer": 1,
            "explanation": "SMOTE oversampling creates synthetic minority class samples by interpolating between existing instances, thereby balancing the dataset without requiring additional real data collection."
        }
    ],

    "AI Generated Section 1778869834": [
        {
            "q": "In the Microsoft Responsible AI framework, which pillar directly addresses the need to prevent an AI system from amplifying historical societal biases that could result in unfair treatment of specific demographic groups?",
            "options": ["Fairness", "Reliability and safety", "Transparency", "Accountability"],
            "answer": 0,
            "explanation": "The Fairness pillar focuses on ensuring equitable outcomes and mitigating bias across different groups, making it the responsibility area that tackles biased amplification."
        },
        {
            "q": "Which Azure Machine Learning service feature enables automatic model selection from multiple candidate architectures without manual hyperparameter tuning?",
            "options": ["AutoML", "Data labeling pipelines", "Model registry", "MLOps CI/CD"],
            "answer": 0,
            "explanation": "Azure AutoML automatically searches through a space of algorithms and hyperparameters to find the best performing model for a given dataset, reducing the need for manual tuning."
        },
        {
            "q": "In a zero-shot prompting scenario for a large language model, what is the main limitation compared to few‑shot prompting?",
            "options": [
                "Requires labeled training data",
                "Cannot generalize beyond the knowledge encoded during pre‑training",
                "Needs excessive computational resources",
                "Produces deterministic outputs"
            ],
            "answer": 1,
            "explanation": "Zero-shot prompts rely solely on the model's existing knowledge, so without examples it may fail to adapt to tasks that are outside its pre‑training distribution, unlike few‑shot which provides contextual examples."
        },
        {
            "q": "Which technique creates a smaller 'student' model that imitates the output distribution of a larger 'teacher' model to reduce size and latency?",
            "options": ["Pruning", "Knowledge Distillation", "Quantization", "Ensemble Learning"],
            "answer": 1,
            "explanation": "Knowledge Distillation transfers knowledge from a large teacher model to a smaller student model by matching soft logits, resulting in a compact yet accurate model."
        },
        {
            "q": "When configuring Azure AI Search to improve relevance by ranking results based on semantic similarity rather than exact keyword matches, which built‑in capability should be enabled?",
            "options": ["Keyword matching", "Vector embeddings", "OCR", "Sentiment analysis"],
            "answer": 1,
            "explanation": "Enabling vector search (using precomputed embeddings) lets Azure AI Search rank documents by semantic similarity, improving relevance beyond simple keyword matching."
        },
        {
            "q": "Which metric is most suitable for evaluating disparate impact across demographic groups in a classification model, reflecting fairness concerns?",
            "options": ["Accuracy", "Precision‑Recall AUC", "Demographic parity", "F1 score"],
            "answer": 2,
            "explanation": "Demographic parity measures whether the positive outcome rate is similar across groups; it directly captures fairness and potential bias in classification decisions."
        },
        {
            "q": "To defend against adversarial examples that subtly perturb input data to cause misclassification, which approach directly enhances model robustness in accordance with responsible AI principles?",
            "options": ["Differential privacy", "Model ensembling", "Input preprocessing for noise removal", "Adversarial training"],
            "answer": 3,
            "explanation": "Adversarial training exposes the model to crafted adversarial inputs during training, teaching it to remain accurate despite small, malicious perturbations, thereby improving robustness."
        }
    ],

    "AI Generated Section 1778871326": [
        {
            "q": "Which of the following best describes the 'Transparency' principle in Microsoft's Responsible AI framework?",
            "options": [
                "Explaining how a model makes decisions so users can understand and trust it",
                "Encrypting data to protect against unauthorized access",
                "Reducing computational cost through model compression",
                "Automating model retraining without human intervention"
            ],
            "answer": 0,
            "explanation": "Transparency in responsible AI focuses on making the model's decision‑making process understandable to stakeholders, enabling them to see why a particular output was produced and fostering trust and accountability."
        },
        {
            "q": "Which Azure Cognitive Service is specifically designed to extract structured information such as fields from invoices or receipts?",
            "options": ["Computer Vision", "Text Analytics", "Language Understanding (LUIS)", "Form Recognizer / Document Intelligence"],
            "answer": 3,
            "explanation": "Form Recognizer (now known as Azure AI Document Intelligence) is built to automatically extract key‑value pairs, text, and tables from unstructured documents like invoices."
        },
        {
            "q": "In a fraud detection model where positive cases represent less than 1% of the data, which evaluation metric primarily measures the model's ability to correctly identify those rare positive instances?",
            "options": ["Accuracy", "Precision", "Recall", "ROC‑AUC"],
            "answer": 2,
            "explanation": "Recall (the true positive rate) emphasizes the model’s capacity to capture actual positive events, which is critical when missing positives has a high financial cost in imbalanced scenarios."
        },
        {
            "q": "What preprocessing technique converts categorical variables into a numeric representation suitable for most machine learning algorithms?",
            "options": ["One-hot encoding", "Principal Component Analysis (PCA)", "Linear regression imputation", "K‑means clustering"],
            "answer": 0,
            "explanation": "One‑hot encoding creates a binary column for each category, translating categorical data into a numeric format without imposing an artificial ordinal relationship among categories."
        },
        {
            "q": "During model development in Azure Machine Learning, which step explicitly separates the dataset into distinct subsets to prevent data leakage?",
            "options": ["Feature scaling", "Train/validation/test split", "Hyperparameter tuning", "Model registration"],
            "answer": 1,
            "explanation": "A train/validation/test split creates distinct datasets for model fitting, hyperparameter selection, and final evaluation, ensuring that information from the training set does not influence or artificially inflate validation performance."
        },
        {
            "q": "In reinforcement learning, which component provides the feedback signal that guides the agent’s behavior?",
            "options": ["Reward signal", "Loss function", "Gradient descent algorithm", "Decision tree"],
            "answer": 0,
            "explanation": "The reward signal tells the agent whether its actions are desirable or undesirable, allowing the policy to update and improve future decisions through trial‑and‑error learning."
        },
        {
            "q": "What is the primary security mechanism Azure uses to protect data that feeds AI models from unauthorized access?",
            "options": [
                "Data encryption at rest and in transit",
                "Network firewall rules only",
                "Model obfuscation techniques",
                "Access control lists (ACLs) on storage accounts only"
            ],
            "answer": 0,
            "explanation": "Azure encrypts data both while stored and during transmission, ensuring confidentiality and integrity of the training data used for AI models."
        }
    ],

    "AI Generated Section 1778871472": [
        {
            "q": "A business implements an AI chatbot powered by a Large Language Model (LLM). What is the most effective architectural pattern to ground the LLM's responses in verified, proprietary company documents rather than its generalized training knowledge?",
            "options": [
                "Fine-tuning the model with negative examples",
                "Implementing a Reinforcement Learning loop on every response",
                "Retrieval-Augmented Generation (RAG) using a vector database",
                "Increasing the temperature parameter during inference"
            ],
            "answer": 2,
            "explanation": "Retrieval-Augmented Generation (RAG) addresses hallucination by coupling the LLM with an external knowledge base. It retrieves relevant, verified documents based on the user query and feeds those specific chunks into the prompt context, forcing the LLM to base its answer on truth."
        },
        {
            "q": "You are deploying a computer vision solution to monitor an industrial conveyor belt. The system must precisely delineate the exact pixel boundaries of a defect (e.g., a hairline crack). Which AI modeling technique provides this highest level of granular spatial information?",
            "options": ["Object Detection (Bounding Boxes)", "Image Classification (Single Label)", "Semantic Segmentation", "Feature Extraction"],
            "answer": 2,
            "explanation": "While Object Detection identifies defects using a bounding box, Semantic Segmentation assigns a specific class label to *every single pixel* in the image. This creates a precise mask around the defect, achieving the highest level of spatial accuracy."
        },
        {
            "q": "A company uses an AI system to analyze customer support transcripts. They wish to automatically group similar issues (e.g., 'My account is locked,' 'login failed') into buckets without pre-defining the exact categories beforehand. This is best suited for which type of AI task?",
            "options": ["Named Entity Recognition (NER)", "Sentiment Analysis", "Clustering/Topic Modeling", "Optical Character Recognition (OCR)"],
            "answer": 2,
            "explanation": "Grouping similar data points into natural clusters without predefined labels fits the definition of Unsupervised Learning, specifically Clustering or Topic Modeling. The AI discovers the inherent groups rather than being told what they are."
        },
        {
            "q": "To move beyond simply tagging comments as 'Positive' or 'Negative,' a company wants the AI to understand emotional intensity and nuance (e.g., 'frustrated but hopeful'). Which specific NLP capability should be employed?",
            "options": ["Keyword Extraction", "Topic Modeling", "Sentiment Analysis (Emotion Detection/Opinion Mining)", "Named Entity Recognition (NER)"],
            "answer": 2,
            "explanation": "Basic Sentiment Analysis provides a simple polarity score. To achieve depth—mapping intensity, tone, and specific emotions like 'frustration'—the system must use advanced Sentiment Analysis capabilities like Emotion Detection or Opinion Mining."
        },
        {
            "q": "A customer service transcript is analyzed. The system determines the user's ultimate goal (e.g., 'Cancel Subscription,' 'Upgrade Plan'). This overall understanding of the desired outcome is referred to as:",
            "options": ["Entity Extraction", "Intent Recognition", "Sentiment Analysis", "Topic Modeling"],
            "answer": 1,
            "explanation": "Intent Recognition is the specific task of determining the user's ultimate goal or desired action from their language. Entity Extraction pulls out the details needed to fulfill that goal (e.g., Account Number)."
        },
        {
            "q": "You are attempting to guide a powerful LLM through a complex, multi-step reasoning task (e.g., 'Analyze this report and suggest strategies'). To maximize logical coherence, which prompting technique should you employ?",
            "options": ["Few-Shot Prompting", "Zero-Shot Prompting", "Chain-of-Thought (CoT) Prompting", "Role-Playing Prompting"],
            "answer": 2,
            "explanation": "Chain-of-Thought (CoT) prompting instructs the LLM to break down its complex problem into intermediate steps before arriving at the final answer. This forces the model to show its reasoning path, significantly improving accuracy on multi-step tasks."
        },
        {
            "q": "If a critical bottleneck arises during the inference phase where the volume of incoming data overwhelms the processing capacity, causing unacceptable delays in prediction delivery, this is primarily a concern regarding:",
            "options": ["Model Training Latency", "Data Preprocessing Error Rate", "Throughput and Scaling Bottleneck", "Feature Selection Inadequacy"],
            "answer": 2,
            "explanation": "Inference latency refers to the time taken for a single prediction. If the *volume* of incoming data exceeds the system's ability to handle it within acceptable timeframes, the issue is a failure in throughput and scaling."
        }
    ],

    "AI Generated Section 1778871615": [
        {
            "q": "A financial institution uses AI to monitor millions of transactions in real-time. The system flags activity that deviates significantly from the established 'normal' spending patterns of a specific user account. This relies on which machine learning paradigm?",
            "options": ["Supervised Classification", "Time Series Regression", "Unsupervised Anomaly Detection", "Reinforcement Learning"],
            "answer": 2,
            "explanation": "Anomaly Detection identifies rare items that deviate from the majority of data points. By establishing a baseline of 'normal' behavior and flagging deviations, the system performs unsupervised learning because it doesn't need pre-labeled examples of 'fraudulent' transactions to start."
        },
        {
            "q": "A company wants to extract specific, structured data, such as the 'Product Name' and 'Issue Reported,' from unstructured customer feedback emails. Which AI task is required?",
            "options": ["Image Recognition", "Sentiment Analysis", "Natural Language Generation (NLG)", "Named Entity Recognition (NER)"],
            "answer": 3,
            "explanation": "To extract specific, structured data entities like 'Product Name' or 'Location' from unstructured text, the model must perform Named Entity Recognition (NER), which identifies and categorizes key entities in text."
        },
        {
            "q": "A company is using Azure AI Vision. To make the system highly efficient, they utilize a massive pre-trained image recognition model developed by Microsoft and only fine-tune the final layers using their specific site data. This process is an example of:",
            "options": ["Data Augmentation", "Transfer Learning", "Zero-Shot Learning", "Ensemble Modeling"],
            "answer": 1,
            "explanation": "Transfer Learning involves leveraging a model previously trained on a vast, general dataset. By 'fine-tuning' only the final layers using a smaller, specific dataset, developers achieve high performance quickly with far less computational power."
        },
        {
            "q": "When building a predictive maintenance system, the goal is to predict the exact number of operational hours remaining before a machine failure. Which type of machine learning task is being executed?",
            "options": ["Classification (Binary)", "Regression", "Clustering (Unsupervised)", "Dimensionality Reduction"],
            "answer": 1,
            "explanation": "Regression is a machine learning task used to predict a continuous numerical value. Since the model is predicting a specific, measurable quantity (the Remaining Useful Life or RUL) in hours, it is performing regression."
        },
        {
            "q": "If developers want to improve a spam filter model to ensure it doesn't just classify based on a single common word like 'FREE,' they incorporate additional context like sender reputation and capitalization patterns. This enhancement process targets improving:",
            "options": ["Computational Speed", "Feature Engineering and Feature Selection", "Model Hyperparameters Only", "Hardware Scaling"],
            "answer": 1,
            "explanation": "Feature Engineering is the process of using domain knowledge to select and transform raw data into features that best predict the target variable, extracting deeper, more robust signals from the raw data."
        },
        {
            "q": "In high-stakes AI applications like automated medical diagnosis, the requirement that the AI system provides a clear, human-understandable chain of reasoning falls under the principle of:",
            "options": ["Scalability", "Low Latency Deployment", "Explainable AI (XAI)", "Model Compression"],
            "answer": 2,
            "explanation": "Explainable AI (XAI) is devoted to making complex 'black box' models understandable. In critical fields, simply arriving at a correct conclusion is insufficient; the system must justify its decision to allow human experts to audit and trust it."
        },
        {
            "q": "When developing an AI solution, the model achieves near-perfect accuracy on the training data but performs unpredictably and poorly on new, unseen production data. This scenario is best described as:",
            "options": ["Overfitting", "Underfitting", "Data Drift", "Bias Amplification"],
            "answer": 0,
            "explanation": "Overfitting occurs when a model learns the training data too well—including noise and anomalies unique to that dataset. While this grants high scores on training data, it fails to generalize effectively to new, real-world data."
        }
    ]
}