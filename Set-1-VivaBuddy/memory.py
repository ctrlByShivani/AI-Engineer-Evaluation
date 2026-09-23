class VivaMemory:

    def __init__(self):
        self.history = []

    def add(self, question, answer, evaluation):
        self.history.append({
            "question": question,
            "answer": answer,
            "evaluation": evaluation
        })

    def get_history(self):
        return self.history

    def get_formatted_history(self):
        if not self.history:
            return "No previous conversation."

        formatted_history = ""

        for i, item in enumerate(self.history, start=1):
            formatted_history += f"""
Round {i}
Question: {item["question"]}
Student Answer: {item["answer"]}
Evaluation: {item["evaluation"]}
"""

        return formatted_history