from distutils.core import setup
setup(
  name = 'voix',         # How you named your package folder (MyLib)
  packages = ['voix'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'It is a tiny library which can generate voice !',   # Give a short description about your library
  author = 'Tahmid Ahnaf',                   # Type in your name
  author_email = 'tahmidahnafxtra@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/tahmidahnaf/voix',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/tahmidahnaf/voix/archive/refs/tags/0.1.tar.gz',    # I explain this later on
  keywords = ['voix','voice','sound','sound generator','meaningfull sound generator' , 'voice generator'],   # Keywords that define your package best
  install_requires=[  
      'gtts',
      'googletrans',
      'playsound',
      'os'
],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)