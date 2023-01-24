import argparse
from inspect import cleandoc
import tokenize
import token
import json


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
parser.add_argument("-f", "--file")
parser.add_argument("-l", "--log")

args = parser.parse_args()

# Scrape updates from provided file.
updates = {}
with tokenize.open(args.file) as f:
    tokens = tokenize.generate_tokens(f.readline)
    for t in tokens:
        if t.type == token.COMMENT and t.string.startswith("# UPDATE"):
            updates[t.string[9]] = t.string[11:]

# Load log data from file.
with open(args.log) as f:
    log = json.load(f)

feedbacks = {
    str(i + 1): record["responseExpert"] for i, record in enumerate(log["records"])
}

if args.mode == "feedback":
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
elif args.mode == "records":
    msg = f"""
    Initial state
    Data: {log["initialState"]["data"]}
    Model: {log["initialState"]["model"]}
    Metrics: {log["initialState"]["metrics"]}
    """
    for record in log["records"]:
        table = f"""
        {"What?":<10.10}|{"Where?":<10.10}|{"When?":<20.20}|{"Why?":<40.40}|{"Impact":<20.20}|
        {'-' * 105}
        """
        for update in record["updates"]:
            table += f"""{update["what"]:<10.10}|{update["where"]:<10.10}|{update["when"]:<20.20}|{update["why"]:<40.40}|{update["impact"]:<20.20}|"""

        msg += f"""
        Prompt: {record["prompt"]}
        Shared Information: {record["sharedInformation"]}
        Expert Response: {record["responseExpert"]}

        {table}

        Update summary: {record["updateSummary"]}
        """

    msg += f"""
    Final state
    Data: {log["finalState"]["data"]}
    Model: {log["finalState"]["model"]}
    Metrics: {log["finalState"]["metrics"]}
    """

# TODO: Add updates
# elif args.mode == "add-record":
#     print("Initial State.\n")

#     initial_data = input("Data:")
#     initial_model = input("Model:")
#     initial_metrics = input("Metrics:")

#     print("\nRecords.\n...\n")

#     print("Final State.\n...\n")

#     msg = """
#         Logged record successfully to log.json.
#         Please view at https://feedback-log.web.app/feedback
#         """

print(cleandoc(msg))
