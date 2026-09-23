import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from prompts import (
    VIVA_PROMPT,
    EVALUATION_PROMPT,
    NEXT_QUESTION_PROMPT
)

from memory import VivaMemory


# ==========================================
# 1. Load environment variables
# ==========================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("\nError: GOOGLE_API_KEY is not configured.")
    print("Please add your Gemini API key to the .env file.")
    exit()


# ==========================================
# 2. Create AI model
# ==========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)


# ==========================================
# 3. Create memory
# ==========================================

memory = VivaMemory()


# ==========================================
# 4. Create prompts and chains
# ==========================================

question_prompt = ChatPromptTemplate.from_template(
    VIVA_PROMPT
)

question_chain = question_prompt | llm


evaluation_prompt = ChatPromptTemplate.from_template(
    EVALUATION_PROMPT
)

evaluation_chain = evaluation_prompt | llm


next_question_prompt = ChatPromptTemplate.from_template(
    NEXT_QUESTION_PROMPT
)

next_question_chain = next_question_prompt | llm


# ==========================================
# 5. Get subject from student
# ==========================================

subject = input("Enter your subject: ")


# ==========================================
# 6. Generate first viva question
# ==========================================

try:

    response = question_chain.invoke({
        "subject": subject
    })

except Exception as e:

    print("\nError: Unable to connect to the AI service.")
    print("Please check your API key, internet connection, or API quota.")
    print(f"Details: {e}")
    exit()


question = response.content[0]["text"]

print("\nVivaBuddy:")
print(question)


# ==========================================
# 7. Viva rounds
# ==========================================

for round_number in range(1, 4):

    print(f"\n---------- Round {round_number} ----------")

    answer = input("\nYour answer: ")


    # ======================================
    # Evaluate student's answer
    # ======================================

    try:

        evaluation = evaluation_chain.invoke({
            "subject": subject,
            "question": question,
            "answer": answer
        })

    except Exception as e:

        print("\nError: Unable to evaluate your answer.")
        print("Please check your API quota or internet connection.")
        print(f"Details: {e}")
        exit()


    evaluation_text = evaluation.content[0]["text"]

    print("\nVivaBuddy Evaluation:")
    print(evaluation_text)


    # ======================================
    # Save conversation to memory
    # ======================================

    memory.add(
        question=question,
        answer=answer,
        evaluation=evaluation_text
    )


    # ======================================
    # Stop after 3 rounds
    # ======================================

    if round_number == 3:
        break


    # ======================================
    # Ask whether to continue
    # ======================================

    continue_viva = input(
        "\nContinue to next question? (yes/no): "
    )


    if continue_viva.lower() != "yes":
        break


    # ======================================
    # Get previous conversation
    # ======================================

    history = memory.get_formatted_history()


    # ======================================
    # Generate next question
    # ======================================

    try:

        next_question = next_question_chain.invoke({
            "subject": subject,
            "history": history
        })

    except Exception as e:

        print("\nError: Unable to generate the next question.")
        print("Please check your API quota or internet connection.")
        print(f"Details: {e}")
        exit()


    question = next_question.content[0]["text"]

    print("\nVivaBuddy:")
    print(question)


# ==========================================
# 8. Final session summary
# ==========================================

print("\n================================")
print("Viva session completed!")
print("================================")

print(f"\nSubject: {subject}")
print(f"Rounds completed: {len(memory.get_history())}")

print("\nThank you for practicing with VivaBuddy!") 