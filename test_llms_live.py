import os
from dotenv import load_dotenv
from llms import DeepSeekModel, OpenAI, DeepSeek, OpenAIModel, ReasoningEffort


def test_openai_gpt_3_5_turbo():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_3_5_TURBO)
    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_4():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_4)
    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_4_turbo():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_4_TURBO)

    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_4_o():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_4_O)

    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_4_o_mini():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_4_O_MINI)

    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_o1():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_O1)

    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_o1_mini():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_O1_MINI)

    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_o3_mini():
    """Test OpenAI LLM with a real API call"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_O3_MINI)

    # Test basic completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI test failed: {e}")


def test_openai_gpt_o1_mini_with_reasoning():
    """Test OpenAI LLM with a reasoning model"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set")
        return

    llm = OpenAI(api_key, OpenAIModel.GPT_O1_MINI,
                 reasoning_effort=ReasoningEffort.MEDIUM)

    # Test reasoning model with a coding problem
    prompt = """
    Write a bash script that takes a matrix represented as a string with 
    format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
    """

    messages = [
        {"role": "user", "content": prompt}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== OpenAI Reasoning Model Test ===")
        print(f"Testing {llm.to_string()}")
        print(f"Prompt: {prompt}")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"OpenAI reasoning model test failed: {e}")


def test_deepseek_chat():
    """Test DeepSeek LLM with a real API call"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("ERROR: DEEPSEEK_API_KEY environment variable not set")
        return

    llm = DeepSeek(api_key)

    # Test code completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== DeepSeek Chat Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"DeepSeek chat test failed: {e}")


def test_deepseek_reasoner():
    """Test DeepSeek Reasoner LLM with a real API call"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("ERROR: DEEPSEEK_API_KEY environment variable not set")
        return

    llm = DeepSeek(api_key, DeepSeekModel.DEEPSEEK_REASONER)

    # Test code completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    try:
        response = llm._call_llm(messages)
        print("\n=== DeepSeek Reasoner Test ===")
        print(f"Testing {llm.to_string()}")
        print("Query: What is the capital of France?")
        print(f"Response: {response}\n")
    except Exception as e:
        print(f"DeepSeek reasoner test failed: {e}")


def main():
    load_dotenv()

    print("Starting LLM live tests...")
    # Test OpenAI
    # test_openai_gpt_3_5_turbo()
    # test_openai_gpt_4()
    # test_openai_gpt_4_turbo()
    # test_openai_gpt_4_o()
    # test_openai_gpt_4_o_mini()
    # test_openai_gpt_o1()
    # test_openai_gpt_o1_mini_with_reasoning()
    # test_openai_gpt_o3_mini()

    # Test DeepSeek
    # test_deepseek_chat()
    # test_deepseek_reasoner()


if __name__ == "__main__":
    main()
