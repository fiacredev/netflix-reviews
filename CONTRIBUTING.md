# Contributing to the Netflix reviews analysis

Thanks for taking the time to contribute. This project is a data analysis
repository built around a single Jupyter notebook plus a small set of helper
scripts, so most contributions fall into one of three groups.

## Reporting an issue

Open an issue and include:

- the operating system and Python version used,
- the command or notebook cell that failed,
- the full traceback, and
- what you expected to happen instead.

## Suggesting an improvement

Ideas that keep the analysis reproducible are welcome: new visualisations,
additional stopword lists, alternative topic counts, or documentation that
clarifies a step of the pipeline.

## Working on the code

1. Fork the repository and create a branch named after the change.
2. Create a virtual environment and install the dependencies.

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   make setup
   ```

3. Keep the notebook deterministic: fix random seeds and avoid hidden state
   between cells.
4. Run the checks before opening a pull request.

   ```bash
   python -m unittest discover -s tests -v
   make check
   ```

5. Write commit messages in the imperative mood, for example
   `feat(notebook): add sentiment distribution chart`.
6. Open a pull request describing the change, the motivation and the impact
   on the results.

## Notebook conventions

- Keep the analysis linear and readable from top to bottom.
- Clear all outputs before committing a notebook so that the file stays
  reviewable in a diff.
- Add explanatory markdown cells above any non-obvious code cell.
- Never edit the source dataset in place; all cleaning happens in code.

## Code style

- Follow PEP 8 with a 100 character line limit.
- Prefer small, testable functions in `scripts/` over duplicated notebook logic.
- Document every public function with a docstring.
