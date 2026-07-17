from pathlib import Path
import fitz  # PyMuPDF
from docx import Document

class ResumeParser:
    SUPPORTED_EXTENSIONS = {".pdf", ".docx"}

    def parse(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        extension = path.suffix.lower()
        if extension not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file format: {extension}")

        if extension == ".pdf":
            return self._parse_pdf(path)
        return self._parse_docx(path)

    def _parse_pdf(self, path: Path) -> str:
        document = fitz.open(path)
        pages = []
        for page in document:
            pages.append(page.get_text())
        document.close()
        return "\n".join(pages).strip()

    def _parse_docx(self, path: Path) -> str:
        document = Document(path)
        paragraphs = [para.text for para in document.paragraphs if para.text.strip()]
        return "\n".join(paragraphs).strip()