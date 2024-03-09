There are 2 main function which Has to be written

1. Encode
2. Decode

### Encode

1. As we know we want to generate a short url and store the long url as value, so this looks like a ==key value== mapping. So we can store in a ==map==.
2. Since we dont want collision, we can maintain a counter for every request.
3. Since we use base 10 number, if the request reaches 1 billion 10000000000, this becomes a not a short url.
4. We can use another ==base x== system like base 16 or base 64.
5. In base 64 system we have ==0,1,2,3---9,A,B,C,D,E,-----X,Y,Z,a,b,c,----x,y,z,-,_==

````
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class UrlEncoder {

    private static final String[] BASE64_ARRAY = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "-", "_"};

    private int counter = 0;

    public String encodeCounterBased(String longUrl) {
        String encodedUrl = convertToBase64(counter++);
        return "bitly/" + encodedUrl;
    }

    public String encodeHashFunction(String longUrl) {
        String hashedUrl = sha256Hash(longUrl);
        String encodedUrl = convertToBase64(hashedUrl.hashCode());
        return "bitly/" + encodedUrl;
    }

    private String convertToBase64(int value) {
        StringBuilder result = new StringBuilder();
        while (value > 0) {
            int remainder = value % 64;
            result.append(BASE64_ARRAY[remainder]);
            value = value / 64;
        }
        return result.reverse().toString();
    }

    private String sha256Hash(String input) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(input.getBytes());

            return Base64.getEncoder().encodeToString(hash);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) {
        UrlEncoder urlEncoder = new UrlEncoder();

        String longUrl = "https://www.example.com";

        String encodedCounterBasedUrl = urlEncoder.encodeCounterBased(longUrl);
        String encodedHashFunctionUrl = urlEncoder.encodeHashFunction(longUrl);

        System.out.println("Original URL: " + longUrl);
        System.out.println("Encoded (Counter-Based) URL: " + encodedCounterBasedUrl);
        System.out.println("Encoded (Hash Function) URL: " + encodedHashFunctionUrl);
    }
}




````

We can pre-generate all the short url as they are not dependent on long url. 
we can use counter or hash function or hash plus counter or timestamp and store in some data structures.

Since, its pre generated, we can sort and remove collision.

