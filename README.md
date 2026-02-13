# Smart Code Reviewer

An AI-ready assistant that reviews code for **readability**, **structure**, and **maintainability** before human review. Run it on files or directories to get actionable feedback.

## Features

- **Readability**: naming, line length, comment ratio, clarity hints
- **Structure**: function/module length, nesting depth, separation of concerns
- **Maintainability**: cyclomatic complexity, maintainability index, duplication cues

Supported languages: **Python** (full analysis). Other languages get basic line-based metrics.

## Install

```bash
pip install -r requirements.txt
```

## Usage

Review current directory (default):

```bash
python -m smart_code_reviewer
```

Review a file or directory:

```bash
python -m smart_code_reviewer -t path/to/file.py
python -m smart_code_reviewer -t path/to/project/
```

Review from stdin (paste code, then Ctrl+D):

```bash
python -m smart_code_reviewer -t -
```

Output formats: default (rich console), or `--json` for machine-readable report.

**Web UI** – paste code and get instant feedback:

```bash
python -m smart_code_reviewer web
# Open http://127.0.0.1:8000
```

## Example output

```
📁 example.py
  Readability   ████████░░  Good – consider shorter lines in 2 places
  Structure     █████████░  Good – 1 long function (45 lines)
  Maintainability ████████░░  Good – 2 blocks with elevated complexity
```
## License

MIT
