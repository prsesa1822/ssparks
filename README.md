# AI and Data Analysis Portfolio

Dark, tech-forward static portfolio site for Sarah Sparks. The live site is designed for GitHub Pages and includes:

- A self-contained portfolio homepage
- A curated web resume page
- A curated data case study page based on the supplied presentation
- An AI and data analysis snapshot section
- An optional extraction helper for local PDFs

## Hosted Files

- `index.html` is the portfolio homepage
- `resume.html` is the curated web resume
- `presentation.html` is the curated data case study
- `generate_pdf_pages.py` is an optional helper for extracting local PDFs into starter HTML
- `requirements.txt` lists Python dependencies

## Local Asset Notes

The original PDFs and generated image/PDF report are kept locally in the working folder. They can be added later with Git or another binary upload route:

- `assets/sarah_sparks_resume.pdf`
- `assets/Presentation_Compressed.pdf`
- `Ai and data analysis.pdf`
- `Ai and data analysis images/`

## GitHub Pages

GitHub Pages is configured to publish from the `main` branch root. The homepage is `index.html`.

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Optional PDF extraction helper:

```bash
python generate_pdf_pages.py
```
