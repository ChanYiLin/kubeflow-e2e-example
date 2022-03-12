from setuptools import setup, find_packages

setup(
    name='transformer',
    version='0.1.0',
    author_email='chanyi.jack.lin@gmail.com',
    description='Transformer',
    python_requires='>=3.6',
    packages=find_packages("transformer"),
    install_requires=[
        "kfserving>=0.2.0",
        "argparse>=1.4.0",
        "requests>=2.22.0",
        "joblib>=0.13.2",
        "pandas>=0.24.2",
        "numpy>=1.16.3",
        "kubernetes >= 9.0.0",
        "Pillow == 9.0.1",
        "opencv-python-headless==4.0.0.21",
    ],
)
