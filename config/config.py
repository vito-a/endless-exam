# /config/config.py
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "lm-studio")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "http://127.0.0.1:1234/v1/")
# "nvidia/nemotron-3-nano-omni" "nvidia/nemotron-3-nano" "liquid/lfm2-24b-a2b"
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "google/gemma-4-26b-a4b-qat")

NUM_QUESTIONS_TO_GENERATE = int(os.getenv("NUM_QUESTIONS_TO_GENERATE", "7"))
GENERATION_DELAY_SECONDS = int(os.getenv("GENERATION_DELAY_SECONDS", "60"))
GENERATOR_MAX_TOKENS = int(os.getenv("GENERATOR_MAX_TOKENS", "10000"))
MAX_GENERATION_RETRIES = int(os.getenv("MAX_GENERATION_RETRIES", "5"))

DISTILLATION_BUFFER_SECTIONS = int(os.getenv("DISTILLATION_BUFFER_SECTIONS", "5"))
MAX_DISTILL_BATCH_SIZE = int(os.getenv("MAX_DISTILL_BATCH_SIZE", "50"))
ENABLE_DISTILLATION = os.getenv("ENABLE_DISTILLATION", "True").lower() == "false"
