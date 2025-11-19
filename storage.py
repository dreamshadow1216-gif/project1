import csv
import os

VOTES_FILE = "votes.csv"
VOTER_IDS_FILE = "voter_ids.csv"
CANDIDATES = ["Alice", "Bob", "Charlie"]

def process_vote(candidate_index: int, voter_identifier: str) -> None:
    if has_voted(voter_identifier):
        raise ValueError("Duplicate vote detected.")

    try:
        candidate_name = CANDIDATES[candidate_index]
        write_vote(candidate_name, voter_identifier)
    except IndexError:
        raise ValueError("Invalid candidate index.")

def write_vote(candidate_name: str, voter_identifier: str) -> None:
    if not os.path.exists(VOTES_FILE):
        with open(VOTES_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Voter ID", "Candidate"])

    if not os.path.exists(VOTER_IDS_FILE):
        with open(VOTER_IDS_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Voter ID"])

    with open(VOTES_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([voter_identifier, candidate_name])

    with open(VOTER_IDS_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([voter_identifier])

def has_voted(voter_identifier: str) -> bool:
    if not os.path.exists(VOTER_IDS_FILE):
        return False

    with open(VOTER_IDS_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return any(row[0] == voter_identifier for row in reader if row)

def count_votes() -> int:
    try:
        with open(VOTES_FILE, "r", newline="", encoding="utf-8") as file:
            return sum(1 for row in csv.reader(file) if row)
    except FileNotFoundError:
        return 0

def get_votes_for_candidate(candidate_name: str) -> int:
    try:
        with open(VOTES_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            return sum(1 for row in reader if row and row[1] == candidate_name)
    except FileNotFoundError:
        return 0

def clear_counter_votes() -> None:
    try:
        with open(VOTES_FILE, "w", newline="", encoding="utf-8"):
            pass
    except Exception as e:
        raise Exception(f"Error clearing vote file: {str(e)}")

def clear_voter_ids() -> None:
    try:
        with open(VOTER_IDS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Voter ID"])  # Write header for voter IDs (clearing the content)
    except Exception as e:
        raise Exception(f"Error clearing voter IDs: {str(e)}")