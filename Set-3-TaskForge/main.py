from agents import (
    create_coordinator,
    create_researcher,
    create_writer,
    create_reviewer
)

from prompts import (
    COORDINATOR_PROMPT,
    RESEARCHER_PROMPT,
    WRITER_PROMPT,
    REVIEWER_PROMPT
)

def run_task(topic):
    try:
        coordinator = create_coordinator()
        researcher = create_researcher()
        writer = create_writer()
        reviewer = create_reviewer()

        # Step 1: Coordinator manages the task
        coordinator_response = coordinator.invoke([
            ("system", COORDINATOR_PROMPT),
            ("human", f"Manage this task: Create a report about {topic}")
        ])

        print("\n[Coordinator] Task plan:")
        print(coordinator_response.content)

        # Step 2: Researcher researches the topic
        research_response = researcher.invoke([
            ("system", RESEARCHER_PROMPT),
            ("human", f"Research the following topic:\n{topic}")
        ])

        print("\n[Researcher] Research completed.")

        # Step 3: Writer creates the report
        writer_response = writer.invoke([
            ("system", WRITER_PROMPT),
            ("human", f"""
Create a structured report using the following research.

Topic:
{topic}

Research:
{research_response.content}
""")
        ])

        print("[Writer] Report draft created.")

        # Step 4: Reviewer checks and improves the report
        review_response = reviewer.invoke([
            ("system", REVIEWER_PROMPT),
            ("human", f"""
Review and improve the following report.

Topic:
{topic}

Report:
{writer_response.content}
""")
        ])

        print("[Reviewer] Report reviewed and finalized.")

        if isinstance(review_response.content, str):
            return review_response.content

        if isinstance(review_response.content, list):
            return "".join(
                item.get("text", "")
                for item in review_response.content
                if isinstance(item, dict)
            )

        return str(review_response.content)

    except Exception as e:
        return f"TaskForge could not complete the task.\nReason: {str(e)}"
    # Step 1: Coordinator manages the task
    coordinator_response = coordinator.invoke([
        ("system", COORDINATOR_PROMPT),
        ("human", f"Manage this task: Create a report about {topic}")
    ])
    print("\n[Coordinator] Task plan:")
    print(coordinator_response.content)

    # Step 2: Researcher researches the topic
    research_response = researcher.invoke([
        ("system", RESEARCHER_PROMPT),
        ("human", f"Research the following topic:\n{topic}")
    ])
    print("[Researcher] Research completed.")

    # Step 3: Writer creates the report
    writer_response = writer.invoke([
        ("system", WRITER_PROMPT),
        ("human", f"""
Create a structured report using the following research.

Topic:
{topic}

Research:
{research_response.content}
""")
    ])

    print("[Writer] Report draft created.")
    # Step 4: Reviewer checks and improves the report
    review_response = reviewer.invoke([
        ("system", REVIEWER_PROMPT),
        ("human", f"""
Review and improve the following report.

Topic:
{topic}

Report:
{writer_response.content}
""")
    ])
    print("[Reviewer] Report reviewed and finalized.")

    if isinstance(review_response.content, str):
        return review_response.content

    if isinstance(review_response.content, list):
        return "".join(
        item.get("text", "")
        for item in review_response.content
        if isinstance(item, dict)
    )

    return str(review_response.content)

print("=" * 50)
print("           🤖 TaskForge")
print("=" * 50)

topic = input("\nEnter a topic for the report: ")

if topic.strip():
    try:
        final_report = run_task(topic)

        print("\n" + "=" * 50)
        print("FINAL REPORT")
        print("=" * 50)
        print(final_report)

    except Exception as e:
        print(f"\nTaskForge AI error: {e}")

else:
    print("Please enter a topic.")