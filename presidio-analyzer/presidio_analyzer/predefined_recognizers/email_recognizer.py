import tldextract

from presidio_analyzer import Pattern, PatternRecognizer


# pylint: disable=line-too-long
class EmailRecognizer(PatternRecognizer):
    """
    Recognizes email addresses using regex
    """

    PATTERN_GROUPS = [
        (
            "Email (Medium)",
            r"\b((([!#$%&'*+\-/=?^_`{|}~\w])|([!#$%&'*+\-/=?^_`{|}~\w][!#$%&'*+\-/=?^_`{|}~\.\w]{0,}[!#$%&'*+\-/=?^_`{|}~\w]))[@]\w+([-.]\w+)*\.\w+([-.]\w+)*)\b",  # noqa: E501
            0.5,
        ),
    ]

    CONTEXT = ["email"]

    def __init__(
        self,
        pattern_groups=None,
        context=None,
        supported_language="en",
        supported_entity="EMAIL_ADDRESS",
    ):
        pattern_groups = pattern_groups if pattern_groups else self.PATTERN_GROUPS
        context = context if context else self.CONTEXT
        patterns = [Pattern(*pattern_group) for pattern_group in pattern_groups]
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )

    def validate_result(self, pattern_text):
        result = tldextract.extract(pattern_text)
        return result.fqdn != ""
