# Copyright (C) 2015  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

# Functions defined here are NOT DESIGNED FOR PRODUCTION


from swh.web.ui import controller
from swh.storage.api.client import RemoteStorage as Storage


# Because the Storage's __init__ function does side effect at startup...
class RemoteStorageAdapter(Storage):
    def __init__(self, base_url):
        self.base_url = base_url


def _init_mock_storage():
    """Instanciate a remote storage whose goal is to be mocked in a test
    context.

    NOT FOR PRODUCTION

    Returns:
        An instance of swh.storage.api.client.RemoteStorage destined to be
        mocked (it does not do any rest call)

    """
    return RemoteStorageAdapter('http://somewhere.org:4321/')  # Mock


def init_app():
    """Function to initiate a flask app with storage designed to be mocked.

    Returns:
        Tuple app and storage.

    NOT FOR PRODUCTION

    """
    storage = _init_mock_storage()

    # inject the mock data
    conf = {'api_backend': 'https://somewhere.org:4321',
            'storage': storage,
            'upload_folder': '/some/upload-dir'}

    controller.app.config['TESTING'] = True
    controller.app.config.update({'conf': conf})
    app = controller.app.test_client()

    return app, storage
