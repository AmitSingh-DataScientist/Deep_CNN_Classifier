# Data Ingestion Configuration Part

# Alternative to 'namedtuple'
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)  # this decorator make sure that it works like 'namedtuple'
class DataIngestionConfig:
    # class variables
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)    # this decorator make sure that it works like 'namedtuple'
class PrepareBaseModelConfig:
    # class variables
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
