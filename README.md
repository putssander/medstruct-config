# MEDSTRUCT

Extract structure from medical narrative (Clinical NLP)
    
## Lung cancer t-stage classification

Includes:

- A rule-based algorithm to perform lung cancer t-stage classification based on ['Lung - Cancer TNM 8th edition'](http://www.radiologyassistant.nl/en/p58ef5eeb172c8/lung-cancer-tnm-8th-edition.html). 
  Supported languages: Nederlands, English
    
### Requirements

- Docker

### RUN 

    docker network create medstruct-network

    docker-compose pull && docker-compose up -d
    
    
The MEDSTRUCT GUI will come available at: [http://localhost:8080](http://localhost:8080])
    
To run the algorithm on an excel sheet.  
   
       docker run -ti --rm --net medstruct-network -v '[LOCAL_PATH_IN_OUT]:/data/' -v ${PWD}/application.yml:/app/application.yml putssander/medstruct:2.0 python medstruct/xlsx_run.py /data/[XLSX_FILE_NAME] [RESULT_NAME]
       
   example
   
       docker run -ti --rm --net medstruct-network -v '/data/reports/t-stage/:/data/' -v ${PWD}/medstruct-application.yml:/app/application.yml putssander/medstruct:2.0 python medstruct/xlsx_run.py /data/t-stage-reports-val-copy.xlsx training-set

  
### FAQ

- "not a directory"

        \\\"not a directory\\\"\"": unknown: Are you trying to mount a directory onto a file (or vice-versa)?

    On Windows make sure to use the latest docker version (verified with 2.1.0.4)
    
