import os
import uuid


from django.utils.deconstruct import deconstructible


@deconstructible
class UUIDUploadTo:
    """
    Automatically change name of file to uuid
    > my-uploaded-file.png
    >> e1f19c9d-2a40-4a8c-af32-61dfc1c94e25.png
    How to:
    class Gallery(models.Model):
        # result: media/e1f19c9d-2a40-4a8c-af32-61dfc1c94e25.png
        file = models.FileField(upload_to=UUIDUploadTo('media'))
    """
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        path = os.path.join(self.path, "%s%s")
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return path % (uuid.uuid4(), extension)
