from distutils.core import setup
setup(
  name = 'ethsnarks_loopring',
  packages = ['ethsnarks_loopring'],
  version = '0.1',
  license='MIT',
  description = 'A toolkit for zkSNARKS signing specific to loopring',
  author = 'LinqLiquidityNetwork',
  author_email = 'michael@linq.network', 
  url = 'https://github.com/Linq-Liquidity-Network/ethsnarks-loopring',
  download_url = 'https://github.com/Linq-Liquidity-Network/ethsnarks-loopring/archive/v_01.tar.gz',
  keywords = ['crypto', 'loopring', 'SNARKS', 'zero-knowledge', 'ethereum'],
  install_requires=[
            'bitstring',
            'pysha3',
            'pyblake2'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)