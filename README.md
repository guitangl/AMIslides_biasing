# Biasing List Extraction for AMI Slides

<!-- PIPELINE -->
<br />
<div align="center">
  <a>
    <img src="F2.pdf" alt="pipeline" width="80" height="80">
  </a>

  <h3 align="center">Visual-grounded Contextual ASR Pipeline</h3>
  </p>
</div>


### Contents:

`Biasing_list/` Directory containing biasing lists for each meeting series. Meetings series are represented using the common prefix, e.g. the ES2011 biasing list is for ES2011a-ES2011d, and IB40 biasing list is used for IB4001, IB4002, IB4003, IB4004, IB4010, IB4011. 

`OCR_raw` Raw OCR text files

`select_slides_words.py` Python script selecting words from the slides that are in the `full_rare_word_list.txt`. It generates `meeting_KB.json` and files in `Biasing_list/` for each meeting series.
