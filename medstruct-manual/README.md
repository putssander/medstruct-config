# NON-Docker installation

## Installation

1. Install [Java 11](https://adoptopenjdk.net/?variant=openjdk8&jvmVariant=hotspot)
2. Install [Python x64](https://www.python.org/downloads/)
3. Install Git
4. Windows Only Install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
    Make sure u install MSVC and use "x64 Native Tools Command Prompt for VS 2019" as terminal
    
4. Unzip medstruct-manual.zip 
5. Open medstruct-manual directory and clone the following repositories

        git clone https://gitlab.com/medstruct/medstruct-config.git
        git clone https://gitlab.com/medstruct/medstruct.git
        git clone -b pyjsonnlpmedstruct https://github.com/putssander/spaCy-JSON-NLP.git        
        git clone https://github.com/maastroclinic/pyConTextNLP.git
        
6. download releases (when not present):

    - [medstruct-gui](https://github.com/putssander/medstruct-gui/releases/download/1.0.0/medstruct-gui-1.0.0.jar) to ./medstruct-gui
    - [medstruct-tnm-classifier](https://github.com/putssander/medstruct-tnm-classifier/releases/download/2.2.2/medstruct-tnm-classifier-2.2.2.jar) to ./medstruct-tnm-classifier
    - [medstruct-measurement-extractor](https://github.com/putssander/medstruct-measurement-extractractor/releases/download/2.3.0/medstruct-measurement-extractor-2.3.0.jar) to ./medstruct-measurement-extractor
        
7. Install Python packages

7.1 Create and activate venv

OSX:   
        
    $ python3 -m venv medstruct-venv
    $ source medstruct-venv/bin/activate

Windows:
       
    $ python -m venv medstruct-venv
    $ medstruct-venv\Scripts\activate
      
7.2 Install Cython

    $ pip install Cython
            
7.3 Install medstruct
       
    $ pip install -e medstruct

7.3 Install spaCy-JSON-NLP (numpy has to be set to ==1.14 on Windows)
    
    cd spaCy-JSON-NLP
    pip install git+https://github.com/putssander/Py-JSON-NLP.git@json_payload_as_params
    python setup.py install
    python -m spacy download en_core_web_sm
    python -m spacy download nl_core_news_sm
    cd ..

7.4 Install pyContextNLP      

        pip install -e pyConTextNLP
        python -m textblob.download_corpora

## Run

Boot services using Python run script
        
        source medstruct-venv/bin/activate
        python run.py

Log files are written in log/
