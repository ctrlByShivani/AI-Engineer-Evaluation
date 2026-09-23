from langchain_core.tools import tool


@tool
def split_bill(total_amount: float, number_of_people: int) -> str:
    """
    Split a bill equally among a given number of people.
    """

    try:
        if total_amount < 0:
            return "Bill error: total amount cannot be negative."

        if number_of_people <= 0:
            return "Bill error: number of people must be greater than zero."

        amount_per_person = total_amount / number_of_people

        return (
            f"Total bill: ₹{total_amount:.2f}\n"
            f"Number of people: {number_of_people}\n"
            f"Amount per person: ₹{amount_per_person:.2f}"
        )

    except Exception as e:
        return f"Bill error: {str(e)}"


@tool
def calculate_tip(bill_amount: float, tip_percentage: float) -> str:
    """
    Calculate the tip amount and total bill including tip.
    """

    try:
        if bill_amount < 0:
            return "Tip error: bill amount cannot be negative."

        if tip_percentage < 0:
            return "Tip error: tip percentage cannot be negative."

        tip_amount = bill_amount * tip_percentage / 100
        total = bill_amount + tip_amount

        return (
            f"Bill amount: ₹{bill_amount:.2f}\n"
            f"Tip ({tip_percentage:.1f}%): ₹{tip_amount:.2f}\n"
            f"Total with tip: ₹{total:.2f}"
        )

    except Exception as e:
        return f"Tip error: {str(e)}"