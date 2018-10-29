iconv -f GB2312 -t UTF-8 group2.xml > group3.xml

find *.xml -exec sh -c "iconv -f GB2312 -t UTF8 {} > ./format/{}" \;





字符串替换
1、将当前目录下包含jack串的文件中，jack字符串替换为tom
sed -i "s/jack/tom/g" `grep "jack" -rl ./`

2、将某个文件中的jack字符串替换为tom

sed -i "s/jack/tom/g" test.txt

替换xml中的编码从gb2312到utf-8
sed -i "s/encoding=\"gb2312\"/encoding=\"utf-8\"/g" `grep "encoding=\"gb2312\"" -rl ./`



操作步骤

1.将原始xml复制到data目录
2.执行`python gbk2utf8 "./state3/data"`，将xml文件转化为utf8格式并保存
3.执行 sed -i "s/encoding=\"gb2312\"/encoding=\"utf-8\"/g" `grep "encoding=\"gb2312\"" -rl ./state3/data` 将xml文件头文件的encoding从gb2312改为utf-8
4.进入对应模块执行 python app.py即可统计



