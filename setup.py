from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='banking.statements.nordea',
      version=version,
      description="Account statement reader plugin for Nordea of Finland",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Utilities',
        'Environment :: Console',
        'Operating System :: OS Independent',
        ],
      keywords=['ofxstatement', 'ofx'],
      author='Petri Savolainen',
      author_email='petri.savolainen@koodaamo.fi',
      url='https://github.com/koodaamo/banking.statements.nordea',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['banking', 'banking.statements'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'ofxstatement'
      ],
      entry_points="""
      [ofxstatement]
      nordea = banking.statements.nordea.plugin:NordeaPlugin
      """,
      )
