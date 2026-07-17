import json
import re
from groq import Groq
from config import Config

# Premium context-aware structured prompt
ATS_PROMPT = """
You are an expert ATS (Applicant Tracking System) Resume Analyzer and a Senior Technical Recruiter.
Your task is to critically analyze the provided Resume Text against the given Job Description.

Provide a highly objective, rigorous, and constructive evaluation.

Job Description:
{job_description}

Resume Text:
{resume_text}

Analyze the alignment based on the following professional criteria:
1. Keyword Match: Check for core technical stack, tools, frameworks, and soft skills mentioned in the Job Description.
2. Experience Relevance: Assess if the candidate's career progression, project roles, and seniority levels align with the requirements.
3. Action-Oriented Impact: Look for bullet points with quantifiable metrics (e.g., numbers, percentages, performance gains) and strong action verbs.
4. Formatting & Readability: Identify potential ATS-parsing bottlenecks (e.g., missing section headers, bad structure).

Return ONLY a single, valid JSON object matching the exact schema below. Do not include any introductory or concluding conversational text, and do not wrap the response in markdown blocks (e.g., do not use ```json).

Expected JSON Schema Format:
{{
  "ats_score": 0,
  "match_percentage": 0,
  "matched_skills": [],
  "missing_skills": [],
  "strengths": [],
  "weaknesses": [],
  "improvements": [],
  "summary": ""
}}

Rules for JSON values:
- "ats_score": An integer (0-100) representing structural quality, readability, and ATS-compliance of the resume.
- "match_percentage": An integer (0-100) representing direct keyword, experience, and skill alignment with the Job Description.
- "matched_skills": A list of technical and soft skills present in both the JD and the resume.
- "missing_skills": A list of critical skills or tools requested in the JD but absent or weak in the resume.
- "strengths": A list of 3-4 specific, high-value strengths found in the resume (e.g., strong use of metrics, solid tech stack).
- "weaknesses": A list of 3-4 specific weaknesses (e.g., lack of quantifiable impact in certain roles, generic statements, missing key framework).
- "improvements": A list of 3-4 highly actionable recommendations, specifying exactly where and how the candidate should rewrite things (e.g., "Add performance metrics to your FastAPI backend bullet points under the Software Engineer role").
- "summary": A professional 3-4 sentence executive summary detailing why this resume is or isn't a strong fit, and its overall hiring potential.
"""

class ATSLLM:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.LLM_MODEL

    def analyze(self, resume_text: str, job_description: str):
        prompt = ATS_PROMPT.format(
            job_description=job_description,
            resume_text=resume_text
        )

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.1,  # Low temperature for highly consistent structured JSON outputs
            response_format={"type": "json_object"}, 
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content.strip()
        
        # Clean potential markdown
        if output.startswith("```"):
            output = re.sub(r"^```(?:json)?\s*", "", output)
            output = re.sub(r"\s*```$", "", output)

        return json.loads(output)