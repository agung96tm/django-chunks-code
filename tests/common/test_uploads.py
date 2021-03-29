from unittest.mock import MagicMock

from django.test import TestCase

from src.common.uploads import UUIDUploadTo

from uuid import UUID


def is_valid_uuid(uuid_to_test, version=4):
    """ check string is uuid format """
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


class UUIDUploadToTest(TestCase):
    def setUp(self):
        self.instance = MagicMock()

    def test_success_generate_random_uuid_filename(self):
        upload = UUIDUploadTo('images/media')
        result = upload(self.instance, 'myfile.jpg')
        self.assertTrue(is_valid_uuid(result.split('/')[-1].split('.')[0]))
