def build_prompt(user_query):

    return f"""
    User Question: {user_query}

    Please provide:

    1. Eligibility Criteria
    2. Required Documents
    3. Step-by-Step Application Process
    4. Estimated Processing Time
    5. Visa Fees (approximate)
    6. Important Tips

    Keep the answer structured and easy to understand.
    """
