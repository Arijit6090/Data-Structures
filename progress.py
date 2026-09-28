# This file is for personal usage and tracking progress. If you are using the same folder structures then you can use this code for your progress tracking too :)

from pathlib import Path
from datetime import datetime


# =========================================================
# CONFIGURATION
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent

PROBLEMS_DIR = ROOT_DIR / "DSA-Problems"
TRACKER_FILE = Path(__file__).resolve()


# =========================================================
# UTILITY FUNCTIONS
# =========================================================

def count_python_files(folder: Path) -> int:
    """
    Recursively count all Python files inside a folder.
    Ignores __pycache__ directories.
    """
    if not folder.exists():
        return 0

    return sum(
        1
        for file in folder.rglob("*.py")
        if file.is_file() and "__pycache__" not in file.parts
    )


def count_problem_files(folder_name: str) -> int:
    """
    Count Python problem files inside a difficulty folder.
    """
    folder = PROBLEMS_DIR / folder_name
    return count_python_files(folder)


def count_concepts() -> int:
    """
    Count Python files anywhere inside the DSA folder,
    except files belonging to DSA-Problems and this tracker.

    This means:
    - DSA-Concepts/*.py -> counted
    - Future folders/*.py -> counted automatically
    - DSA-Problems/*.py -> NOT counted as concepts
    - progress.py -> NOT counted
    """
    count = 0

    for file in ROOT_DIR.rglob("*.py"):
        if not file.is_file():
            continue

        # Ignore __pycache__
        if "__pycache__" in file.parts:
            continue

        # Ignore DSA-Problems
        try:
            file.relative_to(PROBLEMS_DIR)
            continue
        except ValueError:
            pass

        # Ignore progress.py itself
        if file.resolve() == TRACKER_FILE:
            continue

        count += 1

    return count


def progress_bar(current: int, total: int, size: int = 25) -> str:
    """
    Create a simple terminal progress bar.
    """
    if total == 0:
        percentage = 0
    else:
        percentage = (current / total) * 100

    filled = int((percentage / 100) * size)
    empty = size - filled

    return f"[{'█' * filled}{'░' * empty}] {percentage:.1f}%"


# =========================================================
# PROBLEM STATISTICS
# =========================================================

easy = count_problem_files("Easy")
medium = count_problem_files("Medium")
hard = count_problem_files("Hard")
not_solved = count_problem_files("Not Solved")

total_questions = easy + medium + hard + not_solved
solved_questions = easy + medium + hard


# =========================================================
# CONCEPT STATISTICS
# =========================================================

total_concepts = count_concepts()


# =========================================================
# DISPLAY
# =========================================================

print()
print("=" * 60)
print("                 DSA PROGRESS")
print("=" * 60)

print(f"Last Updated : {datetime.now().strftime('%d %B %Y, %I:%M %p')}")

print()
print("PROBLEM PROGRESS")
print("-" * 60)

print(f"Easy         : {easy}")
print(f"Medium       : {medium}")
print(f"Hard         : {hard}")
print(f"Not Solved   : {not_solved}")
print(f"Total        : {total_questions}")
print(f"Solved       : {solved_questions}")

print()

print(
    "Solved Progress : "
    + progress_bar(solved_questions, total_questions)
)

print()
print("DIFFICULTY BREAKDOWN")
print("-" * 60)

print(
    f"Easy         : {easy:3}  "
    + progress_bar(easy, total_questions, 20)
)

print(
    f"Medium       : {medium:3}  "
    + progress_bar(medium, total_questions, 20)
)

print(
    f"Hard         : {hard:3}  "
    + progress_bar(hard, total_questions, 20)
)

print()
print("CONCEPT PROGRESS")
print("-" * 60)

print(f"Concept Files : {total_concepts}")

print()
print("=" * 60)
print("Keep learning. Keep solving. Keep improving.")
print("=" * 60)
print()

# This file should show something like this
# ============================================================
#                  DSA PROGRESS
# ============================================================
# Last Updated : 28 September 2026, 12:15 PM

# PROBLEM PROGRESS
# ------------------------------------------------------------
# Easy         : 15
# Medium       : 5
# Hard         : 0
# Not Solved   : 3
# Total        : 23
# Solved       : 20

# Solved Progress : [█████████████████████░░░░] 87.0%

# DIFFICULTY BREAKDOWN
# ------------------------------------------------------------
# Easy         :  15  [████████████████░░░░] 65.2%
# Medium       :   5  [████░░░░░░░░░░░░░░░░] 21.7%
# Hard         :   0  [░░░░░░░░░░░░░░░░░░░░] 0.0%

# CONCEPT PROGRESS
# ------------------------------------------------------------
# Concept Files : 12

# ============================================================
# Keep learning. Keep solving. Keep improving.
# ============================================================