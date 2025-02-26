from typing import Dict, List, Optional
from enum import Enum, auto

import openai
from openai.types.chat import ChatCompletion


class OpenAIModel(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4_O = "gpt-4o"
    GPT_4_O_MINI = "gpt-4o-mini"
    GPT_O1 = "o1"
    GPT_O1_MINI = "o1-mini"
    GPT_O3_MINI = "o3-mini"


class ReasoningEffort(Enum):
    NONE = None
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class DeepSeekModel(Enum):
    DEEPSEEK_CHAT = "deepseek-chat"
    DEEPSEEK_REASONER = "deepseek-reasoner"


class BaseLLM:
    def __init__(self, api_key: str, model: Enum) -> None:
        self.api_key = api_key
        self.model = model

    def _call_llm(self, messages: List[Dict[str, str]]) -> str:
        raise NotImplementedError

    def _format_message(self, role: str, content: str) -> Dict[str, str]:
        return {"role": role, "content": content}

    def to_string(self) -> str:
        """Convert the object to a string representation."""
        return f"Model: {self.model.value}"


class OpenAI(BaseLLM):
    def __init__(self, 
                api_key: str, 
                model: OpenAIModel = OpenAIModel.GPT_3_5_TURBO,
                reasoning_effort: ReasoningEffort = ReasoningEffort.NONE) -> None:
        super().__init__(api_key, model)
        self.client = openai.OpenAI(api_key=api_key)
        self.reasoning_effort = reasoning_effort
        
    def _is_reasoning_model(self) -> bool:
        """Check if the current model is a reasoning model."""
        reasoning_models = [
            OpenAIModel.GPT_O1.value,
            OpenAIModel.GPT_O3_MINI.value
        ]
        return self.model.value in reasoning_models

    def _call_llm(self, messages: List[Dict[str, str]]) -> str:
        kwargs = {
            "model": self.model.value,
            "messages": [self._format_message(m["role"], m["content"]) for m in messages]
        }
        
        # Add reasoning_effort parameter for reasoning models if specified
        if self._is_reasoning_model() and self.reasoning_effort != ReasoningEffort.NONE:
            kwargs["reasoning_effort"] = self.reasoning_effort.value

        print(kwargs)
            
        response: ChatCompletion = self.client.chat.completions.create(**kwargs)
        return response.choices[0].message.content

    def to_string(self) -> str:
        """Convert the object to a string representation."""
        base_str = f"OpenAI with Model: {self.model.value}"
        if self._is_reasoning_model() and self.reasoning_effort != ReasoningEffort.NONE:
            return f"{base_str}, Reasoning Effort: {self.reasoning_effort.value}"
        return base_str


class DeepSeek(BaseLLM):
    def __init__(self, api_key: str, model: DeepSeekModel = DeepSeekModel.DEEPSEEK_CHAT) -> None:
        super().__init__(api_key, model)
        self.client = openai.OpenAI(
            api_key=api_key, base_url="https://api.deepseek.com")

    def _call_llm(self, messages: List[Dict[str, str]]) -> str:
        response: ChatCompletion = self.client.chat.completions.create(
            model=self.model.value,
            messages=[self._format_message(
                m["role"], m["content"]) for m in messages]
        )
        return response.choices[0].message.content

    def to_string(self) -> str:
        """Convert the object to a string representation."""
        return f"DeepSeek with Model: {self.model.value}"
