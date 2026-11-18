#!/usr/bin/env python3
"""Check required files, input integrity, version labels and Markdown links.
Only scientific inputs are fingerprinted. Documentation is freely editable.
This is a package check, not a mathematical proof or full experiment rerun.
"""
from __future__ import annotations
import hashlib,json,re,sys,tomllib
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    failures=[]
    required=['README.md','RELEASE_NOTES.md','LICENSE','NOTICE.md','CITATION.cff','requirements.txt',
              'docs/REPRODUCING.md','docs/RESULTS_MAP.md','docs/VALIDATION.md','docs/PUBLISHING.md',
              'paper/Zeta_Zeros_Spectral_Statistics_v1.0.md','paper/Zeta_Zeros_Spectral_Statistics_v1.0.pdf','paper/Zeta_Zeros_Spectral_Statistics_v1.0.docx']
    for name in required:
        if not (ROOT/name).is_file():failures.append('Missing required file: '+name)
    if (ROOT/'VERSION').read_text().strip()!='1.0':failures.append('VERSION must be 1.0')
    if tomllib.loads((ROOT/'pyproject.toml').read_text())['project']['version']!='1.0':failures.append('pyproject.toml version must be 1.0')
    cff=(ROOT/'CITATION.cff').read_text()
    if not re.search(r'^version: ["\']?1\.0["\']?\s*$',cff,re.M):failures.append('CITATION.cff project version must be 1.0')
    if not re.search(r'^cff-version: 1\.2\.0\s*$',cff,re.M):failures.append('Unexpected citation format version')
    record=json.loads((ROOT/'manifests/input_data.json').read_text())
    for item in record['files']:
        p=ROOT/item['path']
        if not p.is_file():failures.append('Missing input: '+item['path'])
        elif hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:failures.append('Input fingerprint mismatch: '+item['path'])
    md_files=[p for p in ROOT.rglob('*.md') if not set(p.relative_to(ROOT).parts)&{'build','.git','.venv','__pycache__','.pytest_cache'}]
    links=0
    for p in md_files:
        s=p.read_text()
        if '{{CODE_REPOSITORY_URL}}' in s:failures.append('Unresolved repository URL in '+str(p.relative_to(ROOT)))
        for m in re.finditer(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"\n]*")?\)',s):
            target=m.group(1)
            if re.match(r'(?:https?://|mailto:|#)',target):continue
            target=unquote(target.split('#')[0])
            if target and not (p.parent/target).exists():failures.append(f'Broken relative link in {p.relative_to(ROOT)}: {target}')
            links+=1
    paper=(ROOT/'paper/Zeta_Zeros_Spectral_Statistics_v1.0.md').read_text()
    blocks=re.findall(r'^```math\n(.*?)^```\s*$',paper,re.M|re.S)
    inline=re.findall(r'\$`([^`\n]*)`\$',paper)
    for expression in blocks+inline:
        if r'\operatorname' in expression:failures.append('Avoid operatorname for the documented GitHub renderer limitation')
        if re.search(r'\\left\s*\{',expression):failures.append('Unescaped left-brace delimiter in math')
    figures=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',paper)
    if len(figures)!=8:failures.append(f'Expected eight paper figures; found {len(figures)}')
    for n in ['governance','peer_review']:
        if any(p.is_dir() and p.name==n for p in ROOT.rglob('*') if 'build' not in p.parts):failures.append('Unexpected internal-document directory: '+n)
    result={'status':'FAIL' if failures else 'PASS','input_files_checked':len(record['files']),
            'markdown_files_checked':len(md_files),'relative_links_checked':links,'display_equations':len(blocks),
            'inline_expressions':len(inline),'paper_figures':len(figures),'failures':failures,
            'scope':'Structural checks; MathJax rendering and numerical reruns are separate.'}
    print(json.dumps(result,indent=2));return int(bool(failures))
if __name__=='__main__':raise SystemExit(main())
