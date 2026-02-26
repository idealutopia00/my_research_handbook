# References Management Guide

This document outlines how references are organized and managed in the research handbook.

## Current Structure

### Bibliography Files
- `bib/0.bib` - Smart mining and related references
- `bib/uncategorized.bib` - General references (ML, CV, NLP, Quant Finance)

### LaTeX Configuration
References are loaded in `settings/preamble.tex`:
```latex
\addbibresource{bib/uncategorized.bib}
\addbibresource{bib/0.bib}
```

### Citation Style
The project uses GB/T 7714-2015 Chinese standard (国标样式). To change:
1. Modify `style=` in `settings/preamble.tex`
2. Available styles: `ieee`, `apa`, `mla`, `nature`, etc.

## Adding New References

### Method 1: Direct Editing
1. Open the appropriate `.bib` file
2. Add BibTeX entry in correct format
3. Use `\cite{key}` in LaTeX content

### Method 2: Using Reference Manager
1. Export references from Zotero/Mendeley as BibTeX
2. Copy entries to appropriate `.bib` file
3. Ensure unique citation keys

### Citation Key Convention
Use format: `AuthorLastName_ShortTitle_Year`
- Example: `WangGuoFa_MeiKuangZhiNengHua_2019`

## Future Organization Plan

For better scalability, consider organizing references by theme:

```
bib/
├── smart_mining/
│   ├── digital_twin.bib
│   ├── parallel_systems.bib
│   └── intelligent_mining.bib
├── machine_learning/
│   ├── transformers.bib
│   ├── deep_learning.bib
│   └── reinforcement_learning.bib
├── computer_vision/
├── natural_language_processing/
├── quantitative_finance/
└── general.bib
```

To migrate to this structure:
1. Create new `.bib` files in theme directories
2. Move entries from existing files
3. Update `\addbibresource` calls in preamble
4. Update citation keys in LaTeX content

## Best Practices

1. **Unique Keys**: Ensure each citation key is unique across all `.bib` files
2. **Complete Entries**: Include all required fields (author, title, year, etc.)
3. **Consistent Formatting**: Follow BibTeX formatting standards
4. **Regular Maintenance**: Periodically check for duplicate entries
5. **Backup**: Keep backup of bibliography files

## Troubleshooting

### Missing References
1. Run `biber main` manually
2. Check `.bib` file path in preamble
3. Verify citation keys match

### Incorrect Formatting
1. Check BibTeX entry syntax
2. Ensure proper field formatting
3. Verify style compatibility

### Duplicate Citations
1. Search for duplicate keys
2. Merge or remove duplicates
3. Update LaTeX citations accordingly