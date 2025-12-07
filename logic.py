from storage import has_voted, write_vote, CANDIDATES

def process_vote(candidate_index: int, voter_identifier: str) -> None:
    """Process a vote for the selected candidate."""
    if has_voted(voter_identifier):
        raise ValueError(f"Voter {voter_identifier} has already voted.")

    if candidate_index < 0 or candidate_index >= len(CANDIDATES):
        raise ValueError(f"Invalid candidate index. Valid indexes are 0 to {len(CANDIDATES) - 1}.")

    try:
        candidate_name = CANDIDATES[candidate_index]
        write_vote(candidate_name, voter_identifier)
    except Exception as e:
        raise ValueError(f"Failed to process vote: {str(e)}")
