mv runs/*.csv runs/previous_runs/.

cd ../../kernel

python3 main.py ../models/ref_br/ ref_br_config.json ref_br.json

cd ../models/ref_br

#Rscript -e 'rmarkdown::render("ref_br.rmd", output_format="html_document", output_dir="results")'

#firefox results/ref_br.html