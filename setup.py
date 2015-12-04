from setuptools import setup

config = {
	'description': 'VaxTools',
	'author': 'Bryan Briney',
	'url': 'www.github.com/briney/vaxtools/',
	# 'download_url': 'www.github.com/briney/abstar/',
	'author_email': 'briney@scripps.edu',
	'version': '0.1.0',
	'install_requires': ['nose',
						 'biopython',
						 'celery',
						 'ete2',
						 'matplotlib',
						 'numpy',
						 'nwalign',
						 'pandas',
						 'pymongo',
						 'scikit-bio',
						 'seaborn'],
	'packages': ['vaxtools'],
	# 'scripts': ['bin/vaxtools'],
	'name': 'vaxtools',
	'include_package_data': True
}

setup(**config)
