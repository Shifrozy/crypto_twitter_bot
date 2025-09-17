import re

EXPLORERS = {
    "etherscan.io": "ethereum",
    "bscscan.com": "bsc",
    "polygonscan.com": "polygon",
    "snowtrace.io": "avalanche",
    "solscan.io": "solana"
}

def detect_chain(data: str):
    # Check URLs
    for domain, chain in EXPLORERS.items():
        if domain in data.lower():
            return chain
    
    # Wallet pattern detection
    if re.match(r"^0x[a-fA-F0-9]{40}$", data):
        return "evm"
    if data.startswith("bc1") or re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", data):
        return "bitcoin"
    if len(data) in [43, 44]:
        return "solana"
    
    return None