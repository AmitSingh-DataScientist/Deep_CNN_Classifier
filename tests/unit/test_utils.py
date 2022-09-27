import pytest
from deepCNNClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError

class Test_read_yaml:
    yaml_files = [
        "tests/data/empty.yaml",
        "tests/data/demo.yaml"
    ]

    # start testing with '_' as and when you start 
    def test_read_yaml_empty(self):
        with pytest.raises(ValueError): 
            read_yaml(Path(self.yaml_files[0]))

    # checking for the output
    def test_read_yaml_return_type(self):
        response = read_yaml(Path(self.yaml_files[-1]))
        assert isinstance(response, ConfigBox)

    # In case of failure of testing 

    @pytest.mark.parametrize("path_to_yaml", yaml_files) # to pass multiple parameters for testing
    def test_read_yaml_bad_type(self,path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)

# yaml_files = [
#     "tests\data\empty.yaml",
#     "tests\data\demo.yaml"
# ]

# def test_read_yaml_empty():
#     with pytest.raises(ValueError):
#         read_yaml(Path(yaml_files[0]))