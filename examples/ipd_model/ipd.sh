rm runs/*.csv

cd ../../kernel

python3 main.py ../examples/ipd_model/ config.json ipd.json

cd ../examples/ipd_model

Rscript -e 'rmarkdown::render("ipd.Rmd", output_format="html_document")'
