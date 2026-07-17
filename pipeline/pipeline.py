from pipeline.parser import ResumeParser
from pipeline.llm import ATSLLM

class ATSPipeline:
    def __init__(self):
        self.parser = ResumeParser()
        self.llm = ATSLLM()

    def analyze(self, resume_path: str, job_description: str):
        # Step 1: Parse the full resume (PDF/Docx)
        resume_text = self.parser.parse(resume_path)

        # Step 2: Direct full-text LLM evaluation (Ultra-fast & No Network issues!)
        response = self.llm.analyze(resume_text, job_description)
        return response