from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='sinar.digimon',
      version=version,
      description="Plone Dexterity Form for digital rights violation reports",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Sinar Project',
      author_email='team@sinarproject.org',
      url='http://github.com/sinar',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['sinar'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok, relations]',
          'plone.namedfile [blobs]',
          'collective.grok',
          'collective.dexteritytextindexer',
          'plone.app.multilingual',
          'plone.app.versioningbehavior',
          'plone.formwidget.contenttree',
          'plone.app.widgets',
          'five.pt',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],

      )
