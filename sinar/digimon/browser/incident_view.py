from five import grok
from plone.directives import dexterity, form
from plone.dexterity.browser.view import DefaultView
from sinar.digimon.content.incident import IIncident

grok.templatedir('templates')

class View(DefaultView):
    grok.context(IIncident)
    grok.require('zope2.View')
    grok.template('incident_view')
    grok.name('view')
