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

log = open('log/medstruct.log', 'a')  # so that data written to it will be appended
os.environ["FLASK_APP"] = "./medstruct/medstruct/web/server.py"
medstruct = subprocess.Popen(["flask", "run" ,"-p", "8081"], 
	stdout=log, stderr=log, shell=False)

log = open('log/spacyjsonnlp.log', 'a')  # so that data written to it will be appended
os.environ["FLASK_APP"] ="./spaCy-JSON-NLP/spacyjsonnlp/server.py"
spacy = subprocess.Popen(["flask", "run" ,"-p", "5001"], 
	stdout=log, stderr=log, shell=False)

log = open('log/pyConTextNLP.log', 'a')  # so that data written to it will be appended
os.environ["FLASK_APP"] ="./pyConTextNLP/pyConTextNLP/io/server.py"
pycontextnlp = subprocess.Popen(["flask", "run" ,"-p", "5031"], 
	stdout=log, stderr=log, shell=False)

log = open('log/gui.log', 'a')  # so that data written to it will be appended
gui = subprocess.Popen(["java", "-jar", 
		"./medstruct-gui/medstruct-gui-1.0.0.jar"],
		stdout=log, stderr=log, shell=False)

log = open('log/measurement.log', 'a')  # so that data written to it will be appended
measurement = subprocess.Popen(["java", "-jar", 
		"./medstruct-measurement-extractor/medstruct-measurement-extractor-2.3.0.jar",
		"--spring.config.location="+ medstruct_config_dir + "medstruct-measurement-extractor/medstruct-measurement-extractor-application-nl.yml"],
		stdout=log, stderr=log, shell=False)

log = open('log/classifier.log', 'a')  # so that data written to it will be appended
classifier = subprocess.Popen(["java", "-jar", 
		"./medstruct-tnm-classifier/medstruct-tnm-classifier-2.2.2.jar",
		"--spring.config.location="+ medstruct_config_dir + "medstruct-tnm-classifier/medstruct-tnm-classifier-application-nl.yml"],
		stdout=log, stderr=log, shell=False)

print("medstruct services opened ... (press ctrl + c to terminate)")

try:
	medstruct.wait()
	spacy.wait()
	pycontextnlp.wait()
	gui.wait()
	measurement.wait()
	classifier.wait()

except KeyboardInterrupt:
    try:
    	print("KeyboardInterrupt: medstruct services will terminate")
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