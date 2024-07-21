from setuptools import find_packages, setup
from codecs import open
from os import path

from tjwmd import __version__, __author__

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

SCRIPTS = [

]

PACKAGES = [
    'tjwmd'
]

REQUIRED_PACKAGES = [
    'certifi==2024.7.4',
    'charset-normalizer==3.3.2',
    'contourpy==1.2.1',
    'cycler==0.12.1',
    'filelock==3.15.4',
    'fonttools==4.53.1',
    'fsspec==2024.6.1',
    'idna==3.7',
    'Jinja2==3.1.4',
    'kiwisolver==1.4.5',
    'MarkupSafe==2.1.5',
    'matplotlib==3.9.1',
    'mpmath==1.3.0',
    'networkx==3.3',
    'numpy==1.26.4',
    'nvidia-cublas-cu12==12.1.3.1',
    'nvidia-cuda-cupti-cu12==12.1.105',
    'nvidia-cuda-nvrtc-cu12==12.1.105',
    'nvidia-cuda-runtime-cu12==12.1.105',
    'nvidia-cudnn-cu12==8.9.2.26',
    'nvidia-cufft-cu12==11.0.2.54',
    'nvidia-curand-cu12==10.3.2.106',
    'nvidia-cusolver-cu12==11.4.5.107',
    'nvidia-cusparse-cu12==12.1.0.106',
    'nvidia-nccl-cu12==2.20.5',
    'nvidia-nvjitlink-cu12==12.5.82',
    'nvidia-nvtx-cu12==12.1.105',
    'opencv-python==4.10.0.84',
    'packaging==24.1',
    'pandas==2.2.2',
    'pillow==10.4.0',
    'psutil==6.0.0',
    'py-cpuinfo==9.0.0',
    'pyparsing==3.1.2',
    'python-dateutil==2.9.0.post0',
    'pytz==2024.1',
    'PyYAML==6.0.1',
    'requests==2.32.3',
    'scipy==1.14.0',
    'seaborn==0.13.2',
    'six==1.16.0',
    'sympy==1.13.1',
    'torch==2.3.1',
    'torchvision==0.18.1',
    'tqdm==4.66.4',
    'triton==2.3.1',
    'typing_extensions==4.12.2',
    'tzdata==2024.1',
    'ultralytics==8.2.61',
    'ultralytics-thop==2.0.0',
    'urllib3==2.2.2'
]

setup(
    name='tjwmd',
    packages=find_packages(include=PACKAGES),
    scripts=SCRIPTS,
    version=__version__,
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    url="https://github.com/duynguyen02/tjwmd",
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ]
)
