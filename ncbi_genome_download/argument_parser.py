"""Command line parser for ncbi-genome-download"""
import argparse
from ncbi_genome_download import __version__
from ncbi_genome_download import EDefaults as dflt


def argument_parser():
    """Argument parser for ncbi-genome-download"""
    parser = argparse.ArgumentParser()
    parser.add_argument('group',
                        #choices=dflt.TAXONOMIC_GROUPS.choices, # Moved choice checking to method
                        default=dflt.TAXONOMIC_GROUPS.default,
                        help='The NCBI taxonomic group to download (default: %(default)s). '
                        'A comma-separated list of taxonomic groups is also possible. For example: "bacteria,viral"'
                        'Choose from: {choices}'.format(choices=dflt.TAXONOMIC_GROUPS.choices))
    parser.add_argument('-s', '--section', dest='section',
                        choices=dflt.SECTIONS.choices,
                        default=dflt.SECTIONS.default,
                        help='NCBI section to download (default: %(default)s)')
    parser.add_argument('-F', '--format', dest='file_format',
                        #choices=dflt.FORMATS.choices, # Moved choice checking to method
                        default=dflt.FORMATS.default,
                        help='Which format to download (default: %(default)s).' 
                        'A comma-separated list of formats is also possible. For example: "fasta,assembly-report". '
                        'Choose from: {choices}'.format(choices=dflt.FORMATS.choices))
    parser.add_argument('-l', '--assembly-level', dest='assembly_level',
                        choices=dflt.ASSEMBLY_LEVELS.choices,
                        default=dflt.ASSEMBLY_LEVELS.default,
                        help='Assembly level of genomes to download (default: %(default)s)')
    parser.add_argument('-g', '--genus', dest='genus',
                        default=dflt.GENUS.default,
                        help='Only download sequences of the provided genus. '
                        'A comma-seperated list of genera is also possible. For example: "Streptomyces coelicolor,Escherichia coli".'
                        '(default: %(default)s)')
    parser.add_argument('-T', '--species-taxid', dest='species_taxid',
                        default=dflt.SPECIES_TAXID.default,
                        help='Only download sequences of the provided species NCBI taxonomy ID. '
                            'A comma-separated list of species taxids is also possible. For example: "52342,12325". '
                             '(default: %(default)s)'
                            )
    parser.add_argument('-t', '--taxid', dest='taxid',
                        default=dflt.TAXID.default,
                        help='Only download sequences of the provided NCBI taxonomy ID. '
                             'A comma-separated list of taxids is also possible. For example: "9606,9685". '
                             '(default: %(default)s)')
    parser.add_argument('-R', '--refseq-category', dest='refseq_category',
                        choices=dflt.REFSEQ_CATEGORIES.choices,
                        default=dflt.REFSEQ_CATEGORIES.default,
                        help='Only download sequences of the provided refseq category (default: %(default)s)')
    parser.add_argument('-o', '--output-folder', dest='output',
                        default=dflt.OUTPUT.default,
                        help='Create output hierarchy in specified folder (default: %(default)s)')
    parser.add_argument('-H', '--human-readable', dest='human_readable', action='store_true',
                        help='Create links in human-readable hierarchy (might fail on Windows)')
    parser.add_argument('-u', '--uri', dest='uri',
                        default=dflt.URI.default,
                        help='NCBI base URI to use (default: %(default)s)')
    parser.add_argument('-p', '--parallel', dest='parallel', type=int, metavar="N",
                        default=dflt.NB_PROCESSES.default,
                        help='Run %(metavar)s downloads in parallel (default: %(default)s)')
    parser.add_argument('-r', '--retries', dest='retries', type=int, metavar="N",
                        default=0,
                        help='Retry download %(metavar)s times when connection to NCBI fails ('
                             'default: %(default)s)')
    parser.add_argument('-m', '--metadata-table', type=str,
                        help='Save tab-delimited file with genome metadata')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='print debugging information')
    parser.add_argument('-V', '--version', action='version', version=__version__,
                        help='print version information')
    return parser