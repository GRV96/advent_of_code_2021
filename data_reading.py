from pathlib import Path
from typing import Generator


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"


def read_file_lines(file_path: Path) -> Generator[str, None, None]:
	with file_path.open(encoding=_ENCODING_UTF8, mode=_MODE_R) as data_file:
		for line in data_file:
			yield line.strip()
