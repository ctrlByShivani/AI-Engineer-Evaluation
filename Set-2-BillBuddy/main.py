from agent import run_agent


print("=" * 45)
print("        💰 BillBuddy AI Assistant")
print("=" * 45)
print("Type 'exit' to quit.\n")


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("BillBuddy: Goodbye! 👋")
        break

    if not user_input.strip():
        continue

    try:
        response = run_agent(user_input)
        print(f"\nBillBuddy: {response}\n")

    except Exception as e:
        print(f"\nBillBuddy error: {e}\n")