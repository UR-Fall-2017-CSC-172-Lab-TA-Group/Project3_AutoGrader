public class HuffmanSubmitTest{


  public static void main (String[] args) {

     Huffman  submit = new HuffmanSubmit();
     submit.encode("ur.jpg", "ur.e", "freq.txt");
     submit.decode("ur.e", "ur_decode.jpg", "freq.txt");
  }


}
