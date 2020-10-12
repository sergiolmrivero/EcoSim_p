rm runs/*.csv

cd ../../kernel

python3 main.py ../examples/ipd_model/ ipd_model_config.json ipd.json

cd ../examples/ipd_model


Rscript -e 'rmarkdown::render("ipd.Rmd", output_format="pdf_document", output_dir="results")'
