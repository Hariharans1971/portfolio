# Hariharan S. — Python, Backend & AI/ML Portfolio

[![Portfolio validation](https://github.com/Hariharans1971/portfolio/actions/workflows/pages.yml/badge.svg)](https://github.com/Hariharans1971/portfolio/actions/workflows/pages.yml) [![Live-site checks](https://github.com/Hariharans1971/portfolio/actions/workflows/verify-live-site.yml/badge.svg)](https://github.com/Hariharans1971/portfolio/actions/workflows/verify-live-site.yml) [![History secret audit](https://github.com/Hariharans1971/portfolio/actions/workflows/account-secret-audit.yml/badge.svg)](https://github.com/Hariharans1971/portfolio/actions/workflows/account-secret-audit.yml)

A responsive static portfolio built with HTML, CSS, and JavaScript. The page highlights selected work with direct access to source, architecture notes, setup instructions, and CI evidence.

**Live sites:** [Vercel production](https://portfolio1-tau-sandy.vercel.app/) · [GitHub Pages](https://hariharans1971.github.io/portfolio/)  
**Source code:** [GitHub repository](https://github.com/Hariharans1971/portfolio) · [CI and deployments](https://github.com/Hariharans1971/portfolio/actions)

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

GitHub Actions runs the static validator on pushes to `main`. The publishing workflow detects the repository's Pages source: if it is GitHub Actions, it uses the official Pages artifact deployment; if it is branch-based, it updates `gh-pages` with only `index.html` and `.nojekyll`. The live-site smoke test then checks both public URLs for HTTP 200 and key portfolio content.

- [Publish workflow](https://github.com/Hariharans1971/portfolio/actions/workflows/pages.yml)
- [Live-site smoke tests](https://github.com/Hariharans1971/portfolio/actions/workflows/verify-live-site.yml)
- [GitHub Pages URL](https://hariharans1971.github.io/portfolio/)
- [Vercel production URL](https://portfolio1-tau-sandy.vercel.app/)

## Engineering and accessibility notes

- The document-analysis project links include architecture, setup, and CI evidence, not only source code.
- The page includes a keyboard skip link, visible keyboard focus, a mobile/coarse-pointer fallback, and reduced-motion support.
- Certificate claims are limited to AZ-900; other credentials in the page are presented as project work rather than certifications.
- The document-analysis retrieval benchmark is a six-query synthetic smoke baseline, not a claim of production accuracy.
- Do not commit API keys, credentials, private documents, or generated virtual environments.

## Stack

HTML5 · CSS3 · JavaScript · Google Fonts
