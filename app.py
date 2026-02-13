# Vercel serverless entrypoint
import sys
from pathlib import Path

# Ensure project root is on path when Vercel runs this file
_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from smart_code_reviewer.app import app
