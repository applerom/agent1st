# One feature, the whole Why1st chain

Start at [PRD.md](PRD.md). Follow `FEAT-CAPACITY` through
[why-graph.xml](why-graph.xml) to the contracts in
[reading_list.py](reading_list.py). The contract names what changes together.
[test_capacity.py](test_capacity.py) checks the actual boundary behavior.

From the Agent1st repository root:

```sh
uv run --no-project python -B scripts/validate-why.py --repo-root docs/examples/reading-list --graph docs/examples/reading-list/why-graph.xml
uv run --no-project python -B -m unittest discover -s docs/examples/reading-list -v
```

With Python already installed, `python -B ...` works too; no dependencies are
required. To copy this example into another repo, copy these files and the
validator, then adjust the command paths.

## Change something meaningful

Suppose the reader now needs **25 books**. Change the PRD's capacity and acceptance
examples, the feature's intent and acceptance in the graph, the module contract,
the function default, and the boundary tests together. Keep the marker names:
the feature's identity survived the change.

Two different failures teach the boundary:

1. In a disposable copy, rename only the function's `START_METHOD_can_add_book`
   marker. The graph still points to the old marker: the validator exits 1.
2. Change `<` to `<=` in the function. The graph and markers still resolve:
   the validator passes, but the boundary tests fail.

Restore each change before trying the next. The repository regression suite
also exercises the broken-marker case on a temporary copy of this example.

**A valid coordinate is not a correct implementation.** The graph helps the
agent find the right work; contracts explain it; mechanical checks catch broken
references; behavior tests check the acceptance criteria. Reviewing whether the
requirement itself is right still belongs to the human-agent partnership.
