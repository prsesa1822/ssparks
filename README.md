# AI and Data Analysis Portfolio

This project generates a compact visual portfolio about AI and data analysis work. It includes:

- A static portfolio homepage for GitHub Pages
- Sarah Sparks' resume PDF
- A compressed presentation PDF
- A PDF report built with ReportLab
- A set of presentation-style PNG images built with Pillow
- Source data and chart logic embedded in the Python scripts

## Files

- `index.html` is the portfolio homepage
- `assets/sarah_sparks_resume.pdf` is the resume PDF
- `assets/Presentation_Compressed.pdf` is the presentation PDF
- `build_ai_data_analysis_pdf.py` creates `Ai and data analysis.pdf`
- `export_ai_data_analysis_images.py` creates images in `Ai and data analysis images/`
- `Ai and data analysis images/` contains the exported portfolio images

## GitHub Pages

After pushing this repository to GitHub, enable GitHub Pages from the repository settings and publish from the `main` branch root. The homepage is `index.html`.

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Generate Outputs

Create the PDF:

```bash
python build_ai_data_analysis_pdf.py
```

Create the image set:

```bash
python export_ai_data_analysis_images.py
```

## Notes

The scripts use local Windows font paths for Arial:

- `C:/Windows/Fonts/arial.ttf`
- `C:/Windows/Fonts/arialbd.ttf`

If you run this on another operating system, update the font paths in `export_ai_data_analysis_images.py`.
