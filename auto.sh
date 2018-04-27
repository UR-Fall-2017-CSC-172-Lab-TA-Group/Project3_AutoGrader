javac HuffmanSubmitTest.java
java HuffmanSubmitTest

echo "Diff alice"
diff alice30.txt alice30dec.txt
echo "Diff nipple of knowledge"
diff ur.jpg ur_decode.jpg
echo "Diff done"
echo ""

echo "Byte Counts: "

echo "Alice:"
wc -c < alice30.txt
echo "Encoded Alice:"
wc -c < alice30.e

echo "ur.jpg"
wc -c < ur.jpg
echo "Encoded Nipple of Knowledge"
wc -c < ur.e
