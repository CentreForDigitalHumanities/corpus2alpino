from typing import Optional

from corpus2alpino.abstracts import Target
from corpus2alpino.models import Document


class MemoryTarget(Target):
    """
    Combine output in memory.
    """

    buffer = ""

    def write(
        self,
        document: Document,
        content: str,
        filename: Optional[str] = None,
        suffix: Optional[str] = None,
    ):
        """
        Write all lines to memory buffer.
        """
        self.buffer += content

    def write_merged(self, content: str) -> None:
        """Write all lines to memory buffer.

        Args:
            content (str): content to write
        """
        self.buffer += content

    def flush(self):
        try:
            return self.buffer
        finally:
            self.buffer = ""

    def close(self):
        return
