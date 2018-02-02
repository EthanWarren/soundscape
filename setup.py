from distutils.core import setup
def readme() :
    f=open("README.txt","r+")
    data=f.read()
    f.close()
    return data
setup(name="soundscape",author="Ethan Warren",version="1.0",packages=["soundscape"],install_requires=["pygame"],description="Package for the creation of audio games for the blind and visually impaired.",long_description=readme(),keywords="game blind accessibility accessible sound",include_package_data=True)