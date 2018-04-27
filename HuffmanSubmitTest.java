public class HuffmanSubmitTest{


    public static void main (String[] args) {

        Huffman submit = new HuffmanSubmit();
      
        submit.encode("alice30.txt", "alice30.e", "alicefreq.txt");
        submit.decode("alice30.e", "alice30dec.txt", "alicefreq.txt");
        submit.encode("ur.jpg", "ur.e", "urfreq.txt");
        submit.decode("ur.e", "ur_decode.jpg", "urfreq.txt");
    }


}
