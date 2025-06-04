import requests
import difflib

def get_best_smiles(drug_name):
    # Step 1: Search for CIDs by drug name
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/cids/JSON"
    response = requests.get(search_url)
    
    if response.status_code != 200:
        print(f"❌ CID search failed with status code {response.status_code}")
        return None

    cids = response.json().get("IdentifierList", {}).get("CID", [])
    if not cids:
        print(f"⚠️ No CIDs found for '{drug_name}'.")
        return None

    best_match = None
    highest_similarity = 0

    # Step 2: Fetch and compare titles for each CID
    for cid in cids[:10]:  # Limit to first 10 results for speed
        prop_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/CanonicalSMILES,Title/JSON"
        prop_response = requests.get(prop_url)
        
        if prop_response.status_code != 200:
            continue
        
        props = prop_response.json().get("PropertyTable", {}).get("Properties", [])
        if not props:
            continue
        
        compound = props[0]
        title = compound.get("Title", "")
        smiles = compound.get("CanonicalSMILES", "")
        
        # Calculate similarity score between query and title
        similarity = difflib.SequenceMatcher(None, drug_name.lower(), title.lower()).ratio()

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = {
                "title": title,
                "smiles": smiles,
                "similarity": similarity,
                "cid": cid
            }

    if best_match:
        print(f"✅ Best match for '{drug_name}':")
        print(f"   ➤ Title: {best_match['title']}")
        print(f"   ➤ CID: {best_match['cid']}")
        print(f"   ➤ Similarity: {best_match['similarity']:.2f}")
        print(f"   ➤ SMILES: {best_match['smiles']}")
        return best_match['smiles']
    else:
        print(f"⚠️ No suitable match found for '{drug_name}'.")
        return None

# Name of the FDA-Approved Drug
get_best_smiles("DACOMITINIB")
