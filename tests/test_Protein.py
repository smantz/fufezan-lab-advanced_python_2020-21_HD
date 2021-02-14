from Ex4.Protein import Protein
from Ex4.Ex4_functions import get_lookup_dict


def test_get_data():
    p1 = Protein('P32249')
    sequence = p1.get_data()
    assert sequence == ['M', 'D', 'I', 'Q', 'M', 'A', 'N', 'N', 'F', 'T', 'P', 'P', 'S', 'A', 'T', 'P', 'Q', 'G', 'N',
                        'D', 'C', 'D', 'L', 'Y', 'A', 'H', 'H', 'S', 'T', 'A', 'R', 'I', 'V', 'M', 'P', 'L', 'H', 'Y',
                        'S', 'L', 'V', 'F', 'I', 'I', 'G', 'L', 'V', 'G', 'N', 'L', 'L', 'A', 'L', 'V', 'V', 'I', 'V',
                        'Q', 'N', 'R', 'K', 'K', 'I', 'N', 'S', 'T', 'T', 'L', 'Y', 'S', 'T', 'N', 'L', 'V', 'I', 'S',
                        'D', 'I', 'L', 'F', 'T', 'T', 'A', 'L', 'P', 'T', 'R', 'I', 'A', 'Y', 'Y', 'A', 'M', 'G', 'F',
                        'D', 'W', 'R', 'I', 'G', 'D', 'A', 'L', 'C', 'R', 'I', 'T', 'A', 'L', 'V', 'F', 'Y', 'I', 'N',
                        'T', 'Y', 'A', 'G', 'V', 'N', 'F', 'M', 'T', 'C', 'L', 'S', 'I', 'D', 'R', 'F', 'I', 'A', 'V',
                        'V', 'H', 'P', 'L', 'R', 'Y', 'N', 'K', 'I', 'K', 'R', 'I', 'E', 'H', 'A', 'K', 'G', 'V', 'C',
                        'I', 'F', 'V', 'W', 'I', 'L', 'V', 'F', 'A', 'Q', 'T', 'L', 'P', 'L', 'L', 'I', 'N', 'P', 'M',
                        'S', 'K', 'Q', 'E', 'A', 'E', 'R', 'I', 'T', 'C', 'M', 'E', 'Y', 'P', 'N', 'F', 'E', 'E', 'T',
                        'K', 'S', 'L', 'P', 'W', 'I', 'L', 'L', 'G', 'A', 'C', 'F', 'I', 'G', 'Y', 'V', 'L', 'P', 'L',
                        'I', 'I', 'I', 'L', 'I', 'C', 'Y', 'S', 'Q', 'I', 'C', 'C', 'K', 'L', 'F', 'R', 'T', 'A', 'K',
                        'Q', 'N', 'P', 'L', 'T', 'E', 'K', 'S', 'G', 'V', 'N', 'K', 'K', 'A', 'L', 'N', 'T', 'I', 'I',
                        'L', 'I', 'I', 'V', 'V', 'F', 'V', 'L', 'C', 'F', 'T', 'P', 'Y', 'H', 'V', 'A', 'I', 'I', 'Q',
                        'H', 'M', 'I', 'K', 'K', 'L', 'R', 'F', 'S', 'N', 'F', 'L', 'E', 'C', 'S', 'Q', 'R', 'H', 'S',
                        'F', 'Q', 'I', 'S', 'L', 'H', 'F', 'T', 'V', 'C', 'L', 'M', 'N', 'F', 'N', 'C', 'C', 'M', 'D',
                        'P', 'F', 'I', 'Y', 'F', 'F', 'A', 'C', 'K', 'G', 'Y', 'K', 'R', 'K', 'V', 'M', 'R', 'M', 'L',
                        'K', 'R', 'Q', 'V', 'S', 'V', 'S', 'I', 'S', 'S', 'A', 'V', 'K', 'S', 'A', 'P', 'E', 'E', 'N',
                        'S', 'R', 'E', 'M', 'T', 'E', 'T', 'Q', 'M', 'M', 'I', 'H', 'S', 'K', 'S', 'S', 'N', 'G', 'K']


def test_map():
    p1 = Protein('P32249')
    lookup_dictionary = get_lookup_dict('amino_acid_properties.csv')
    result_list = p1.map(lookup_dictionary, 'hydropathy index (Kyte-Doolittle method)')
    assert result_list == [1.9, -3.5, 4.5, -3.5, 1.9, 1.8, -3.5, -3.5, 2.8, -0.7, -1.6, -1.6, -0.8, 1.8, -0.7, -1.6,
                           -3.5, -0.4, -3.5, -3.5, 2.5, -3.5, 3.8, -1.3, 1.8, -3.2, -3.2, -0.8, -0.7, 1.8, -4.5, 4.5,
                           4.2, 1.9, -1.6, 3.8, -3.2, -1.3, -0.8, 3.8, 4.2, 2.8, 4.5, 4.5, -0.4, 3.8, 4.2, -0.4, -3.5,
                           3.8, 3.8, 1.8, 3.8, 4.2, 4.2, 4.5, 4.2, -3.5, -3.5, -4.5, -3.9, -3.9, 4.5, -3.5, -0.8, -0.7,
                           -0.7, 3.8, -1.3, -0.8, -0.7, -3.5, 3.8, 4.2, 4.5, -0.8, -3.5, 4.5, 3.8, 2.8, -0.7, -0.7, 1.8,
                           3.8, -1.6, -0.7, -4.5, 4.5, 1.8, -1.3, -1.3, 1.8, 1.9, -0.4, 2.8, -3.5, -0.9, -4.5, 4.5,
                           -0.4, -3.5, 1.8, 3.8, 2.5, -4.5, 4.5, -0.7, 1.8, 3.8, 4.2, 2.8, -1.3, 4.5, -3.5, -0.7, -1.3,
                           1.8, -0.4, 4.2, -3.5, 2.8, 1.9, -0.7, 2.5, 3.8, -0.8, 4.5, -3.5, -4.5, 2.8, 4.5, 1.8, 4.2,
                           4.2, -3.2, -1.6, 3.8, -4.5, -1.3, -3.5, -3.9, 4.5, -3.9, -4.5, 4.5, -3.5, -3.2, 1.8, -3.9,
                           -0.4, 4.2, 2.5, 4.5, 2.8, 4.2, -0.9, 4.5, 3.8, 4.2, 2.8, 1.8, -3.5, -0.7, 3.8, -1.6, 3.8,
                           3.8, 4.5, -3.5, -1.6, 1.9, -0.8, -3.9, -3.5, -3.5, 1.8, -3.5, -4.5, 4.5, -0.7, 2.5, 1.9,
                           -3.5, -1.3, -1.6, -3.5, 2.8, -3.5, -3.5, -0.7, -3.9, -0.8, 3.8, -1.6, -0.9, 4.5, 3.8, 3.8,
                           -0.4, 1.8, 2.5, 2.8, 4.5, -0.4, -1.3, 4.2, 3.8, -1.6, 3.8, 4.5, 4.5, 4.5, 3.8, 4.5, 2.5,
                           -1.3, -0.8, -3.5, 4.5, 2.5, 2.5, -3.9, 3.8, 2.8, -4.5, -0.7, 1.8, -3.9, -3.5, -3.5, -1.6,
                           3.8, -0.7, -3.5, -3.9, -0.8, -0.4, 4.2, -3.5, -3.9, -3.9, 1.8, 3.8, -3.5, -0.7, 4.5, 4.5,
                           3.8, 4.5, 4.5, 4.2, 4.2, 2.8, 4.2, 3.8, 2.5, 2.8, -0.7, -1.6, -1.3, -3.2, 4.2, 1.8, 4.5, 4.5,
                           -3.5, -3.2, 1.9, 4.5, -3.9, -3.9, 3.8, -4.5, 2.8, -0.8, -3.5, 2.8, 3.8, -3.5, 2.5, -0.8,
                           -3.5, -4.5, -3.2, -0.8, 2.8, -3.5, 4.5, -0.8, 3.8, -3.2, 2.8, -0.7, 4.2, 2.5, 3.8, 1.9, -3.5,
                           2.8, -3.5, 2.5, 2.5, 1.9, -3.5, -1.6, 2.8, 4.5, -1.3, 2.8, 2.8, 1.8, 2.5, -3.9, -0.4, -1.3,
                           -3.9, -4.5, -3.9, 4.2, 1.9, -4.5, 1.9, 3.8, -3.9, -4.5, -3.5, 4.2, -0.8, 4.2, -0.8, 4.5,
                           -0.8, -0.8, 1.8, 4.2, -3.9, -0.8, 1.8, -1.6, -3.5, -3.5, -3.5, -0.8, -4.5, -3.5, 1.9, -0.7,
                           -3.5, -0.7, -3.5, 1.9, 1.9, 4.5, -3.2, -0.8, -3.9, -0.8, -0.8, -3.5, -0.4, -3.9]
