# START_MODULE_CAPACITY:
# FILE: reading_list.py
# VERSION: 2026-09-05
# PURPOSE: Keep all callers on the same reading-list capacity policy.
# PRD_REF: PRD.md#CAPACITY
# WHY_REF: why-graph.xml FEAT-CAPACITY
# SCOPE: One pure capacity decision; no storage or UI.
# INVARIANTS: Default limit 20; adding requires count < limit; negatives rejected.
# LINKS: A policy change also updates PRD, feature intent/acceptance, and test_capacity.py.

# START_METHOD_can_add_book:
# PURPOSE: Decide whether one more book fits.
# INPUTS: Non-negative integer current_count and limit.
# OUTPUTS: True below the limit, False at or above it; ValueError for negatives.
# LINKS: PRD.md#CAPACITY; why-graph.xml FEAT-CAPACITY.
def can_add_book(current_count: int, limit: int = 20) -> bool:
    """Return whether the list has room; reject negative counts or limits."""
    if current_count < 0 or limit < 0:
        raise ValueError("current_count and limit must be non-negative")
    return current_count < limit
# :END_METHOD_can_add_book

# :END_MODULE_CAPACITY
