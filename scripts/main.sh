cd ../
for file in *.swf; do
    if [ -f "$file" ]; then
	rm -rf "$file.html"
        python3 ./scripts/mainexec.py "$file" > "$file.html"
	echo "<a href=\"${file}.html\" style='color:blue;'>${file}</a><br>" >> "ALL-MAIN.html"
	echo "Completed File $file"
    fi
done
