from setuptools import find_packages, setup

# We don't declare our dependency on transformers here because we build with
# different packages for different variants

VERSION = "0.1.0"


# Ubuntu packages
# libsndfile1-dev: torchaudio requires the development version of the libsndfile package which can be installed via a system package manager. On Ubuntu it can be installed as follows: apt install libsndfile1-dev
# ffmpeg: ffmpeg is required for audio processing. On Ubuntu it can be installed as follows: apt install ffmpeg
# libavcodec-extra : libavcodec-extra  inculdes additional codecs for ffmpeg

install_requires = [
    # transformers
    "transformers[sklearn,sentencepiece]>=4.20.1",
    "Pillow",
    "starlette",
    "uvicorn",
    # "torch>=1.8.0",
    # "tensorflow>=2.4.0"
]

extras = {}

# test and quality
extras["test"] = [
    "pytest",
    "pytest-xdist",
    "parameterized",
    "psutil",
    "datasets",
    "pytest-sugar",
    "mock==2.0.0",
    "docker",
    "requests",
]
extras["quality"] = [
    "black",
    "isort",
    "flake8",
]


setup(
    name="hf_endpoints_emulator",
    version=VERSION,
    author="HuggingFace",
    description=".",
    url="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
    extras_require=extras,
    entry_points={"console_scripts": "emulate=hf_endpoints_emulator.emulator:emulate"},
    python_requires=">=3.8.0",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)