# MEDSTRUCT

Extract structure from medical narrative (Clinical NLP)
    
## Lung cancer t-stage classification

A rule-based algorithm has been created to perform lung cancer t-stage classification based on ['Lung - Cancer TNM 8th edition'](http://www.radiologyassistant.nl/en/p58ef5eeb172c8/lung-cancer-tnm-8th-edition.html).

The results described in the article are produced using the following [tests/classify_report_tumor_t_test.py](/tests/classify_report_tumor_t_test.py)

Supported languages: Dutch
    
### Requirements:

-  Run pyContextNLP as a TCP service

        docker run --rm    -v '/Users/sanderputs/Documents/git/research/medstruct/medstruct/resources/tnmlung/lexical_kb_2019feb20_nl.yml:/opt/pyContextNLP/KB/custom_modifiers.yml'    -e OPTIONAL_ARGS='--modifiers=/opt/pyContextNLP/KB/custom_modifiers.yml'    -p 9999:9999 maastrodocker/pycontextnlp:1.0.0
- The used pyContextNLP modifiers in Dutch 'lexical_kb_2019feb20_nl.yml' can be downloaded [here](https://raw.githubusercontent.com/maastroclinic/medstruct/master/medstruct/resources/tnmlung/lexical_kb_2019feb20_nl.yml) (tag 1.0.0)
- Input data should be an excel file with 2 columns (report, tnm-label)


### Docker 

    docker network create medstruct-network

    docker-compose pull && docker-compose up -d

    docker run -ti --rm --net medstruct-network -v '/data/reports/t-stage/:/data/' -v ${PWD}/medstruct-application.yml:/app/application.yml putssander/medstruct:2.0 python medstruct/xlsx_run.py /data/t-stage-reports-val-copy.xlsx training-set
    
   docker run -ti --rm --net medstruct-network -v '[LOCAL_PATH_IN_OUT]:/data/' -v ${PWD}/application.yml:/app/application.yml putssander/medstruct:2.0 python medstruct/xlsx_run.py /data/[XLSX_FILE_NAME] [RESULT_NAME]
   
      docker run -ti --rm --net medstruct-network -v '/Users/sanderputs/DataSets/Research/TNM-LUNG/reproduce/tnm1/:/data/' -v ${PWD}/application.yml:/app/application.yml putssander/medstruct:boston2019 python medstruct/xlsx_run.py /data/t-stage-reports-train-latestlabel.xlsx result-tnm1train