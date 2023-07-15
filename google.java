import java.io.IOException;
import java.net.URL;
import java.util.Scanner;

public class google{
    public static void main(String args[]) throws IOException{
        URL website = new URL("https://dummyjson.com/products");
        Scanner input = new Scanner(website.openStream());
        StringBuffer word = new StringBuffer();
        while (input.hasNext()){
            word.append(input.next());
        }
        String result = word.toString();
        System.out.println(result);
        
    }   

}

class product{
    Integer id;
    String titel;
    Integer price;
}