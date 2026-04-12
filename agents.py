def hr_agent(answer):
    if len(answer) < 20:
        return "Answer too short, improve communication."
    return "Good communication."

def technical_agent(role):
    if "java" in role.lower():
        return "Explain OOP principles in Java."
    elif "ai" in role.lower():
        return "Explain supervised learning."
    return "Explain one technical project."

def career_agent(role):
    if "java" in role.lower():
        return "Improve DSA and SQL."
    elif "ai" in role.lower():
        return "Strengthen ML projects."
    return "Build stronger portfolio."