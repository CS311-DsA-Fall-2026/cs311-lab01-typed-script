"""
Lab 1: The Typed Script -- verification suite.

Run: python test_container.py
Prints the Success Token only if every check below passes.
"""

import base64
import hashlib
import sys

from container import TypedContainer

ASSIGNMENT_ID = "LAB01"


def get_student_id() -> str:
    """Prompt for the student's USI username; baked into the Success Token
    so a copied/shared token decodes to someone else's name, not yours."""
    student_id = input("Enter your USI username (e.g. cwill): ").strip()
    while not student_id:
        student_id = input("Username cannot be blank. Enter your USI username: ").strip()
    return student_id


def generate_token(assignment_id: str, student_id: str) -> str:
    digest = hashlib.sha256(f"CS311-{assignment_id}-{student_id}-VERIFIED".encode()).hexdigest()[:16]
    raw = f"CS311|{assignment_id}|{student_id}|PASS|{digest}"
    return base64.b64encode(raw.encode()).decode()


def print_success_banner(assignment_id: str) -> None:
    student_id = get_student_id()
    token = generate_token(assignment_id, student_id)
    print("\n" + "=" * 60)
    print(f"  ALL CHECKS PASSED -- {assignment_id}")
    print(f"  STUDENT: {student_id}")
    print("  SUCCESS TOKEN (paste this into Blackboard):")
    print(f"  {token}")
    print("=" * 60 + "\n")


def check(label: str, condition: bool, failures: list) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    if not condition:
        failures.append(label)


def main() -> int:
    failures: list = []
    c: TypedContainer = TypedContainer()

    print("Running TypedContainer verification suite...\n")

    # Basic set/get
    c.set("alpha", 1)
    check("set/get round-trip", c.get("alpha") == 1, failures)

    # Overwrite existing key
    c.set("alpha", 2)
    check("overwrite existing key", c.get("alpha") == 2, failures)

    # __contains__
    check("'alpha' in container is True", "alpha" in c, failures)
    check("'missing' in container is False", "missing" not in c, failures)

    # __len__
    c.set("beta", 3)
    check("__len__ reflects two entries", len(c) == 2, failures)

    # Non-str key on set() must raise TypeError
    try:
        c.set(123, "bad")  # type: ignore[arg-type]
        check("set() rejects non-str key", False, failures)
    except TypeError:
        check("set() rejects non-str key", True, failures)
    except Exception:
        check("set() rejects non-str key (wrong exception type)", False, failures)

    # Non-str key on get() must raise TypeError
    try:
        c.get(456)  # type: ignore[arg-type]
        check("get() rejects non-str key", False, failures)
    except TypeError:
        check("get() rejects non-str key", True, failures)
    except Exception:
        check("get() rejects non-str key (wrong exception type)", False, failures)

    # get() on a missing key should not silently return None
    try:
        c.get("nope")
        check("get() on missing key does not return silently", False, failures)
    except (KeyError, TypeError):
        check("get() on missing key raises instead of returning None", True, failures)

    print()
    if failures:
        print(f"{len(failures)} check(s) failed. No token issued.")
        return 1

    print_success_banner(ASSIGNMENT_ID)
    return 0


if __name__ == "__main__":
    sys.exit(main())
