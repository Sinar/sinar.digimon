from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective import dexteritytextindexer

from sinar.digimon import MessageFactory as _


# Interface class; used to define content-type schema.

class IIncident(form.Schema, IImageScaleTraversable):
    """
    Incident Report
    """

    summary = RichText (
            title=_(u'Detailed Summary'),
            description=_(u'Detailed Summary of the incident'),
            required=True,
            )

    incident_date = schema.Datetime(
            title=_(u'Incident Date'),
            )

    violation_type = schema.Choice(
                     title=_(u'Type of Violation'),
                     values=['Censorship','Takedown'],
                     )

    media_type = schema.Choice(
                 title=_(u'Media Type'),
                 values=['Article','News','Video','Audio','Photo'],
                 )

    offense_type = schema.Choice(
                   title=_(u'Type of Offence'),
                   values=['Sedition','National Security','Fraud',
                           'Copyright','Defamation','Gaming/Betting',
                           'Threats to life/property','Hacking',]
                   )

    #Law
    #Enforcing Agency

    sector_type = schema.Choice(
                  title=_('Sector Type'),
                  values=['Academia','Media','Private Sector',
                          'Government','Civil Society','Public',]
                  )

alsoProvides(IIncident, IFormFieldProvider)
