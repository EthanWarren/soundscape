from distutils.core import setup
def readme() :
    f=open("README.txt","r+")
    data=f.read()
    f.close()
    return data
setup(name="soundscape",author="Ethan Warren",author_email="ethanraviwarren@gmail.com",license="MIT",url="https://github.com/PythonicLegend/soundscape",platforms=["Mac OS","Windows","Linux"],version="1.0.0",packages=["soundscape"],requires=["pygame"],description="Package for the creation of audio games for the blind and visually impaired.",long_description=readme(),keywords="game blind accessibility accessible sound")