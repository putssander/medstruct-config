# NON-Docker installation

1. Install [Java 11](https://adoptopenjdk.net/?variant=openjdk8&jvmVariant=hotspot)
2. Install [Python 3.7](https://www.python.org/downloads/)
3. Install git
4. Unzip medstruct-manual.zip 
5. Open medstruct-manual directory and clone the following repositories

        git clone https://github.com/putssander/medstruct-config.git
        git clone https://github.com/putssander/medstruct.git
        git clone -b pyjsonnlpmedstruct https://github.com/putssander/spaCy-JSON-NLP.git        
        git clone https://github.com/maastroclinic/pyConTextNLP.git
        
6. download releases (when not present):

    - [medstruct-gui](https://github.com/putssander/medstruct-gui/releases/download/1.0.0/medstruct-gui-1.0.0.jar) to ./medstruct-gui
    - [medstruct-tnm-classifier](https://github.com/putssander/medstruct-tnm-classifier/releases/download/2.2.2/medstruct-tnm-classifier-2.2.2.jar) to ./medstruct-tnm-classifier
    - [medstruct-measurement-extractor](https://github.com/putssander/medstruct-measurement-extractractor/releases/download/2.3.0/medstruct-measurement-extractor-2.3.0.jar) to ./medstruct-measurement-extractor
        
7. Install Python packages

8.1 Create and activate venv
       
        python3 -m venv medstruct-venv
        source medstruct-venv/bin/activate
        
8.2 Install medstruct
       
        pip install -e medstruct

8.3 Install spaCy-JSON-NLP (cython in advance?)
    
        cd spaCy-JSON-NLP
        pip install git+https://github.com/putssander/Py-JSON-NLP.git@json_payload_as_params       
        python setup.py install
        python -m spacy download en_core_web_sm
        python -m spacy download nl_core_news_sm
        cd ..

8.4 Install pyContextNLP      

        pip install -e pyConTextNLP
        python -m textblob.download_corpora

9. Boot services using Python run script
        
        source medstruct-venv/bin/activate
        python run.py

10. Stop services

        ctrl + c