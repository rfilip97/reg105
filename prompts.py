PREPROMPT = (
    "You are a regression tester. Examine the provided screenshot and verify the placement of the UI elements "
    "based on the criteria listed below. Respond only with 'LGTM'(and nothing more) if all elements are "
    "correctly placed according to the specifications. If any discrepancies are "
    "found, list them using bullet points."
)


def get_prompt(items):
    prompt = "\n\nCheck if the following statements are true for the received image:"

    for item in items:
        prompt += f"\n- '{item}'"

    return (
        prompt
        + "\n\nRemember to respond with 'LGTM' and nothing more if you find all the above checks to be true."
    )
