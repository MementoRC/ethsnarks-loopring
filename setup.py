from setuptools import setup, find_packages

setup(
    name='ethsnarks_loopring',
    packages=find_packages(),
    version='0.1.6a1',
    license='MIT',
    description='A toolkit for zkSNARKS signing specific to loopring',
    author='LinqLiquidityNetwork',
    author_email='michael@linq.network',
    url='https://github.com/Linq-Liquidity-Network/ethsnarks-loopring',
    download_url='https://github.com/MementoRC/ethsnarks-loopring/archive/refs/tags/v0.1.6a1.tar.gz',
    keywords=['crypto', 'loopring', 'SNARKS', 'zero-knowledge', 'ethereum'],
    install_requires=[
        'bitstring',
        'safe-pysha3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
