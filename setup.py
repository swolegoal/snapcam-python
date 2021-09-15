from setuptools import setup
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

# install_requires breaks installing bluepy.  I don't know thy and I really
# don't care, so I did this:
pipmain(["install", "-r", "requirements.txt"])

scripts = ["scripts/enable-sc-wifi"]
setup(
    name="Snapcam",
    version="0.1",
    author="Andrew Rogers (@tuxlovesyou)",
    author_email="tuxlovesyou at g mail dot com",
    url="https://github.com/tuxlovesyou/Snapcam",
    packages=["Snapcam"],
    include_package_data=True,
    scripts=scripts,
)
