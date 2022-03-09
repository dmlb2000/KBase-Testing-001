# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import pprint

from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.annotation_ontology_apiClient import annotation_ontology_api
#END_HEADER


class dmlb2000genome:
    '''
    Module Name:
    dmlb2000genome

    Module Description:
    A KBase module: dmlb2000genome
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:dmlb2000/KBase-Testing-001.git"
    GIT_COMMIT_HASH = "41e16c3ba157525d7da53d053215c46ca529fd93"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_dmlb2000genome(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_dmlb2000genome
        print(f"Input parameter {params['parameter_1']}")
        pp = pprint.PrettyPrinter(indent=4)
        dfu = DataFileUtil(self.callback_url)
        genome_ref = dfu.get_objects({'object_refs': [params['parameter_1'],]})['data']
        print('='*80)
        pp.pprint(genome_ref[0]['data']['cdss'][0])
        print('='*80)
        pp.pprint(genome_ref[0]['data']['mrnas'][0])
        print('='*80)
        #pp.pprint(genome_ref[0]['data']['taxon_assignments'])
        print('='*80)
        events = annotation_ontology_api(service_ver='dev').get_annotation_ontology_events(params={
                "input_ref": params['parameter_1'],
                "input_workspace": params['workspace_name']
        })
        pp.pprint(events)
        print('='*80)
        report = KBaseReport(self.callback_url)
        report_info = report.create({
            'report': {
                'objects_created':[],
                'text_message': params['parameter_1']
            },
            'workspace_name': params['workspace_name']
        })
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_dmlb2000genome

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_dmlb2000genome return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
