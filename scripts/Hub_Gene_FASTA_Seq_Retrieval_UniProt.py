import requests

def get_uniprot_fasta_formatted(gene_name, organism_id="9606"):
    # Step 1: Use updated UniProt API for gene search
    query = f"(gene_exact:{gene_name}) AND (organism_id:{organism_id}) AND (reviewed:true)"
    url = "https://rest.uniprot.org/uniprotkb/search"
    params = {
        "query": query,
        "fields": "accession",
        "format": "json",
        "size": 1
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"❌ UniProt search failed for gene '{gene_name}'.")
        return

    data = response.json()
    results = data.get("results", [])
    if not results:
        print(f"⚠️ No reviewed UniProt entry found for '{gene_name}'.")
        return

    accession = results[0]["primaryAccession"]

    # Step 2: Fetch FASTA sequence using the accession
    fasta_url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    fasta_response = requests.get(fasta_url)
    if fasta_response.status_code != 200:
        print(f"❌ Failed to retrieve FASTA for accession '{accession}'")
        return

    fasta_lines = fasta_response.text.strip().split("\n")
    header = fasta_lines[0]
    sequence = ''.join(fasta_lines[1:])

    # Print in your requested format
    print(gene_name)
    print(header)
    for i in range(0, len(sequence), 60):
        print(sequence[i:i+60])

# Example
get_uniprot_fasta_formatted("SMAD4")
