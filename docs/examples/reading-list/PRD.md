# Reading-list capacity — Why1st example

One tiny feature makes the full chain visible. This is a teaching fixture.

<!-- PRD_ANCHOR: CAPACITY -->

- **UC-ADD-BOOK:** A reader adds a book while the list has room.
- **FEAT-CAPACITY:** A list holds at most **20 books** by default. A caller may
  supply another limit. Adding is allowed only when `current_count < limit`.
- Counts and limits are non-negative integers. Negative values raise `ValueError`.
- Acceptance: 19/20 allows adding; 20/20 and 21/20 reject it; a zero limit rejects
  adding to an empty list. A custom limit uses the same boundary.

No persistence, UI, accounts, or recommendation engine belongs to this feature.
