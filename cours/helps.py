import uuid


class SaveMediaFile(object):
    def speciality_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"speciality/{uuid.uuid4()}.{image_extension}"

    def course_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"course/{uuid.uuid4()}.{image_extension}"

    def teacher_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"teacher/{uuid.uuid4()}.{image_extension}"
