from setuptools import find_packages, setup, file_packages

setup(
    name='uagents-ai-engine',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic',
    ],
    description='UAgents AI-Engine Integration Package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/uagents-ai-engine',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)