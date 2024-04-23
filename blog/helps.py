import uuid


class SaveMediaFile(object):
    def blog_save_image(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'blog/{uuid.uuid4()}.{image_extension}'
