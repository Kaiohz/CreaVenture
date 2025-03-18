from dataclasses import dataclass
from typing import Optional


@dataclass
class BrowserUseResponse:
    markdown_content: str
    file_path: Optional[str]
