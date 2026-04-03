from pathlib import Path
from .types import Chunk


def parse_repo(repo_path: Path) -> list[Chunk]:
    chunks = []
    for file_path in repo_path.rglob("*"):
        if file_path.is_file():
            with open(file_path, "r") as f:
                content = f.read()
                chunks.append(
                    Chunk(
                        id=str(file_path),
                        text=content,
                        metadata={
                            "path": str(file_path),
                            "language": file_path.suffix[1:],
                        },
                    )
                )
    return chunks
