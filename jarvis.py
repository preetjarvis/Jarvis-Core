import time

COMMANDER = "PREET"
AUTHORIZED = False

def authorize(commander_name):
    global AUTHORIZED
    if commander_name.upper() == COMMANDER:
        AUTHORIZED = True
        return "Authorization confirmed. Awaiting commands."
    return "Authorization denied."

def think(problem):
    return f"Thinking deeply about: {problem}"

def propose_solution(problem):
    return f"Proposed solution for '{problem}': Analyze, simulate, refine."

def execute(action):
    if not AUTHORIZED:
        return "Execution blocked. Commander authorization required."
    return f"Executing action: {action}"

if __name__ == "__main__":
    print("Jarvis core online. Advisory mode active.")
    while True:
        time.sleep(5)
