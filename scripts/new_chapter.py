#!/usr/bin/env python3
"""
Script to create a new chapter in the research handbook.
Usage: python scripts/new_chapter.py <chapter_name> [--theme <theme>]
"""

import os
import sys
import argparse
from pathlib import Path

# Project root (relative to script location)
PROJECT_ROOT = Path(__file__).parent.parent

def create_chapter(name, theme=None):
    """Create a new chapter directory with template files."""
    
    # Determine the target directory
    if theme:
        target_dir = PROJECT_ROOT / "sections" / theme / name
    else:
        target_dir = PROJECT_ROOT / "sections" / name
    
    # Create directory
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {target_dir}")
    
    # Create main.tex from template
    template_path = PROJECT_ROOT / "settings" / "template.tex"
    chapter_main = target_dir / "main.tex"
    
    if template_path.exists():
        with open(template_path, 'r') as f:
            template = f.read()
        
        # Replace placeholder with actual chapter name
        content = template.replace("Chapter Title", name.replace("_", " ").title())
        
        with open(chapter_main, 'w') as f:
            f.write(content)
        print(f"Created chapter file: {chapter_main}")
    else:
        # Create minimal main.tex
        with open(chapter_main, 'w') as f:
            f.write(f"\\chapter{{{name.replace('_', ' ').title()}}}\n\n")
            f.write("\\section{Introduction}\n")
            f.write("% Start your content here\n")
        print(f"Created minimal chapter file: {chapter_main}")
    
    # Create a placeholder .bib file if in a theme directory
    if theme:
        bib_file = PROJECT_ROOT / "bib" / f"{theme}.bib"
        if not bib_file.exists():
            bib_file.touch()
            print(f"Created bibliography file: {bib_file}")
    
    # Update main.tex (optional - would need manual review)
    print(f"\nNext steps:")
    print(f"1. Edit content in: {chapter_main}")
    print(f"2. Add references to appropriate .bib file in bib/")
    if theme:
        print(f"3. Update main.tex to include: \\input{{sections/{theme}/{name}/main}}")
    else:
        print(f"3. Update main.tex to include: \\input{{sections/{name}/main}}")
    print(f"4. Run 'make' to compile and verify")

def main():
    parser = argparse.ArgumentParser(description="Create a new chapter in the research handbook")
    parser.add_argument("name", help="Name of the chapter (use underscores for spaces)")
    parser.add_argument("--theme", help="Theme/category for the chapter (e.g., machine_learning, smart_mining)")
    
    args = parser.parse_args()
    
    create_chapter(args.name, args.theme)

if __name__ == "__main__":
    main()