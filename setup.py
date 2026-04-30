import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='corpus2alpino',
                 version='0.3.13',
      description='Converts FoLiA and TEI files to Alpino XML files',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/UUDigitalHumanitieslab/corpus2alpino',
      author='Sheean Spoel, Digital Humanities Lab, Utrecht University',
      author_email='s.j.j.spoel@uu.nl',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      install_requires=['argparse', 'chamd>=0.5.13', 'folia',
                        'spacy', 'tei-reader', 'tqdm',
                        'numpy==1.24.4; python_version=="3.8"',
                        'numpy==1.26.4; python_version>="3.9" and python_version<"3.13"',
                        'numpy==2.1.3; python_version>="3.13"'],
      python_requires='>=3.8',
      zip_safe=True,
      entry_points={
          'console_scripts': [
              'corpus2alpino = corpus2alpino.__main__:main'
          ]
      })
