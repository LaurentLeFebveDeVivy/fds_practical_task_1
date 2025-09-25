from config import DATA_DIR
import pandas as pd
import pathlib

# Returns any CSV in the assets/data directory as a pandas DF by simply specifying the name
# Example: df = DataLoader("data.csv").load()
class DataLoader:

    def __init__(self, file_name: str, dir: pathlib.Path=DATA_DIR) -> None:

        self.file_path = dir / file_name

        if not self.file_path.exists():
            raise FileNotFoundError(f"❌ File not found: {self.file_path}")

    def load(self) -> pd.DataFrame:

        return pd.read_csv(self.file_path)