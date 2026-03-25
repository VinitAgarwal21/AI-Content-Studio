
from core.prompt_builder import get_prompt_template
from core.parser import parse_output
from llm_helper import llm


def generate_post(data):
    platform = data.get("platform")

    prompt_template = get_prompt_template(platform)

    chain = prompt_template | llm

    response = chain.invoke({
        "platform": platform,
        "topic": data.get("topic"),
        "tone": data.get("tone"),
        "audience": data.get("audience", ""),
        "points": data.get("points", ""),
        "context": data.get("context", ""),
        "cta": data.get("cta", "")
    })

    result = parse_output(response)

    return result["content"] + "\n\n" + " ".join(result["hashtags"])