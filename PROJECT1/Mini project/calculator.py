"""
╔══════════════════════════════════════════╗
║         CALCX — Python Calculator        ║
║   Basic Ops · Stats · Percentage         ║
╚══════════════════════════════════════════╝
"""

# ── Imports ────────────────────────────────
from statistics import mean, median, mode, multimode


# ── Helpers ────────────────────────────────
def get_float(prompt: str) -> float:
    """Prompt user and cast input to float (type casting)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ✗ Invalid number. Please try again.")


def get_numbers(prompt: str) -> list[float]:
    """Prompt for a comma-separated list of numbers (type casting each)."""
    while True:
        raw = input(prompt)
        try:
            nums = [float(x.strip()) for x in raw.split(",") if x.strip()]
            if not nums:
                print("  ✗ Please enter at least one number.")
                continue
            return nums
        except ValueError:
            print("  ✗ Could not parse one or more values. Use commas: 1, 2, 3")


def divider(char="─", width=44):
    print(char * width)


def header(title: str):
    divider("═")
    print(f"  {title}")
    divider("═")


def section(title: str):
    print(f"\n  ── {title} ──")


# ── Modes ──────────────────────────────────

def basic_calculator():
    """Perform +, -, *, / on two numbers."""
    header("BASIC CALCULATOR  ( + - * / )")

    a = get_float("  Enter first number  : ")
    b = get_float("  Enter second number : ")

    ops = {"+": a + b, "-": a - b, "*": a * b}

    # Division needs a zero-check
    if b != 0:
        ops["/"] = a / b

    section("Results")
    print(f"  {a} + {b} = {a + b}")
    print(f"  {a} - {b} = {a - b}")
    print(f"  {a} × {b} = {a * b}")

    if b != 0:
        print(f"  {a} ÷ {b} = {a / b:.6g}")
    else:
        print(f"  {a} ÷ {b} = undefined  (division by zero)")

    # Modulo / remainder
    if b != 0:
        print(f"  {a} % {b} = {a % b:.6g}  (remainder)")
    divider()


def stats_calculator():
    """Mean, median, mode, average for a list of numbers."""
    header("STATISTICS CALCULATOR")

    nums = get_numbers("  Enter numbers (comma-separated): ")
    n = len(nums)
    total = sum(nums)
    avg = total / n                  # manually computed average
    med = median(nums)               # built-in median

    # Mode — handle multi-mode gracefully
    modes = multimode(nums)
    mode_str = ", ".join(str(m) for m in modes) if len(modes) < n else "No mode (all values unique)"

    sorted_nums = sorted(nums)
    rng = sorted_nums[-1] - sorted_nums[0]

    # Variance & std dev (population)
    variance = sum((x - avg) ** 2 for x in nums) / n
    std_dev = variance ** 0.5

    section("Your Numbers")
    print(f"  {nums}")

    section("Statistics")
    print(f"  Count      : {n}")
    print(f"  Sum        : {total:.6g}")
    print(f"  Mean / Avg : {avg:.6g}")
    print(f"  Median     : {med:.6g}")
    print(f"  Mode       : {mode_str}")
    print(f"  Min        : {sorted_nums[0]:.6g}")
    print(f"  Max        : {sorted_nums[-1]:.6g}")
    print(f"  Range      : {rng:.6g}")
    print(f"  Variance   : {variance:.6g}")
    print(f"  Std Dev    : {std_dev:.6g}")
    divider()


def percent_calculator():
    """Three percentage operations."""
    header("PERCENTAGE CALCULATOR")
    print("  1 · X% of Y")
    print("  2 · Percentage change (from → to)")
    print("  3 · X is what % of Y?")

    choice = input("\n  Choose (1/2/3): ").strip()

    if choice == "1":
        section("X% of Y")
        pct = get_float("  Percentage  : ")
        of  = get_float("  Of number   : ")
        result = (pct / 100) * of
        print(f"\n  {pct}% of {of} = {result:.6g}")

    elif choice == "2":
        section("Percentage Change")
        frm = get_float("  From : ")
        to   = get_float("  To   : ")
        if frm == 0:
            print("  ✗ 'From' cannot be zero for percentage change.")
        else:
            change = ((to - frm) / abs(frm)) * 100
            direction = "increase" if change >= 0 else "decrease"
            print(f"\n  {frm} → {to} is a {abs(change):.4g}% {direction}")

    elif choice == "3":
        section("X is what % of Y?")
        part  = get_float("  X (part)  : ")
        whole = get_float("  Y (whole) : ")
        if whole == 0:
            print("  ✗ Whole cannot be zero.")
        else:
            result = (part / whole) * 100
            print(f"\n  {part} is {result:.6g}% of {whole}")

    else:
        print("  ✗ Invalid choice.")

    divider()


# ── Main Menu ──────────────────────────────

def main():
    MENU = {
        "1": ("Basic Calculator  ( + - * / % )", basic_calculator),
        "2": ("Statistics  ( mean · median · mode · avg )", stats_calculator),
        "3": ("Percentage  ( % of · % change · X is Y% )", percent_calculator),
        "q": ("Quit", None),
    }

    while True:
        header("CALCX — MAIN MENU")
        for key, (label, _) in MENU.items():
            print(f"  [{key}]  {label}")
        divider()

        choice = input("  Choose an option: ").strip().lower()

        if choice == "q":
            print("\n  Bye! 👋\n")
            break
        elif choice in MENU and MENU[choice][1]:
            print()
            MENU[choice][1]()
            input("\n  Press Enter to return to menu...")
        else:
            print("  ✗ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
