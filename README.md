# Research Handbook - Long-term Literature Review

![Build Status](https://img.shields.io/badge/Status-Active-success)
![LaTeX](https://img.shields.io/badge/Language-LaTeX-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Introduction
This repository serves as a living document for literature reviews across multiple domains including smart mining, machine learning, computer vision, natural language processing, and quantitative finance. It is maintained long-term to track the evolution of state-of-the-art methods, theoretical foundations, and emerging trends.

## 🗂 Project Structure
```
my_research_handbook/
├── main.tex              # Root LaTeX document
├── Makefile             # Build automation
├── README.md           # This file
├── LICENSE             # MIT License
├── settings/
│   └── preamble.tex    # Global LaTeX configuration and packages
├── sections/           # Modular content chapters
│   ├── 0_preface/      # Preface and abstract
│   ├── smart_mining/   # Smart mining research (formerly winter break research)
│   ├── ai_foundations/ # AI foundations (computer vision, NLP, quant finance)
│   ├── emerging_technologies/  # Emerging AI technologies (world models, VLMs, etc.)
│   └── themes/         # Theme-based organization examples
├── bib/                # Bibliography database
│   ├── smart_mining.bib           # Smart mining references
│   ├── ai_foundations.bib         # AI foundations references
│   └── emerging_technologies.bib  # Emerging AI technologies references
├── assets/             # Figures and resources
│   └── figures/
└── .gitignore          # LaTeX auxiliary files exclusion
```

## 🚀 Getting Started

### Prerequisites
- TeX Live 2023+ or MiKTeX (with XeLaTeX and BibLaTeX support)
- Basic LaTeX knowledge

### Installation
```bash
git clone <repository-url>
cd my_research_handbook
```

### Building the Document
```bash
# Full compilation (recommended)
make

# Fast compilation (for quick checks)
make fast

# Compile and view PDF
make all-view

# Clean intermediate files
make clean

# Deep clean (including PDF)
make distclean
```

## 📝 Adding New Content

### Creating a New Chapter

#### Manual Method
1. Create a new directory in `sections/` with a descriptive name
2. Add a `main.tex` file with proper chapter structure
3. Update `main.tex` to include the new chapter

#### Using Automation Script
For consistency, use the chapter creation script:
```bash
# Create a standalone chapter
python scripts/new_chapter.py "chapter_name"

# Create a chapter within a theme/category
python scripts/new_chapter.py "chapter_name" --theme "theme_name"

# Example: Create a deep learning chapter in ML theme
python scripts/new_chapter.py "deep_learning" --theme "machine_learning"
```

The script will:
- Create directory structure
- Generate chapter template from `settings/template.tex`
- Provide next steps for integration

### Adding References
1. Add BibTeX entries to the appropriate `.bib` file in `bib/`
2. Use `\cite{key}` in your LaTeX content
3. Run `make` to regenerate bibliography

### Adding Figures
1. Place images in `assets/figures/`
2. Use `\includegraphics` with relative path
3. Include PDF or SVG format for best quality

## 🔧 Advanced Usage

### Custom Commands
- `make check` - Check LaTeX syntax
- `make wordcount` - Approximate word count
- `make view` - Open PDF viewer

### Bibliography Management
This project uses BibLaTeX with GB/T 7714-2015 Chinese standard. To change style, modify `settings/preamble.tex`.

### Cross-references
Use `\label{key}` and `\ref{key}` for figures, tables, and sections.

## 📚 Content Organization

The handbook is organized into Parts and Chapters:
- **Part I**: Smart Mining Research
- **Part II**: AI Foundations (Computer Vision, NLP, Quantitative Finance)
- **Part III**: Emerging AI Technologies (World Models, Vision-Language Models, End-to-End Models)

Each part uses `refsection` for independent bibliography management.

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Add your content following existing patterns
4. Test compilation with `make`
5. Submit a pull request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- LaTeX community for excellent documentation
- BibLaTeX developers for powerful bibliography management
- All researchers whose work is cited in this handbook
