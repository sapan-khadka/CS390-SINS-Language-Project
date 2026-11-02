# AI Use Statement — Part 5

## AI Tool Used

ChatGPT

## How AI Was Used

The group used ChatGPT to clarify the Part 5 requirements, divide responsibilities, plan nested environments, review function and string integration, diagnose parser indentation problems, develop test commands, resolve Git merge conflicts, and organize the final documentation. Group members implemented, reviewed, tested, corrected, and explained the submitted work.

## Components That Received AI Assistance

AI assistance was used while planning or reviewing:

- Parent-linked environments and local scope
- Function AST nodes, parsing, calls, and returns
- String parsing, escape sequences, and concatenation
- Integration and Git conflict-resolution steps
- Part 5 test planning
- EBNF, README, and submission organization

## Suggestion the Group Verified and Corrected

During string integration, an AI-generated suggestion discussed changing the condition for concatenation from `and` to `or`. The group verified that this change alone was insufficient in Python because adding a string directly to a number still raises a type error. The implementation was corrected to detect whether either operand is a string and then explicitly convert both operands with `str()` before concatenating them.

The group also rejected automatic “accept both changes” conflict resolution for the parser, interpreter, and AST files. Accepting both complete versions would have duplicated code. Instead, the group preserved the newer function implementation and manually integrated only the required string additions.

## Independent Verification

The group ran:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

All 32 automated tests passed. The group also ran five Part 5 programs covering function parameters and returns, scope shadowing, local variables, a zero-parameter function, strings, escape sequences, and concatenation. The observed outputs matched the expected results.

## What the Group Learned

AI suggestions must be checked against the current AST interfaces, parser rules, environment behavior, and Python runtime semantics. Small-looking edits can remove newer team contributions or introduce type errors. Reviewing diffs and rerunning both unit tests and complete programs after integration were essential.
