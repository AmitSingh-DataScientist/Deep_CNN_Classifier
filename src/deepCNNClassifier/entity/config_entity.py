## Data Ingestion Configuration Part

# Alternative to 'namedtuple'
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)    # this decorator make sure that it works like 'namedtuple'
class DataIngestionConfig:
    # class variables
    root_dir : Path
    source_URL : str
    local_data_file :Path
    unzip_dir : Path