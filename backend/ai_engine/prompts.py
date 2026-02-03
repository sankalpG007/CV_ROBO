def resume_summary_prompt(resume_data: dict) -> str:
    return f"""
You are a professional resume writer.

Based on the following resume details, write a concise,
professional resume summary (3–4 lines).

Resume Data:
{resume_data}

Rules:
- Use strong action words
- Be ATS-friendly
- Do NOT add fake experience
"""
