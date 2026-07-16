# NTLM Hash Extractor

## Description
The NTLM Hash Extractor is a tool designed to extract NTLM hashes from network traffic captures (PCAP files). This can be useful for security researchers and penetration testers who need to analyze network traffic for NTLM hash exchanges.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ntlm-hash-extractor.git
   cd ntlm-hash-extractor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
```bash
python main.py --pcap-file <path_to_pcap_file>
```

### Options
- `--pcap-file <path>`: Path to the PCAP file to analyze.

## Examples
```bash
python main.py --pcap-file example_traffic.pcap
```

This will parse the `example_traffic.pcap` file and print any NTLM hashes found in the NTLM authentication exchanges.