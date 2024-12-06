
# Unstructured Data Extraction Tool

This software tool extracts information from unstructured documents. Users can input specific entities in the GUI (such as 'name', 'total amount', 'phone number', etc.) that they want extracted from the selected file. The supported file formats include .pdf, .jpg, .jpeg, .png, .tif, and .img. The tool generates the accurate output accordingly when the user presses the run button. 

The entire tool, including both logic and GUI components, is predominantly built using Python. The software architecture contains 2 main components: the Text Extraction Component and the Information Retrieval Component. The components are build up by modules. The Text Extraction Component contains the following files: preprocessing.py, ocr_extraction.py, spell_correction.py, and ai_correction.py. The Information Retrieval Component contains the following files: fuzzy_regex.py, ner_extraction.py, and ai_correction.py.

### Software Architecture

#### Main Modules
- The tool consists of two main modules: the Text Extraction Module and the Information Retrieval Module.

#### Text Extraction Module
- **Components**:
  - `preprocessing.py`
  - `ocr_extraction.py`
  - `spell_correction.py`
  - `ai_correction.py`

#### Information Retrieval Module
- **Components**:
  - `fuzzy_regex.py`
  - `ner_extraction.py`
  - `ai_correction.py`
