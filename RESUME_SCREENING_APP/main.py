from fastapi import FastAPI, UploadFile
from parsepdf import parse_pdf
from agents.resume_extractor import analyze_resume
from agents.jd_extractor import analyze_jd
from agents.candidate_evaluation_agent import evaluate_candidate
import json

app = FastAPI()

@app.post("/screening/")
async def screening(resume: UploadFile):
    resume_text = parse_pdf(resume.file)
    resume_details_extracted = analyze_resume(resume_text)
    jd_text = ""
    with open("resources/job_description.pdf", "rb") as file:
        jd_text = parse_pdf(file)

    jd_extracted = analyze_jd(jd_text)
    evaluation_result = evaluate_candidate(json.dumps(resume_details_extracted), json.dumps(jd_extracted))


    return resume_details_extracted
    