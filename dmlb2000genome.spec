/*
A KBase module: dmlb2000genome
*/

module dmlb2000genome {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_dmlb2000genome(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
