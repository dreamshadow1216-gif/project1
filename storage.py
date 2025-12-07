import csv
import os

VOTES_FILE = "votes.csv"
"""CSV file storing all votes."""

VOTER_IDS_FILE = "voter_ids.csv"
"""CSV file storing all voter IDs."""

CANDIDATES = ["Alice", "Bob", "Charlie"]
"""List of candidates available for voting."""


def process_vote(candidate_index: int, voter_identifier: str) -> None:
    """Record a vote for a candidate if voter hasn't voted."""
    if has_voted(voter_identifier):
        raise ValueError("Duplicate vote detected.")

    try:
        candidate_name = CANDIDATES[candidate_index]
        write_vote(candidate_name, voter_identifier)
    except IndexError:
        raise ValueError("Invalid candidate index.")


def write_vote(candidate_name: str, voter_identifier: str) -> None:
    """Write vote and voter ID to CSV files."""
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
    """Check if a voter ID has already voted."""
    if not os.path.exists(VOTER_IDS_FILE):
        return False

    with open(VOTER_IDS_
