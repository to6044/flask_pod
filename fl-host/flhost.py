from flask import Flask, jsonify, make_response
from flask_api import status
from os import getenv
import logging
import kfp
import traceback


APP = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@APP.route("/pipelines")
def list_pipelines():
    pipe_dict = {}
    try:
        pipeline_list = client.list_pipelines(page_size=20)
        pipe_dict['next_page_token'] = pipeline_list.next_page_token
        pipe_dict['total_size'] = pipeline_list.total_size
        
        pipelines = []
        for pipeline in pipeline_list.pipelines:
            pipe_super_dict = {} 
            pipe_super_dict['pipeline_id'] = pipeline.pipeline_id
            pipe_super_dict['display_name'] = pipeline.display_name
            pipe_super_dict['description'] = pipeline.description
            pipe_super_dict['created_at'] = pipeline.created_at
            pipelines.append(pipe_super_dict)
        pipe_dict['pipelines'] = pipelines
        
    except:
        tbk = traceback.format_exc()
        logging.error(tbk)
        response = make_response(jsonify({'error': 'Unsupported error from Kubeflow'}), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    return jsonify(pipe_dict), status.HTTP_200_OK




if __name__ == "__main__":
    #Kubeflow uri
    kf_dict = {}
    kf_dict['kfhostname'] = getenv('KUBEFLOW_HOST')
    kf_dict['kfport'] = getenv('KUBEFLOW_PORT')
    kf_dict['kfdefaultns'] = getenv('KF_FL_NAMESPACE')
    appport = getenv('KF_FL_HOST_PORT')
    # KF_HOST_URI = "http://" + kf_dict['kfhostname'] + ":" + kf_dict['kfport'] + "/pipeline"
    KF_HOST_URI = "http://" + str(kf_dict['kfhostname']) + ":" + str(kf_dict['kfport']) + "/pipeline"
    logging.debug(KF_HOST_URI)

    try:
        client = kfp.Client(KF_HOST_URI)
        logging.debug(appport)
        # THR = Thread(target=wait_status_thread, args=(1, KFCONNECT_KF_OBJ))
        # THR.start()
        APP.run(debug=True, host='0.0.0.0', port=appport)
    except Exception as some_err:# pylint: disable=broad-except
        logging.error(some_err)
