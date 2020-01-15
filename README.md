# MEDSTRUCT

Extract structure from medical narrative (Clinical NLP)
    
## Classifiers

### Lung cancer classification (TNM-8)
A rule-based algorithm to perform lung cancer t-stage classification on radiology reports ['Lung - Cancer TNM 8th edition'](http://www.radiologyassistant.nl/en/p58ef5eeb172c8/lung-cancer-tnm-8th-edition.html). 

Supported languages: 
  - Dutch
  - English 
  
- Accuracies
    - T: trained/validated for English and Dutch with an accuracy of approximately 0.85
    - N: trained/validated for Dutch with an accuracy of approximately 0.85
    - M: not implemented/feasible based on thorax scans

Expressions with uncertainty are detected and not used for classification.
  
The medstruct applications contains the following services and repositories:

### 1. Requirements 

   - [docker](https://www.docker.com/)
   - [git](https://git-scm.com/)
   
### 2. Install 
   
    git clone https://github.com/putssander/medstruct-config.git
    
    cd medstruct-config
    
    docker network create medstruct-network
    
### 3. Configuration

This repository is pre-configured.
- putssander/medstruct-config (THIS repository): configuration repository
 
Detailed configuration options are described in the repositories of each individual service.

list of services:
- [putssander/medstruct](https://github.com/putssander/medstruct): core component, containing read/write excel data, evaluations, text cleaning
- [putssander/spacy-json-nlp](https://github.com/putssander/spaCy-JSON-NLP): annotate text with spaCy into the json-nlp format
- [maastrodocker/pycontextnlp](https://github.com/maastroclinic/pycontextnlp): JSON-NLP wrapper around pyContextNLP to annotate clincal targets (clinical entities) and context (negations/uncertainty)
- [putssander/medstruct-measurement-extractor](https://github.com/putssander/medstruct-measurement-extractractor): extract and link measurements expressions to clinical concepts
- [putssander/medstruct-tnm-classifier](https://github.com/putssander/medstruct-tnm-classifier): lung classification (tnm-8)

If you want to perform classification on a excel file containg a batch for reports look  [putssander/medstruct](https://github.com/putssander/medstruct)


### RUN 

    docker-compose pull && docker-compose up -d
    
#### GUI    
    
The medstruct user interface will come available at: [http://localhost:8080](http://localhost:8080])

![Alt text](https://raw.githubusercontent.com/putssander/medstruct-gui/master/doc/MEDSTRUCT_GUI_2020-01-15.png?raw=true "MEDSTRUCT GUI")


#### Excel Lung TNM-classification
    
To run the algorithm on an excel sheet.  
   
       docker run -ti --rm --net medstruct-network -v '[LOCAL_PATH_IN_OUT]:/data/' -v ${PWD}/application.yml:/app/application.yml putssander/medstruct:2.0 python medstruct/xlsx_run.py /data/[XLSX_FILE_NAME] [RESULT_NAME]
       
   example
   
       docker run -ti --rm --net medstruct-network -v '/data/reports/t-stage/:/data/' -v ${PWD}/medstruct-application.yml:/app/application.yml putssander/medstruct:2.0 python medstruct/xlsx_run.py /data/t-stage-reports-val-copy.xlsx training-set
  
### FAQ

- "not a directory"

        \\\"not a directory\\\"\"": unknown: Are you trying to mount a directory onto a file (or vice-versa)?

    On Windows make sure to use the latest docker version (2.1.0.4 or newer)
    
