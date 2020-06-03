# NON-Docker installation

1. Install [Java 11](https://adoptopenjdk.net/?variant=openjdk8&jvmVariant=hotspot)
2. Install [Python 3.7](https://www.python.org/downloads/) (not tested with newer)
3. Intall git
4. Create a new directory (medstruct-manual) for this project and clone:

        git clone https://github.com/putssander/medstruct-config.git
        git clone https://github.com/putssander/medstruct.git
        git clone https://github.com/putssander/spaCy-JSON-NLP.git        
        git clone https://github.com/maastroclinic/pyConTextNLP.git
        
4. download releases:

    - [medstruct-gui](https://github.com/putssander/medstruct-gui/releases/download/1.0.0/medstruct-gui-1.0.0.jar) to ./medstruct-gui
    - [medstruct-tnm-classifier](https://github.com/putssander/medstruct-tnm-classifier/releases/download/2.2.2/medstruct-tnm-classifier-2.2.2.jar) to ./medstruct-tnm-classifier
    - [medstruct-measurement-extractor](https://github.com/putssander/medstruct-measurement-extractractor/releases/download/2.3.0/medstruct-measurement-extractor-2.3.0.jar) to ./medstruct-measurement-extractor
        
5. Install Python packages
    
        python3 -m venv medstruct-manual
        source medstruct-manual/bin/activate
        
        pip install -e medstruct
     
        pip install git+https://github.com/putssander/Py-JSON-NLP.git   
        cd spaCy-JSON-NLP
        python setup.py install
        cd ..
        pip install -e spaCy-JSON-NLP
        python -m spacy download en_core_web_sm
        python -m spacy download nl_core_news_sm
        
        pip install -e pyConTextNLP
        python -m textblob.download_corpora
 
 6. Run python
    
        cd medstruct-manual
        source medstruct-manual/bin/activate
        python run.py