import argparse
from inspect import cleandoc
import tokenize
import token


class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[32m"
    WARNING = "\033[31m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


parser = argparse.ArgumentParser(
    prog="FeedbackLog",
    description="Logs feedback",
    epilog="Used to track feedback and updates",
)


parser.add_argument("mode")

args = parser.parse_args()

updates = {}

with tokenize.open("model.py") as f:
    tokens = tokenize.generate_tokens(f.readline)
    for t in tokens:
        if t.type == token.COMMENT and t.string.startswith("# UPDATE"):
            updates[t.string[9]] = t.string[11:]

feedbacks = {"1": "Model is overconfident.", "2": "Model should use X metric."}

match args.mode:
    case "feedback":
        msg = ""
        for id, feedback in feedbacks.items():
            if id in updates:
                msg += f"""
                Feedback {id}:
                {colors.OKGREEN}[COMPLETE] {feedback} {colors.ENDC}
                Update: {updates[id]}
                """
            else:
                msg += f"""
                Feedback {id}:
                {colors.WARNING}[TODO] {feedback} {colors.ENDC}
                """

    case "records":
        msg = f"""
        Record 1
        --------

        Initial state
        Data: data
        Model: resnet
        Metrics: robustness

        What?   | Where?    | When?             | Why?                      | Impact        |
        -------------------------------------------------------------------------------------
        CutMix  | Dataset   | Before training   | Background insensitivity  | Robustness +5%|

        Final state:
        data: data
        Model: resnet
        Metrics: robustness
        """

    case "add-record":
        print("Initial State.\n")

        initial_data = input("Data:")
        initial_model = input("Model:")
        initial_metrics = input("Metrics:")

        print("\nRecords.\n...\n")

        print("Final State.\n...\n")

        msg = """
        Logged record successfully to log.json.
        Please view at https://feedback-log.web.app/feedback
        """

print(cleandoc(msg))
