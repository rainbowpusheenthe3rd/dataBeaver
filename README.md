# metabeaver 🦫

**Beaverish about data.** A Python glue library and computer-science reference — data
structures, algorithms, worked interview answers, cloud data-engineering helpers, and a
few quality-of-life utilities — wrapped in a codebase that, at times, is actually fun to
read. (Beavers really do have orange teeth, and all mushrooms are edible at least once.)

metabeaver began life damming together code reused across projects and an algorithmic
reference point. It has grown into a resource to **learn** computer science and Python,
and to **stop rebuilding the wheel** — theory next to practical, runnable code.

## Install

```bash
pip install -e .            # core (numpy, pandas)
pip install -e ".[gcp]"     # + Google BigQuery helpers
pip install -e ".[graph]"   # + Neo4j helpers
pip install -e ".[dev]"     # + pytest, ruff
```

## What's inside

| Area | Where |
|---|---|
| **Data structures** | `metabeaver/DataStructures/` — BST, linked list, FIFO/FILO queues, nodes |
| **Sorting** | `metabeaver/SortingAlgorithms/` — merge, quick, heap, insertion, timsort |
| **Searching** | `metabeaver/SearchAlgorithms/` — binary search, BFS/DFS over trees & graphs |
| **Graph algorithms** | `metabeaver/GraphAlgorithms/` — Dijkstra, Bellman-Ford, DFS, Monte-Carlo tree search |
| **Interview answers** | `metabeaver/InterviewQuestions/` — two-sum, best-time-to-sell, stacks, … (space/time notes) |
| **Binary & maths** | `metabeaver/Binary/`, `metabeaver/MathematicalOperations/`, `metabeaver/SetTheory/` |
| **Caching** | `metabeaver/Caching/` — least-recently-used cache |
| **Text validation** | `metabeaver/TextValidation/` — palindromes, closure/bracket checking |
| **Cloud data-eng** | `metabeaver/GoogleCloudPlatform/` (BigQuery), `metabeaver/DatabaseFunctionality/` (SQL, SQLite, Neo4j) |
| **Ops & meta** | `metabeaver/OperationBeaver/` (Docker, Actions, logging), `metabeaver/MetaProgramming/`, `metabeaver/Formatting/` |
| **Whimsy** | `metabeaver/BeaverTown/`, and a poem in `main.py` |

Design philosophy (standard-library-first, keep life simple): see
[`metabeaver/DESIGN_PHILOSOPHY.md`](metabeaver/DESIGN_PHILOSOPHY.md).

## Develop

```bash
pip install -e ".[dev]"
ruff check .        # lint (real errors + import order; tightening over time)
pytest              # tests in tests/
```

CI runs ruff + pytest on every push (`.github/workflows/ci.yml`).

> **Note:** cloud helpers load credentials from files/env — never commit real
> `credentials.json` / service-account keys (they're git-ignored). The Neo4j example
> uses a localhost placeholder password; swap in your own.

## Roadmap

metabeaver is being reborn as the grounded-examples half of a learning system (the
spiritual successor to its "CS reference" origins): syllabus + spaced-repetition
flashcards + takeaway problems over these very modules.

## License

MIT — see [`LICENSE`](LICENSE).
