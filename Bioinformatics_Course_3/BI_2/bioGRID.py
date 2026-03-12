from network import Network
from typing import Dict, List, Tuple, Union


class BioGRIDReader:
    """
    Reads a BioGRID database file and stores its processed interaction content. You can add help functions if needed.
    """
    def __init__(self, bioGRID_path: str):
        """
        Read in the BioGRID data and store it. The interaction data should be stored as a dictionary that contains the
        interaction Network for each organism. The mapping data can be stored in a way that you find convenient for the
        rest of the task.

        Specification:
        - Use the official symbols for interactor IDs.
        - Exclude entries where the two interactors belong to different organisms.
        - Exclude entries where the two interactors are the same.
        - Associate the interactions with the organisms via the NCBI taxon ID, not the organism name.
        - For each organism, avoid interaction duplicates and consider that the interactions are undirected.
        - Create a mapping of NCBI taxon IDs <=> organism names from the interaction data.
        - You do not need to handle potential file errors (e.g. the file does not exist).

        :param bioGRID_path: path to the BioGRID file
        """
        # key: NCBI taxon ID, value: Network-object containing the interactions associated with the organism
        self.networks = {}                                              # type: Dict[str, Network]
        # TODO: initialize your data structure for the mapping, and note down its type as shown above
        ...

        # TODO: process and store the interaction and mapping data
        raise NotImplementedError

    def organism_name(self, taxon_id: Union[int, str]) -> str:
        """
        Fetches the organism name associated with the given NCBI taxon ID. If the organism name is not in the mapping,
        this should return the taxon ID tagged with [name unknown], e.g. "1234 [name unknown]".

        :param taxon_id: NCBI taxon ID of an organism
        :return: the organism name associated with the taxon ID, or tagged taxon ID if the organism name is unknown
        :raises: KeyError (with a custom message) if the taxon ID is not included in the BioGRID data
        """
        # TODO
        raise NotImplementedError

    def taxon_id(self, organism_name: str) -> str:
        """
        Fetches the NCBI taxon ID associated with the given organism name. This should be case agnostic, e.g.
        "Homo sapiens" and "homo sapiens" should both work. If the organism name is not in the mapping, this should
        return the organism name tagged with [ID unknown], e.g. "Homo sapiens [ID unknown]".

        :param organism_name: the scientific name of an organism, e.g. "Homo sapiens"
        :return: the NCBI taxon ID associated with the organism name
        """
        # TODO
        raise NotImplementedError

    def network_size(self, taxon_id: Union[int, str]) -> int:
        """
        :param taxon_id: NCBI taxon ID of an organism
        :return: number of undirected interactions for the specified organism
        :raises: KeyError (with a custom message) if there is no data for an organism with that NCBI taxon ID
        """
        # TODO
        raise NotImplementedError

    def most_abundant_taxon_ids(self, n: int) -> List[Tuple[int, str]]:
        """
        Compute the n organisms with the most interactions in BioGRID.

        :param n: number of organisms
        :return: list of the min(n, organisms in database) organisms with the most interactions and the respective
        number of interactions as (interactions, taxon IDs) pairs
        :raises: ValueError (with a custom message) if n is negative
        """
        # TODO
        raise NotImplementedError

    def highest_degree_interactors(self, taxon_id: Union[int, str], n: int) -> List[Tuple[int, str]]:
        """
        Compute the n interactors in the organism-specific network with the highest degree.

        :return: list of the min(n, interactors in the organism network) interactors with the highest degree in the
        organism-specific network as (degree, interactor symbol) pairs
        :raises: KeyError (with a custom message) if there is no data for an organism with that NCBI taxon ID
        :raises: ValueError (with a custom message) if n is negative
        """
        # TODO:
        raise NotImplementedError

    def export_network(self, taxon_id: Union[int, str], file_path: str, delimiter='\t'):
        """
        Writes the interactions of the specified organism into the specified file, matching the specifications of the
        export function in the Network-class.

        :param taxon_id: NCBI taxon ID of an organism
        :param file_path: path to the output network file
        :param delimiter: the delimiter that separates the two columns, default is a tab
        :raises: KeyError (with a custom message) if there is no data for an organism with that NCBI taxon ID
        """
        # TODO
        raise NotImplementedError

