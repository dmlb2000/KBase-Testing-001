#BEGIN_HEADER
import logging
import os
import pprint

from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.annotation_ontology_apiClient import annotation_ontology_api
#END_HEADER
#BEGIN_CLASS_HEADER
#END_CLASS_HEADER
#BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
#END_CONSTRUCTOR
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
        events = annotation_ontology_api(self.callback_url).get_annotation_ontology_events(params={
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
#BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
#END_STATUS