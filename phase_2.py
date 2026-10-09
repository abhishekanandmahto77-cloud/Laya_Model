import laya
import pandas as pd

# Read whole text from excel file
df = pd.read_excel("Questions.xlsx")
# Load Laya model
agent = laya.load("convaiinnovations/laya")


# Define the decisions we want Laya to make
schema = {
    "type": "object",
    "properties": {
        "intent": {
            "type": "string",
            "enum": [
                "login",
                "billing",
                "technical",
                "other",
                "cricket",
                "politics",
                "terrorism",
                "entertainment",
                "movies",
                "music",
                "gaming",
                "technology",
                "farming",
                "science",
                "health",
                "travel",
                "food",
                "fashion",
                "education"
            ]
        },

        "urgency": {
            "type": "string",
            "enum": [
                "low",
                "medium",
                "high"
            ]
        },

        "human_required": {
            "type": "boolean"
        }
    },

    "required": [
        "intent",
        "urgency",
        "human_required"
    ]
}


# Test input
text = """
I have been charged twice for my insurance policy.
Please refund the extra amount. If this is not resolved today,
I will escalate the issue.
"""


# Ask Laya to make all three decisions
# result = agent.decide(text, schema)
result = agent.decide(
    text,
    schema,
    return_details=True
)
print("Decision:")
print(result.values)

print("\nConfidence:")
print(result.answer_confidence)
for field, probabilities in result.probabilities.items():
    print(f"\n{field}:")
    for label, probability in probabilities.items():
        print(f"  {label}: {probability:.4f}")
# print(result1)
# print(agent.decide("I cannot login to my account even after resetting my password",schema,return_details=True))
# print(agent.decide("I was charged twice for my insurance policy. Please refund the extra amount.",schema,return_details=True))
# print(agent.decide("The application crashes whenever I try to upload a document.",schema,return_details=True))
# print(agent.decide("What are the different insurance plans available?",schema,return_details=True))
# print(agent.decide("I met Rohit yesterday. He is one of the best batters in the world.",schema,return_details=True))
# print(agent.decide("Where can I find black soil suitable for farming in India?",schema,return_details=True))
# print(agent.decide("My account has been compromised and I can see transactions I did not make.",schema,return_details=True))
# print(agent.decide("Can you tell me how artificial intelligence works?",schema,return_details=True))
# print(agent.decide("The website is temporarily unavailable. I have an important payment due today.",schema,return_details=True))
# print(agent.decide("I would like information about travelling to Europe",schema,return_details=True))



