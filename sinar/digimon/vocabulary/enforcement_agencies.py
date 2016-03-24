from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class enforcement_agencies(grok.GlobalUtility):
    grok.name('sinar.digimon.enforcement_agencies')
    grok.implements(IVocabularyFactory)

    _terms = [
       {
        'value': '14c27117b54e46f2b57382a8aaa7b154',
        'title': 'Bank Negara Malaysia',
        'token': 'bnm',
        },
        {
            'value': '7e15cff930604463ac0195cc9bd017d6',
            'title': 'Companies Commission of Malaysia',
            'token': 'ssm',
        },
       {
        'value': '11af5d0168984556a86d545153f10fa0',
        'title': 'Ministry of Domestic Trade, Co-Operatives and Consumerism',
        'token': 'kpdnkk',
        },

        {
        'value': '55b7134d9a3fd0026f65fc30',
        'title': 'Royal Malaysian Police',
        'token': 'pdrm',
        },
    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
