# Identification of Natural Remedies for Long COVID Using Hub Gene Biomarkers and Repurposed Drugs
This repository contains a bioinformatics research study identifying potential natural therapeutic compounds for 17 common long COVID symptoms.

## Overview
This research project investigates therapeutic options for Long COVID by identifying hub gene biomarkers and evaluating interactions with natural and repurposed drug compounds. The study integrates gene biomarkers, FDA-approved drugs, and molecular docking simulations to suggest natural remedies. Protein sequences were retrieved from UniProt, and molecular docking was performed using iGEMDOCK to assess the binding affinity of selected compounds. The goal is to provide insight into potential treatments for Long COVID symptoms using in-silico methods, without requiring lab-based experimentation. The study offers a computational approach to accelerate drug discovery and support further clinical validation.

## Repository Contents

- `thesis/`: Final manuscript, literature review, and formal documentation.
- `data/`: Docking results and hub gene sequences (FASTA).
- `presentations/`: Conference and final presentation slide decks.
- `software/`: Tools used (iGEMDOCK) for molecular docking.
- `scripts/`: New scripts that were included after completion of project to increase efficiency and automation of the methodology.
---

## 🔬 Methodology

This study used a bioinformatics pipeline involving the following tools and databases:  
**PubChem, NCBI, NPASS, Open Babel, AlphaFold, UniProt, and iGEMDOCK.**

### 1. **Data Retrieval**
- Long COVID symptoms were gathered from systematic reviews and case studies via PubMed and LitCovid.
- From 250 reported symptoms, 17 of the most recurring were selected (e.g., fatigue, shortness of breath, brain fog, insomnia).

### 2. **Hub Gene and Drug Association**
- Each symptom was mapped to 10 hub genes using prior studies.
- Associated FDA-approved drugs were compiled for these genes.

### 3. **Natural Compound Identification**
- Drug structures were retrieved from PubChem and used to find structurally similar natural compounds via the NPASS database using fingerprint similarity (threshold ≥ 0.80).

### 4. **Structure Preparation**
- 3D protein structures of hub genes were collected from UniProt and AlphaFold.
- 2D structures of natural compounds were retrieved from PubChem and converted to 3D using Open Babel.

### 5. **Molecular Docking**
- Docking simulations were conducted using iGEMDOCK to analyze binding affinity between hub genes and natural compounds.
- The top-ranked compounds with the highest negative binding energy were proposed as therapeutic candidates.

---

## 🧪 Tools & Databases
- **PubChem** (for drug and compound structures)
- **NPASS** (Natural Product Activity and Species Source)
- **UniProt** and **AlphaFold** (for protein structures)
- **Open Babel** (structure conversion)
- **iGEMDOCK** (docking simulation)

---
## Key Findings

- The study evaluated **17 common long COVID symptoms**, mapping each to hub genes and FDA-approved drugs.
- Using structural similarity, natural compounds were identified for 14 of the 17 symptoms.
- 3 symptoms (muscle pain, diarrhea, skin rash) yielded no natural compounds due to lack of structural data.
- Natural compounds like **Gefitinib, Dehydroevidiamine, Lindoldhamine, and Micropeptin B** showed strong binding affinities with genes like RET, NF1, CHRNE, and CACNA1B, respectively.
- These findings suggest potential therapeutic candidates, although further experimental validation is needed.

---
## Note
This research does not include any executable scripts or code but utilizes bioinformatics tools and manual analysis, as some tools did not suppot automation. Future work may automate docking or gene expression analysis using Python or R. The scripts in the `scripts/` folder were included recently to allow ease of extracting FASTA sequences from UniProt database and the retrieval of SMILES structrue from PubChem database.

## License
This project is provided for academic and educational purposes.

- **Author**: Dinesh Davagandhi  
- **Degree**: Bachelor of Biomedical Science (Hons)  
- **University**: Management & Science University  
- **Supervisor**: Dr. Suresh Kumar Sampath Rajan  
- **Date**: May 2023
---

> _This repository contains files from the author's final year research project submitted in partial fulfillment of the requirements for a Bachelor's degree._
