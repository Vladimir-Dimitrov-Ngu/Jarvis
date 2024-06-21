import json
from copy import deepcopy

import requests

from config import catalog_id, secret_key, system_prompt


def _get_response_yandex_gpt(original_context: list[dict], text: str):
    context = deepcopy(original_context)
    sp = {
        "role": "system",
        "text": f"{system_prompt}",
    }
    context.insert(0, sp)
    prompt = {
        "modelUri": f"gpt://{catalog_id}/yandexgpt-lite",
        "completionOptions": {"stream": False, "temperature": 0.3, "maxTokens": "40"},
        "messages": context,
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {secret_key}",
    }

    response = requests.post(url, headers=headers, json=prompt, timeout=10)
    result = response.text
    json_data = json.loads(result)
    return (
        json_data["result"]["alternatives"][0]["message"]["text"],
        json_data["result"]["usage"]["totalTokens"],
    )


if __name__ == "__main__":
    text = "Привет :)"
    result, tokens = _get_response_yandex_gpt(text)
    print(result)
