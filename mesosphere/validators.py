from mesosphere import utils


class Validator(object):

    def validate(self):
        raise NotImplementedError(
            'Every validator should implement its own validation'
        )


class RequiredValidator(Validator):

    context = {
        'code': 'required'
    }

    def validate(self, field, document):
        return utils.dict_contains_key(document, field)


class DontAllowBlankValidator(Validator):

    context = {
        'code': 'blank_is_now_allowed'
    }

    def validate(self, value):
        return value.strip() != ''


class DontAllowNoneValidator(Validator):

    context = {
        'code': 'null_is_not_allowed'
    }

    def validate(self, value):
        return value is not None


class MaxLengthValidator(Validator):

    context = {
        'code': 'max_length'
    }

    def __init__(self, max_length):
        self.context['max_length'] = max_length

    def validate(self, value):
        return value <= self.context['max_length']


class MinLengthValidator(Validator):

    context = {
        'code': 'min_length'
    }

    def __init__(self, min_length):
        self.context['min_length'] = min_length

    def validate(self, value):
        return value >= self.context['min_length']
