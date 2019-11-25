from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from contributors.models.base import NAME_LENGTH, CommonFields
from contributors.models.contributor import Contributor
from contributors.models.organization import Organization


class Repository(CommonFields):
    """Model representing a repository."""

    contributors = models.ManyToManyField(
        Contributor,
        through='Contribution',
        verbose_name=_('Contributors'),
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name=_('Organization'),
    )
    full_name = models.CharField(_('full name'), max_length=NAME_LENGTH)

    class Meta(object):
        verbose_name = _('Repository')
        verbose_name_plural = _('Repositories')

    def get_absolute_url(self):
        """Returns the url of an instance."""
        return reverse('contributors:repository_details', args=[self.pk])