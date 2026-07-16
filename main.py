import argparse
import logging
from core.ntlm_extractor import NTLMExtractor
from utils.logger import setup_logger

def parse_arguments():
    parser = argparse.ArgumentParser(description='Extract NTLM hashes from a PCAP file.')
    parser.add_argument('--pcap-file', required=True, help='Path to the PCAP file to analyze.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    logger = setup_logger('ntlm_extractor')
    
    try:
        extractor = NTLMExtractor(logger)
        ntlm_hashes = extractor.extract_hashes_from_pcap(args.pcap_file)
        if ntlm_hashes:
            logger.info('Extracted NTLM hashes:')
            for hash_ in ntlm_hashes:
                print(hash_)
        else:
            logger.info('No NTLM hashes found in the PCAP file.')
    except Exception as e:
        logger.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()