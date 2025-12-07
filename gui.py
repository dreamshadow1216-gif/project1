from PyQt6.QtWidgets import QDialog, QVBoxLayout, QRadioButton, QPushButton, QLineEdit, QLabel, QMessageBox
from storage import process_vote, has_voted
from admin import AdminPage

SPECIAL_ADMIN_ID = "admin"


class VotingApp(QDialog):
    """Main voting window where users enter ID and select a candidate."""

    def __init__(self, parent=None):
        """Set up the voting UI."""
        super().__init__(parent)
        self.setWindowTitle("Voting System")

        self.layout = QVBoxLayout(self)

        self.voter_id_input = QLineEdit(self)

        self.candidate_radio_buttons = {
            "Jane": QRadioButton("Jane", self),
            "John": QRadioButton("John", self),
            "James": QRadioButton("James", self),
        }

        self.vote_button = QPushButton("Vote!", self)
        self.vote_button.clicked.connect(self.submit_vote)

        self.layout.addWidget(QLabel("Voter ID:"))
        self.layout.addWidget(self.voter_id_input)

        self.layout.addWidget(QLabel("Select Candidate:"))
        for rb in self.candidate_radio_buttons.values():
            self.layout.addWidget(rb)

        self.layout.addWidget(self.vote_button)
        self.setLayout(self.layout)

    def submit_vote(self) -> None:
        """Validate input, process vote, or open admin panel."""
        voter_id = self.voter_id_input.text().strip()

        if not voter_id:
            self.show_message("Error", "Must have Voter ID", "error")
            return

        if voter_id == SPECIAL_ADMIN_ID:
            self.open_admin_panel()
            return

        if has_voted(voter_id):
            self.show_message("Error", "This ID has already voted.", "error")
            return

        selected = [name for name, rb in self.candidate_radio_buttons.items() if rb.isChecked()]
        if not selected:
            self.show_message("Error", "Must select a candidate", "error")
            return

        try:
            candidate = selected[0]
            candidate_index = list(self.candidate_radio_buttons.keys()).index(candidate)
            process_vote(candidate_index, voter_id)
            self.show_message("Success", "Vote submitted :)", "success")
        except Exception as e:
            self.show_message("Error", f"An error occurred: {str(e)}", "error")

    def show_message(self, title: str, message: str, category: str) -> None:
        """Show a simple message box."""
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)

        if category == "success":
            msg.setIcon(QMessageBox.Icon.Information)
        elif category == "error":
            msg.setIcon(QMessageBox.Icon.Critical)

        msg.exec()

    def open_admin_panel(self) -> None:
        """Open the admin page dialog."""
        admin_window = AdminPage(self)
        admin_window.exec()
