from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox
from storage import count_votes, clear_counter_votes, CANDIDATES, get_votes_for_candidate, clear_voter_ids

class AdminPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Admin Page")

        # Create layout
        self.layout = QVBoxLayout(self)


        total_votes = count_votes()  # Get total number of votes
        self.total_votes_label = QLabel(f"Total Votes : {total_votes}", self)
        self.layout.addWidget(self.total_votes_label)


        self.candidate_labels = {}
        for candidate in CANDIDATES:
            candidate_label = QLabel(f"{candidate}: {get_votes_for_candidate(candidate)}", self)
            self.candidate_labels[candidate] = candidate_label
            self.layout.addWidget(candidate_label)

        self.clear_button = QPushButton("Clear All Votes", self)
        self.clear_button.clicked.connect(self.clear_votes)
        self.layout.addWidget(self.clear_button)
        self.clear_voter_ids_button = QPushButton("Clear All Voter IDs", self)
        self.clear_voter_ids_button.clicked.connect(self.clear_voter_ids)
        self.layout.addWidget(self.clear_voter_ids_button)

        # Set the layout for the dialog
        self.setLayout(self.layout)

    def clear_votes(self) -> None:

        clear_counter_votes()
        self.total_votes_label.setText(f"Total Votes Cast: 0")  # Reset vote count
        for candidate, label in self.candidate_labels.items():
            label.setText(f"{candidate}: 0")  # Reset candidate vote counts
        self.show_message("Success", "All votes have been cleared.", "success")

    def clear_voter_ids(self) -> None:
        try:
            # Call the function to clear voter IDs from the file
            clear_voter_ids()
            self.show_message("Success", "All voter IDs have been cleared.", "success")
        except Exception as e:
            self.show_message("Error", f"An error occurred while clearing voter IDs: {str(e)}", "error")

    def show_message(self, title: str, message: str, message_category: str) -> None:
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        if message_category == "success":
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet("QMessageBox { background-color: #d4edda; color: #155724; }")
        elif message_category == "error":
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStyleSheet("QMessageBox { background-color: #f8d7da; color: #721c24; }")

        msg_box.exec()