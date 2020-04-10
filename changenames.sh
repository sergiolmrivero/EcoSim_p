for i in *.py; do
    mv "$i" "${i// ./.}"
done
