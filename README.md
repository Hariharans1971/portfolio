# Hariharan S. — Python, Backend & AI/ML Portfolio

A responsive static portfolio built with HTML, CSS, and JavaScript. The page highlights selected work with direct access to source, architecture notes, setup instructions, and CI evidence.

**Portfolio deployment:** [Open the Vercel site](https://portfolio1-tau-sandy.vercel.app/)  
**Source code:** [GitHub repository](https://github.com/Hariharans1971/portfolio)

## Featured projects

- **Document Analysis + RAG:** [Repository](https://github.com/Hariharans1971/document_analysis) · [Architecture and trade-offs](https://github.com/Hariharans1971/document_analysis/blob/main/docs/ARCHITECTURE.md) · [Setup guide](https://github.com/Hariharans1971/document_analysis/blob/main/RAG_GUIDE.md) · [CI checks](https://github.com/Hariharans1971/document_analysis/actions)
- **ClinicDesk appointment workflow demo:** [Repository](https://github.com/Hariharans1971/Clinic) · [CI checks](https://github.com/Hariharans1971/Clinic/actions)
- **Inventory Management System:** [Repository](https://github.com/Hariharans1971/inventory-management-system)
- **Student Performance Prediction:** [Repository](https://github.com/Hariharans1971/Student-Performance-ML-Project)

## Preview locally

Requires Python 3 only for the optional local server; there is no build step.

```bash
git clone https://github.com/Hariharans1971/portfolio.git
cd portfolio
python -m http.server 8000
```

Open http://localhost:8000.

## Validation and deployment

A dependency-free static validator checks the page title and metadata, required sections, duplicate IDs, in-page links, safe new-tab links, accessibility hooks, and project evidence links:

```bash
python scripts/validate_portfolio.py
```

GitHub Actions runs this validator on pushes to `main`. To publish with GitHub Pages, open **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**. Then open the **Actions** tab, choose **Publish portfolio to GitHub Pages**, and run the workflow once. The workflow checks the Pages source and skips deployment until it is configured; future pushes to `main` deploy the validated `index.html` automatically.

Expected GitHub Pages URL: https://hariharans1971.github.io/portfolio/

## Engineering and accessibility notes

- The document-analysis project links include architecture, setup, and CI evidence, not only source code.
- The page includes a keyboard skip link, visible keyboard focus, a mobile/coarse-pointer fallback, and reduced-motion support.
- Certificate claims are limited to AZ-900; other credentials in the page are presented as project work rather than certifications.
- The document-analysis retrieval benchmark is a six-query synthetic smoke baseline, not a claim of production accuracy.
- Do not commit API keys, credentials, private documents, or generated virtual environments.

## Stack

HTML5 · CSS3 · JavaScript · Google Fonts
