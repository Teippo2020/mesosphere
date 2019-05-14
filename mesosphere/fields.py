from marshmallow import validators


class Field(object):

    def validate():
        raise NotImplementedError(
            'Every field should implement its own validation rules'
        )


class CharField(Field):

    def __init__(
        self,
        required=False,
        allow_blank=True,
        allow_none=False,
        max_length=None,
        min_length=None
    ):

        self.validators = []
        self.validators_precedence = [
            'required', 'allow_none', 'allow_blank', 'min_length', 'max_length'
        ]

        if required:
            self.validators.push(validators.RequiredValidator())

        if not allow_blank:
            self.validators.push(validators.DontAllowBlankValidator())

        if not allow_none:
            self.validators.push(validators.DontAllowNoneValidator())

        if max_length:
            self.validators.push(
                validators.MaxLengthValidator(
                    max_length=max_length
                )
            )

        if min_length:
            self.validators.push(
                validators.MinLengthValidator(
                    min_length=min_length
                )
            )

    def validate('')
