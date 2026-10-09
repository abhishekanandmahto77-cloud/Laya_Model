import laya

agent = laya.load("convaiinnovations/laya")

schema = {
    "type": "object",
    "properties": {
        "issue": {
            "type": "string",
            "enum": ["login", "billing", "technical", "other","cricket","politics","terrorism","entertainment","movies","music","gaming","technology","farming","science","health","travel","food","fashion","education"]
        }
    },
    "required": ["issue"]
}

result = agent.decide(
    "I am unable to login to my account. I have tried resetting my password several times.",
    schema
)
result1 = agent.decide(
    "I met Rohit yesterday. he is one of the best batter in the world.",
    schema
)
result2 = agent.decide(
    "I met Narendra yesterday.he told no one could beat him in election.",
    schema
)
result3 = agent.decide(
    "where i can find black soil land in india",
    schema
)
print(result)
print(result1)
print(result2)
print(result3)

