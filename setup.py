from setuptools import setup
from ar_site_maker import version
setup(
    name="ar-site-maker",
    version=version,
    install_requires=["qrcode", "pymarker","Pillow","fire"],
    entry_points={
        'console_scripts': [
            'ar-site-maker = ar_site_maker:cli',
        ]
    }
)