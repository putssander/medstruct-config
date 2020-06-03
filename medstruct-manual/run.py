#!/usr/bin/env python
import subprocess
import os

current = os.getcwd()
medstruct_config_dir = current + "/medstruct-config/"

# PyContextNLP
os.environ["MODIFIERS"] = medstruct_config_dir + "pycontextnlp/" + "pycontextnlp_modifiers_nl.yml"
os.environ["TARGETS"] = medstruct_config_dir + "pycontextnlp/" + "pycontextnlp_tnm_targets_nl.yml"

# Spacy
os.environ["COREFERENCES"] = "false"
os.environ["CONSTITUENTS"] = "false"

# Java
os.environ["SPRING_PROFILES_ACTIVE"] = "rest,h2file"

os.environ["FLASK_APP"] = "./medstruct/medstruct/web/server.py"
medstruct = subprocess.Popen(["flask", "run" ,"-p", "8081"])

os.environ["FLASK_APP"] ="./spaCy-JSON-NLP/spacyjsonnlp/server.py"
spacy = subprocess.Popen(["flask", "run" ,"-p", "5001"])

os.environ["FLASK_APP"] ="./pyConTextNLP/pyConTextNLP/io/server.py"
pycontextnlp = subprocess.Popen(["flask", "run" ,"-p", "5031"])

gui = subprocess.Popen(["java", "-jar", 
		"./medstruct-gui/medstruct-gui-1.0.0.jar",
		"--spring.config.location=" + medstruct_config_dir + "medstruct-gui/"])
measurement = subprocess.Popen(["java", "-jar", 
		"./medstruct-measurement-extractor/medstruct-measurement-extractor-2.3.0.jar",
		"--spring.config.location="+ medstruct_config_dir + "medstruct-measurement-extractor/medstruct-measurement-extractor-application-nl.yml"])
classifier = subprocess.Popen(["java", "-jar", 
		"./medstruct-tnm-classifier/medstruct-tnm-classifier-2.2.2.jar",
		"--spring.config.location="+ medstruct_config_dir + "medstruct-tnm-classifier/medstruct-tnm-classifier-application-nl.yml"])

try:
	medstruct.wait()
	spacy.wait()
	pycontextnlp.wait()
	gui.wait()
	measurement.wait()
	classifier.wait()
except KeyboardInterrupt:
    try:
    	medstruct.terminate()
    	spacy.terminate()
    	pycontextnlp.terminate()
    	gui.terminate()
    	measurement.terminate()
    	classifier.terminate()
    except OSError:
    	pass
    medstruct.wait()
    spacy.wait()
    pycontextnlp.wait()
    gui.wait()
    measurement.wait()
    classifier.wait()