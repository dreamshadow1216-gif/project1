import sys
from PyQt6.QtWidgets import QApplication
from gui import VotingApp

def main() -> None:
    """ main function"""
    try:
        app = QApplication(sys.argv)
        main_window = VotingApp()
        main_window.setWindowTitle("Voting Application")
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error during application initialization: {e}")
        sys.exit(1)

if __name__ == "__main__":

    main()
