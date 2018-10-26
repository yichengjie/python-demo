iconv -f GB2312 -t UTF-8 group2.xml > group3.xml

find *.xml -exec sh -c "iconv -f GB2312 -t UTF8 {} > ./format/{}" \;

