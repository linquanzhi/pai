# Copyright (c) Microsoft Corporation
# All rights reserved.
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import time
import os
import tempfile

from ...confStorage.download import download_configuration
from ...clusterObjectModel.cluster_object_model import cluster_object_model


def gengerate_tmp_path():
    time_in_seconds = str(int(time.time()))
    sub_directory = "tmp-service-config-{0}".format(time_in_seconds)
    return os.path.join(tempfile.gettempdir(), sub_directory)


def get_cluster_object_model_from_k8s(kube_config_path):
    tmp_path = gengerate_tmp_path()

    config_get_handler = download_configuration(config_output_path=tmp_path, kube_config_path=kube_config_path)
    config_get_handler.run()

    objectModelFactoryHandler = cluster_object_model(configuration_path=tmp_path)
    cluster_object_service = objectModelFactoryHandler.service_config()

    return cluster_object_service
