rm -rf rfflsrc
rm -rf astrosrc
mkdir astrosrc
cd astrosrc
git clone "https://github.com/derpferpmerp/astroUNL.git"
cd ../
mkdir rfflsrc
cd rfflsrc

curl -O -L "https://github.com/ruffle-rs/ruffle/releases/download/nightly-2021-06-08/ruffle-nightly-2021_06_08-web-selfhosted.zip"

unzip "ruffle-nightly-2021_06_08-web-selfhosted.zip"
rm -rf "ruffle-nightly-2021_06_08-web-selfhosted.zip"
mv * ../astrosrc/astroUNL
cd ../astrosrc/astroUNL
rm -rf "ALL-MAIN.html"
touch "ALL-MAIN.html"
echo "<div id=\"container\"> </div><body><strong>All SWFS</strong><p>" >> "ALL-MAIN.html"
for file in *.swf; do
    if [ -f "$file" ]; then
        python3 ../../mainexec.py "$file" > "$file.html"
				echo "<a href=\"${file}.html\" style='color:blue;'>${file}</a><br>" >> "ALL-MAIN.html"
				echo "Completed File $file"
    fi
done
echo "</p></body>" >> "ALL-MAIN.html"
