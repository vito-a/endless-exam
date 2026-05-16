# /config/config.py
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "lm-studio")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "http://127.0.0.1:1234/v1/")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "nvidia/nemotron-3-nano-omni") # "google/gemma-4-26b-a4b"
NUM_QUESTIONS_TO_GENERATE = int(os.getenv("NUM_QUESTIONS_TO_GENERATE", "7"))
GENERATION_DELAY_SECONDS = int(os.getenv("GENERATION_DELAY_SECONDS", "60"))
GENERATOR_MAX_TOKENS = int(os.getenv("GENERATOR_MAX_TOKENS", "10000"))
