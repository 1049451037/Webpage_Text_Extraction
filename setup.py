from setuptools import setup

setup(name='pextract',
      version='0.3',
      description='Extract main textual information from HTML.',
      url='https://github.com/1049451037/Webpage_Text_Extraction',
      author='Qingsong Lv',
      author_email='lqs@mail.bnu.edu.cn',
      license='MIT',
      packages=['pextract'],
      install_requires=[
          'beautifulsoup4',
		  'requests',
		  'lxml',
      ],
      zip_safe=False)