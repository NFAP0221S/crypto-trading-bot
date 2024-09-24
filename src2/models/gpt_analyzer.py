# models/gpt_analyzer.py

import openai
from utils.config import OPENAI_API_KEY
from utils.logger import logger

openai.api_key = OPENAI_API_KEY

def analyze_with_gpt(system_prompt, user_prompts):
    try:
        messages = [{"role": "system", "content": system_prompt}]
        messages += [{"role": "user", "content": prompt} for prompt in user_prompts]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        assistant_reply = response.choices[0].message.content
        logger.info("GPT analysis completed")
        return assistant_reply
    except Exception as e:
        logger.error(f"GPT analysis failed: {e}")
        return None
