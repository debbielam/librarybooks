# librarybooks
Organising library books

The input file is library-titles.xlsx. Each row of the input file contains the related information of one single book item. 
An ISSN or e-ISSN being considered must have 8 digits; some are separated by ‘-’ while some are not. An ISBN or e-ISBN being considered
must be either 10 digits or 13 digits; some are separated by ‘-’ while some are not. Hence, you need to reset those which are not 
conforming to the aforementioned digit formats to null, instead of dropping, before comparison.

Conditions for a duplication:
1)Exact match of any of the ISSN, e-ISSN, ISBN, and e-ISBN and exact match of the TITLE name from two or more book items.
2)Such matches must come from different DB.; i.e. multiple (same) book items from the same DB must be merged as one book item before matching.
3)Only output one record for the duplicated titles in duplication.csv; i.e. permutation should not be excluded. See below:All of the scenarios above are considered the same description of duplication and your output should use scenario 3 where unqiue duplicates are sorted alphabetically by DB.
