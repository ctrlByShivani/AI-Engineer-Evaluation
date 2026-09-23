import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import ToolMessage
from tools import split_bill, calculate_tip
from prompts import SYSTEM_PROMPT


load_dotenv()


def create_agent():
    model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0
    )

    tools = [split_bill, calculate_tip]

    model_with_tools = model.bind_tools(tools)

    return model_with_tools


def run_agent(user_input: str):
    agent = create_agent()

    tools = {
        "split_bill": split_bill,
        "calculate_tip": calculate_tip
    }

    messages = [
        ("system", SYSTEM_PROMPT),
        ("human", user_input)
    ]

    response = agent.invoke(messages)

    while response.tool_calls:
        messages.append(response)

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            if tool_name in tools:
                tool_result = tools[tool_name].invoke(tool_args)

                messages.append(
                    ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
    )
)
        response = agent.invoke(messages)

    if isinstance(response.content, str):
        return response.content

    if isinstance(response.content, list):
        return "".join(
            item.get("text", "")
            for item in response.content
            if isinstance(item, dict)
    )

    return str(response.content)