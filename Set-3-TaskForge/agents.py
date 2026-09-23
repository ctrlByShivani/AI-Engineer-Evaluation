from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts import (
    COORDINATOR_PROMPT,
    RESEARCHER_PROMPT,
    WRITER_PROMPT,
    REVIEWER_PROMPT
)


load_dotenv()


def create_coordinator():
    return ChatGoogleGenerativeAI(
       model="gemini-3.5-flash-lite",
        temperature=0
    )


def create_researcher():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        temperature=0
    )


def create_writer():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        temperature=0
    )


def create_reviewer():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        temperature=0
    )