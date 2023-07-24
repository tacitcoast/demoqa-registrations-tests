from pathlib import Path
import tests


def path(file_name):
    a = tests.__file__
    return str(Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute())
