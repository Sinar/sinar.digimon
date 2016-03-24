from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class malaysian_acts(grok.GlobalUtility):
    grok.name('sinar.digimon.malaysian_acts')
    grok.implements(IVocabularyFactory)

    _terms = [
            
    {
        'value': 'cma',
        'title': 'Communications and Multimedia Act',
        'token': 'cma',
        },
   {
        'value': 'cca',
        'title': 'Computer Crimes Act',
        'token': 'cca',
        },

    {
        'value': 'companies',
        'title': 'Companies Act',
        'token': 'companies',
        },
    {
        'value': 'consumers',
        'title': 'Consumer Protection Act',
        'token': 'consumers',
        },
    {
        'value': 'gaming',
        'title': 'Common Gaming Houses Act',
        'token': 'gaming',
        },

    {
        'value': 'direct',
        'title': 'Direct Sales Act',
        'token': 'direct',
        },
    {
        'value': 'defamation',
        'title': 'Defamation Act',
        'token': 'defamation',
        },

    {
        'value': 'financial',
        'title': 'Financial Services Act',
        'token': 'financial',
        },

    {
        'value': 'pppa',
        'title': 'Printing Presses and Publications Act',
        'token': 'pppa',
        },
    {
        'value': 'sedition',
        'title': 'Sedition Act',
        'token': 'sedition',
        },
    {
        'value': 'sosma',
        'title': 'Security Offences (Special Measures) Act',
        'token': 'sosma',
        },
    {
        'value': 'poca',
        'title': 'Prevention of Crime Act',
        'token': 'poca',
        },
    {
        'value': 'pota',
        'title': 'Prevention of Terrorism Act',
        'token': 'pota',
        },
    {
        'value': 'penal',
        'title': 'Penal Code',
        'token': 'penal',
        },
   {
        'value': 'pool',
        'title': 'Pool Betting Act',
        'token': 'pool',
        },

    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
