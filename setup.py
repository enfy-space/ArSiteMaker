from setuptools import setup
setup(
    name="ar_site_maker",
    version="1.0.0",
    install_requires=["qrcode", "pymarker","Pillow","fire"],
    entry_points={
        'console_scripts': [
            'ar_site_maker = ar_site_maker:cli',
        ]
    }

)