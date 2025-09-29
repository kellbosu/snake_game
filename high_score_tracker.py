import json
from pathlib import Path


class HighScoreTracker:
    """Persist and retrieve the game's high score to/from a JSON file."""
    def __init__(self, path: str = "high_score.json"):
        self.path = Path(path)
        self.high_score = 0
        self._load()

    def _load(self):
        try:
            if self.path.exists():
                data = json.loads(self.path.read_text())
                self.high_score = int(data.get("high_score",0))
            else:
                self.save()
        except Exception:
            self.high_score = 0
            self.save()

    def get(self):
        return int(self.high_score)
    
    def save(self):
        self.path.write_text(json.dumps({"high_score": int(self.high_score)}, indent=2))

    def maybe_update(self, score: int) -> bool:
        score = int(score)
        if score > self.high_score:
            self.high_score = score
            self.save()
            return True
        return False

    