#!/usr/bin/env python
# File created on 22 Feb 2012
from __future__ import division

__author__ = "Greg Caporaso"
__copyright__ = "Copyright 2011, The PICRUST project"
__credits__ = ["Greg Caporaso"]
__license__ = "GPL"
__version__ = "1.4.0-dev"
__maintainer__ = "Greg Caporaso"
__email__ = "gregcaporaso@gmail.com"
__status__ = "Development"
 

from cogent.util.unit_test import TestCase, main
from picrust.parse import parse_marker_gene_copy_numbers,\
  extract_ids_from_table

class ParseTests(TestCase):
    """ """
    
    def setUp(self):
        """ """
        self.counts_f1 = counts_f1.split('\n')
        self.counts_bad1 = counts_bad1.split('\n')
        self.counts_bad2 = counts_bad2.split('\n')
    
    def test_parse_marker_gene_copy_numbers(self):
        """ parse_marker_gene_copy_numbers functions as expected with valid input 
        """
        
        actual = parse_marker_gene_copy_numbers(self.counts_f1,
                                                metadata_identifier='cn')
        expected = {'GG_OTU_1':{'cn':2},
                    'GG_OTU_2':{'cn':4},
                    'GG_OTU_3':{'cn':1}}
        self.assertEqual(actual,expected)
    
    def test_parse_marker_gene_copy_numbers_invalid(self):
        """ parse_marker_gene_copy_numbers raises ValueError on invalid input 
        """
        self.assertRaises(ValueError,parse_marker_gene_copy_numbers,self.counts_bad1,'cn')
        self.assertRaises(ValueError,parse_marker_gene_copy_numbers,self.counts_bad2,'cn')


    
    def test_extract_ids_from_table_qiime_legacy_otu_table(self):
        """extract_ids_from_table extracts ids from a legacy QIIME 1.3 OTU table
        """
        exp = ['39','238','277','1113','1206','1351',\
          '1637','2043','3472','3757','4503','4546',\
          '5403','5479']
        obs = extract_ids_from_table(otu_table_lines)
        self.assertEqual(obs,exp)
        
    

        
otu_table_lines =[\
'# QIIME v1.3.0 OTU table',\
'#OTU ID\tS1\tS2\tS3\tS4\tS5\tS6\tS7\tS8\tS9\tConsensus Lineage',\
'39\t0\t0\t1\t0\t0\t5\t3\t0\t1\tArchaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae',\
 '238\t0\t1\t5\t6\t0\t1\t5\t2\t3\tArchaea;Euryarchaeota',\
 '277\t0\t0\t2\t0\t0\t0\t0\t5\t1\tArchaea;Euryarchaeota',\
 '1113\t0\t0\t0\t0\t1\t5\t0\t0\t0\tArchaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae',\
 '1206\t0\t0\t3\t2\t0\t1\t0\t0\t0\tArchaea;Euryarchaeota',\
 '1351\t0\t0\t0\t0\t0\t0\t1\t11\t5\tArchaea;Euryarchaeota',\
 '1637\t0\t3\t0\t2\t0\t0\t0\t3\t0\tArchaea;Euryarchaeota',\
 '2043\t0\t0\t0\t1\t0\t0\t1\t0\t0\tArchaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halorubrum',\
 '3472\t0\t0\t2\t0\t0\t0\t0\t2\t1\tArchaea;Euryarchaeota',\
 '3757\t0\t0\t1\t2\t0\t3\t0\t0\t0\tArchaea',\
 '4503\t0\t0\t0\t0\t0\t1\t1\t0\t0\tArchaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae',\
 '4546\t0\t3\t0\t3\t0\t0\t9\t6\t2\tArchaea;Euryarchaeota',\
 '5403\t1\t2\t1\t1\t0\t1\t0\t1\t3\tArchaea;Euryarchaeota',\
 '5479\t0\t0\t1\t1\t0\t0\t0\t0\t0\tArchaea']

counts_f1 = """GG_OTU_1	2
GG_OTU_2	4
GG_OTU_3	1"""

counts_bad1 = """GG_OTU_1	hello
GG_OTU_2	4
GG_OTU_3	1"""

counts_bad2 = """GG_OTU_1	42
GG_OTU_2	4
GG_OTU_3	0"""

if __name__ == "__main__":
    main()
